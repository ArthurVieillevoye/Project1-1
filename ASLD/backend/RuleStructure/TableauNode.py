import copy
from enum import Enum
from .ArgumentationRule import DefeasibleRule
from .Logic.Literal import LitValue, Literal
from typing import List, Union
from .Logic.Rule import *
from .Argument import *
from .TableauRule import applyTableauRule, createNegation

# class for each Node in an argumentation tableau
class TableauNode:
    # list of arguments in the current node
    arguments: List[Argument]
    # list of defeasibleRules available (only applicable if antecedent holds)
    defeasibleRules: List[DefeasibleRule]
    # ordering of the defeasible rules
    order: List
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

    def __init__(self, arguments: List[Argument], defeasibleRules: List[DefeasibleRule], order: List = None, right = None, left = None):
        self.validLiterals = []
        self.arguments = []
        # add arguments and fill valid literals
        for arg in arguments:
            self.addArgument(arg)
        
        self.defeasibleRules = defeasibleRules
        self.order = order
        self.left = left
        self.right = right
        self.isClosed = False
        self.closureArguments = []

    # add argument to current node, and update valid literals if applicable
    def addArgument(self, argument):
        self.arguments.append(argument)
        if argument.isAtomic() and not argument.isTest:
            self.validLiterals.append(argument.conclusion)

    # return all arguments of the node and its children
    def getAllArguments(self):
        allArguments = []

        if self.left:
            allArguments.extend(self.left.getAllArguments())
            if self.right:
                allArguments.extend(self.right.getAllArguments())

        else:
            allArguments = copy.copy(self.arguments)

        args = allArguments.copy()

        for arg in args:
            if arg.isTest:
                allArguments.remove(arg)

        allArguments.sort(key=lambda x: (x.depth, len(x.support)))

        return list(set(allArguments))

        
    def checkClosure(self):
        leftClosed = False
        rightClosed = False

        self.isClosed = False
        self.closureArguments = []

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
                        if idx2 > idx1 and arg2.isAtomic() and not (arg1.isTest and arg2.isTest):
                            # check if there are opposing conclusions (--> contradiction --> branch closure)
                            if arg1.conclusion.isNegation and arg1.conclusion.negationOf == arg2.conclusion \
                                or arg2.conclusion.isNegation and arg1.conclusion == arg2.conclusion.negationOf:
                                    self.isClosed = True
                                    self.closureArguments.append(Argument(support=arg1.support + arg2.support, conclusion=Literal(stringRepresentation='⊥')))
                                    # note attack relation for later labeling
                                    self.updateAttackSymmetric(argument1=arg1, argument2=arg2)
                                    
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
                        self.left = TableauNode(arguments=leftNodeArgs, defeasibleRules=self.defeasibleRules, order=self.order)
                        for arg2 in self.arguments:
                            if arg != arg2:
                                self.left.addArgument(arg2)
                        
                        if rightNodeArgs:
                            self.right = TableauNode(arguments=rightNodeArgs, defeasibleRules=self.defeasibleRules, order=self.order)
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
            #for defRule in self.defeasibleRules:
            #    if self.isValidInNode(defRule):
            #        defRule.defeatConsequence()
            
            # when filtered for undercutting defeaters, add arguments for applicable defeasible rules
            for defRule in self.defeasibleRules:
                #if not defRule.isDefeated and not defRule.wasApplied:
                if not defRule.wasApplied:

                    argForDefRule = self.constructArgument(conclusion = defRule.antecedent)

                    if argForDefRule:
                        self.addArgument(Argument(support=argForDefRule.support, conclusion=defRule))
                        self.addArgument(Argument(support=[Argument(support=argForDefRule.support, conclusion=defRule)], conclusion=defRule.consequence))
                        
                        defRule.wasApplied = True
                        defeasibleRulesChanged = True


        return leftDefRulesChanged or rightDefRulesChanged or defeasibleRulesChanged


    # check for contradictions (without the test literals) and defeat weakest rule if possible
    def checkContradiction(self):
        newContradictionFound = False
        leftChanged = False
        rightChanged = False

        # check recursively for closure in child nodes
        if self.left:
            leftChanged = self.left.checkContradiction()

            # can't have right child without left child
            if self.right:
                rightChanged = self.right.checkContradiction()
        
        # check only for leaf nodes
        else:
            # check all atomic non-test arguments pair-wise for contradictions
            for idx1, arg1 in enumerate(self.arguments):
                if arg1.isAtomic() and not arg1.isTest:
                    for idx2, arg2 in enumerate(self.arguments):
                        if idx2 > idx1 and arg2.isAtomic() and not arg2.isTest:
                            # check if there are opposing conclusions (--> contradiction)
                            if arg1.conclusion.isNegation and arg1.conclusion.negationOf == arg2.conclusion \
                             or arg2.conclusion.isNegation and arg1.conclusion == arg2.conclusion.negationOf:
                                    contradictionSupport = arg1.support + arg2.support

                                    # identify weakest rule used in contradiction
                                    usedDefRules  = self.getUsedDefRules(contradictionSupport)
                                    weakestRules = self.getWeakestRules(usedDefRules)

                                    for weakestRule in weakestRules:
                                        # defeat weakest non-defeated rule
                                        if not weakestRule.isDefeated and not (self.isDefRuleUsedInArgument(weakestRule, arg1) and self.isDefRuleUsedInArgument(weakestRule, arg2)):
                                            newContradictionFound = True
                                            undercuttingArgSupport = self.getUndercuttingAttackSupport(support=contradictionSupport, defRule=weakestRule)
                                            weakestRule.isDefeated = True
                                            # create undercutting argument
                                            undercuttingArg = Argument(support = undercuttingArgSupport, conclusion = createNegation(weakestRule))
                                            # note attack relation for later labeling
                                            self.updateAttackRelationUndercuttingArg(undercuttingArgument=undercuttingArg, defeatedRule=weakestRule)
                                            # add undercutting argument to list of arguments
                                            self.addArgument(undercuttingArg)
                                            break

        return leftChanged or rightChanged or newContradictionFound

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

    # constructs an argument to support a given conclusion based on facts and rules in the current node, return None if not possible
    def constructArgument(self, conclusion):
        
        # can't find argument, if concluson is not valid
        if not self.isValidInNode(conclusion):
            return None

        # check, if argument already exists, then just return
        for arg in self.arguments:
            if arg.conclusion == conclusion and not arg.isTest:
                return arg

        # if target conclusion is a rule, try to build argument, based on valid literals and other arguments
        if type(conclusion) == Rule:
            argSupport = conclusion.constructSupport(self.arguments)
            if len(argSupport) > 0:
                return Argument(support=argSupport, conclusion=conclusion)
            else:
                return None

        # theoretical case, should not happen
        elif type(conclusion) == DefeasibleRule:
            print("warning, check defeasible rule")
            return self.constructArgument(conclusion.antecedent)

    
    # get all defeasible rules, that are used by a given list of support items of an argument
    def getUsedDefRules(self, support):
        usedDefRules = []
        for item in support:
            if type(item) == DefeasibleRule:
                usedDefRules.append(item)
            elif type(item) == Argument:
                if type(item.conclusion) == DefeasibleRule:
                    usedDefRules.append(item.conclusion)
                usedDefRules.extend(self.getUsedDefRules(item.support))

        return usedDefRules

    # remove support for given defeasible rule in list of support for a contradiction
    def getUndercuttingAttackSupport(self, support, defRule):
        undercuttingAttackSupport = support
        for item in support:
            if type(item) == Argument:
                if self.isDefRuleUsedInArgument(defRule=defRule, argument=item):
                    undercuttingAttackSupport.remove(item)

        return undercuttingAttackSupport
    
    # check recursively, whether a given defeasible rule is used in an given argument
    def isDefRuleUsedInArgument(self, defRule: DefeasibleRule, argument: Argument):
        if argument.conclusion == defRule:
            return True

        for item in argument.support:
            if item == defRule:
                return True
            elif type(item) == Argument and self.isDefRuleUsedInArgument(defRule=defRule, argument=item):
                return True

        return False

    # note attack relation for two arguments attacking each other
    def updateAttackSymmetric(self, argument1, argument2):
        if not (argument1.isTest or argument2.isTest):
            argument1.attacks.append(argument2)
            argument1.attackedBy.append(argument2)
            argument2.attacks.append(argument1)
            argument2.attackedBy.append(argument1)

            argument1.attacks = list(set(argument1.attacks))
            argument1.attackedBy = list(set(argument1.attackedBy))
            argument2.attacks = list(set(argument2.attacks))
            argument2.attackedBy = list(set(argument2.attackedBy))

    # note attack relation for all arguments using a defeated rule for later labeling
    def updateAttackRelationUndercuttingArg(self, undercuttingArgument, defeatedRule):
        for arg in self.arguments:
            if self.isDefRuleUsedInArgument(defRule=defeatedRule, argument=arg):
                if not arg.isTest:
                    undercuttingArgument.attacks.append(arg)
                    undercuttingArgument.attacks = list(set(undercuttingArgument.attacks))
                    arg.attackedBy.append(undercuttingArgument)
                    arg.attackedBy = list(set(arg.attackedBy))


    def findWeakRule(self, rules):
        weakRuleList = []
        for rule1 in rules:
            for rule2 in rules:
                if self.order[rule1.ruleId-1][rule2.ruleId-1] == 2 and rule1 not in weakRuleList:
                    weakRuleList.append(rule1)

        for rule1 in rules:
            differentThan0 = False
            for rule2 in rules:
                if self.order[rule1.ruleId-1][rule2.ruleId-1] != 0:
                    differentThan0 = True
            if rule1 not in weakRuleList and not differentThan0:
                weakRuleList.append(rule1)

        return weakRuleList

    

    def getWeakestRules(self, rules):
        newRuleList = []
        newRuleList = self.findWeakRule(rules)
        if len(newRuleList) == len(rules):
            return []
        while len(newRuleList) != len(rules):
            rules = newRuleList
            newRuleList = self.findWeakRule(rules)

        return rules

    # remove all arguments from node, that use a given (defeated) defeasible rule
    def removeWeakRuleArguments(self, defRule):
        currentArguments = copy.copy(self.arguments)
        for arg in currentArguments:
            if self.isDefRuleUsedInArgument(defRule=defRule, argument=arg):
                self.arguments.remove(arg)
    
    def evaluate(self):
        pass