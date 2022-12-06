import copy
from enum import Enum
from RuleStructure.ArgumentationRule import DefeasibleRule
from RuleStructure.Logic.Literal import LitValue, Literal
from typing import List, Union
from RuleStructure.Logic.Rule import *
from RuleStructure.Argument import *
from RuleStructure.TableauRule import applyTableauRule

# class for each Node in an argumentation tableau
class TableauNode:
    # list of arguments in the current node
    arguments: List[Argument]
    # list of defeasibleRules available (only applicable if antecedent holds)
    defeasibleRules: List[DefeasibleRule]
    # list of Literals that hold in this node
    validLiterals: List[Literal]
    # left child node
    left: None #Node
    # right child node
    right: None #Node
    # indicator whether this node is closed
    isClosed: bool
    # arguments for closure of node
    closureArguments: List[Argument]

    def __init__(self, arguments: List[Argument], defeasibleRules: List[DefeasibleRule], right = None, left = None):
        self.validLiterals = []
        self.arguments = []
        # add arguments and fill valid literals
        for arg in arguments:
            self.addArgument(arg)
        
        self.defeasibleRules = defeasibleRules
        self.left = left
        self.right = right
        self.isClosed = False
        self.closureArguments = []

    # add argument to current node, and update valid literals if applicable
    def addArgument(self, argument):
        self.arguments.append(argument)
        if argument.isAtomic():
            self.validLiterals.append(argument.conclusion)


    def checkClosure(self):
        leftClosed = False
        rightClosed = False

        # check recursively for closure in child nodes
        if self.left:
            leftClosed, leftClosureArgs = self.left.checkClosure()
            self.closureArguments.extend(leftClosureArgs)

            # can't have right child without left child
            if self.right:
                rightClosed, rightClosureArgs = self.right.checkClosure()
                self.closureArguments.extend(rightClosureArgs)
            else:
                rightClosed = True
            
            # node is closed is all its childs are closed
            if leftClosed and rightClosed:
                self.isClosed = True
        
        # check only for leaf nodes
        else:
            # compare all atomic arguments pair-wise
            for idx1, arg1 in enumerate(self.arguments):
                if arg1.isAtomic():
                    for idx2, arg2 in enumerate(self.arguments):
                        if idx2 > idx1 and arg2.isAtomic():
                            # check if there are opposing conclusions (--> contradiction --> branch closure)
                            if arg1.conclusion.isNegation:
                                if arg1.conclusion.negationOf == arg2.conclusion:
                                    self.isClosed = True
                                    self.closureArguments.append(Argument(support=arg1.support + arg2.support, conclusion=Literal(stringRepresentation='⊥')))
                            elif arg2.conclusion.isNegation:
                                if arg1.conclusion == arg2.conclusion.negationOf:
                                    self.isClosed = True
                                    self.closureArguments.append(Argument(support=arg1.support + arg2.support, conclusion=Literal(stringRepresentation='⊥')))
                                    
        return self.isClosed, self.closureArguments

    def expandTree(self):
        tableauChanged = False
        leftChanged = False
        rightChanged = False

        # only expand if not already expanded
        if not self.left:
            for arg in self.arguments:
                if not arg.isAtomic() and not type(arg.conclusion) == DefeasibleRule:
                    # try applying tableau rules to all arguments (except atomic and defeasible rule arguments, no tableau rules can be applied there)
                    leftNodeArgs, rightNodeArgs = applyTableauRule(arg)
                    
                    # if tableau rule was applied, create child node(s) and copy all other arguments to child node(s)
                    if leftNodeArgs:
                        tableauChanged = True
                        self.left = TableauNode(arguments=leftNodeArgs, defeasibleRules=self.defeasibleRules)
                        for arg2 in self.arguments:
                            if arg != arg2:
                                self.left.addArgument(arg2)
                        
                        if rightNodeArgs:
                            self.right = TableauNode(arguments=rightNodeArgs, defeasibleRules=self.defeasibleRules)
                            for arg2 in self.arguments:
                                if arg != arg2:
                                    self.right.addArgument(arg2)
                        break
        
        # apply rules in child nodes recusively
        if self.left:
            leftChanged = self.left.expandTree()

        if self.right:
            rightChanged = self.right.expandTree()

        tableauChanged = tableauChanged or leftChanged or rightChanged

        return tableauChanged

    def checkDefeasibleRules(self):        
        
        leftDefRulesChanged = False
        rightDefRulesChanged = False
        defeasibleRulesChanged = False
        
        # check defeasible rules in left child-branch if applicable
        if self.left:
            leftDefRulesChanged = self.left.checkDefeasibleRules()

            # check defeasible rules in left child-branch if applicable (can't have right child, without left child)
            if self.right:
                rightDefRulesChanged = self.right.checkDefeasibleRules()
        
        # only check in leaf nodes
        else:

            # check for any undercutting defeaters, before applying defeasible rules
            for defRule in self.defeasibleRules:
                if self.isValidInNode(defRule):
                    defRule.defeatConsequence()
            
            # when filtered for undercutting defeaters, add arguments for applicable defeasible rules
            for defRule in self.defeasibleRules:
                if not defRule.isDefeated and not defRule.wasApplied:
                    for arg in self.arguments:
                        if arg.conclusion == defRule.antecedent:
                            self.addArgument(Argument(support=arg.support, conclusion=defRule))
                            self.addArgument(Argument(support=[Argument(support=arg.support, conclusion=defRule)], conclusion=defRule.consequence))
                            defRule.wasApplied = True

                            defeasibleRulesChanged = True


        return leftDefRulesChanged or rightDefRulesChanged or defeasibleRulesChanged

    # check, whether a given term holds valid in the current node
    def isValidInNode(self, term):
        # literal is valid, if it is in list of valid literals for this node
        if type(term) == Literal:
            if term in self.validLiterals:
                return True
        # interpret rule to check value, pass valid literals for evaluation
        elif type(term) == Rule:
            return term.interpret(self.validLiterals)

        # defeasible rule is valid if undefeated and its antecedent holds
        elif type(term) == DefeasibleRule:
            return not term.isDefeated and self.isValidInNode(term.antecedent)

    
    def evaluate(self):
        pass