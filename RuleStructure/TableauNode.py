import copy
from enum import Enum
from RuleStructure.ArgumentationRule import DefeasibleRule
from RuleStructure.Logic.Literal import LitValue, Literal
from typing import List, Union
from RuleStructure.Logic.Rule import *
from RuleStructure.Argument import *
from RuleStructure.TableauRule import applyTableauRule

class TableauNode:
    arguments: List[Argument]
    defeasibleRules: List[DefeasibleRule]
    left: None #Node
    right: None #Node
    isClosed: bool
    closureArguments: List[Argument]

    def __init__(self, arguments: List[Argument], defeasibleRules: List[DefeasibleRule], right = None, left = None):
        self.arguments = arguments
        self.defeasibleRules = defeasibleRules
        self.left = left
        self.right = right
        self.isClosed = False
        self.closureArguments = []

    def addArgument(self, argument):
        self.arguments.append(argument)

    def checkClosure(self):
        leftClosed = False
        rightClosed = False

        if self.left:
            leftClosed, leftClosureArgs = self.left.checkClosure()
            self.closureArguments.extend(leftClosureArgs)
            if self.right:
                rightClosed, rightClosureArgs = self.right.checkClosure()
                self.closureArguments.extend(rightClosureArgs)
            else:
                rightClosed = True
            
            if leftClosed and rightClosed:
                self.isClosed = True
        else:
            for i in range(len(self.arguments)):
                if self.arguments[i].isAtomic():
                    for j in range(i + 1, len(self.arguments)):
                        if self.arguments[j].isAtomic():
                            if self.arguments[i].conclusion.isNegation:
                                if self.arguments[i].conclusion.negationOf == self.arguments[j].conclusion:
                                    self.isClosed = True
                                    self.closureArguments.append(Argument(support=self.arguments[i].support + self.arguments[j].support, conclusion=Literal(stringRepresentation='⊥')))
                            elif self.arguments[j].conclusion.isNegation:
                                if self.arguments[i].conclusion == self.arguments[j].conclusion.negationOf:
                                    self.isClosed = True
                                    self.closureArguments.append(Argument(support=self.arguments[i].support + self.arguments[j].support, conclusion=Literal(stringRepresentation='⊥')))
        
        return self.isClosed, self.closureArguments

    def expandTree(self):
        tableauChanged = False
        leftChanged = False
        rightChanged = False

        if not self.left:
            for i in range(len(self.arguments)):
                if not self.arguments[i].isAtomic() and not type(self.arguments[i].conclusion) == DefeasibleRule:
                    leftNodeArgs, rightNodeArgs = applyTableauRule(self.arguments[i])
                    if leftNodeArgs:
                        tableauChanged = True
                        self.left = TableauNode(arguments=leftNodeArgs, defeasibleRules=self.defeasibleRules)
                        for j in range(len(self.arguments)):
                            if j != i:
                                self.left.addArgument(self.arguments[j])
                        
                        if rightNodeArgs:
                            self.right = TableauNode(arguments=rightNodeArgs, defeasibleRules=self.defeasibleRules)
                            for j in range(len(self.arguments)):
                                if j != i:
                                    self.right.addArgument(self.arguments[j])
                        break
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

        if self.left:
            leftDefRulesChanged = self.left.checkDefeasibleRules()
            if self.right:
                rightDefRulesChanged = self.right.checkDefeasibleRules()
        

        else:
            defRules = copy.copy(self.defeasibleRules)

            for i in range(len(defRules)):
                for j in range(len(self.arguments)):
                    if defRules[i].antecedent == self.arguments[j].conclusion \
                     and type(defRules[i].consequence) == DefeasibleRule \
                     and defRules[i].consequence.isNegation:

                        if defRules[i].consequence.negationOf in self.defeasibleRules:
                            self.defeasibleRules.remove(defRules[i].consequence.negationOf)
                            #self.defeasibleRules.remove(defRules[i])

                            defeasibleRulesChanged = True

            defRules = copy.copy(self.defeasibleRules)

            for i in range(len(defRules)):
                for j in range(len(self.arguments)):
                    if defRules[i].antecedent == self.arguments[j].conclusion:

                        self.addArgument(Argument(support=self.arguments[j].support, conclusion=defRules[i]))
                        self.addArgument(Argument(support=[Argument(support=self.arguments[j].support, conclusion=defRules[i])], conclusion=defRules[i].consequence))
                        self.defeasibleRules.remove(defRules[i])

                        defeasibleRulesChanged = True


        return leftDefRulesChanged or rightDefRulesChanged or defeasibleRulesChanged


    
    def evaluate(self):
        pass