from enum import Enum
from RuleStructure.ArgumentationRule import DefeasibleRule
from RuleStructure.Logic.Literal import LitValue, Literal
from typing import List, Union
from RuleStructure.Logic.Rule import *
from RuleStructure.Argument import *
from RuleStructure.TableauRule import applyTableauRule

class TableauNode:
    arguments: List[Argument]
    left = None
    right = None
    isClosed: bool = False
    closureArguments: List[Argument] = []
    nodeExpanded = False

    def __init__(self, arguments: List[Argument], right = None, left = None):
        self.arguments = arguments
        self.left = left
        self.right = right

    def addArgument(self, argument):
        self.arguments.append(argument)

    def checkClosure(self):
        leftClosed = False
        rightClosed = False

        #print(id(self))
        #print(id(self.left))
        #print(id(self.right))
        #print([str(arg) for arg in self.closureArguments])

        if self.left:
            leftClosed, leftClosureArgs = self.left.checkClosure()
            #print(id(self.left))
            #print([str(arg) for arg in leftClosureArgs])
            self.closureArguments.extend(leftClosureArgs)
        if self.right:
            rightClosed, rightClosureArgs = self.right.checkClosure()
            self.closureArguments.extend(rightClosureArgs)
        
        if leftClosed and rightClosed:
            self.isClosed = True

        for i in range(len(self.arguments)):
            if self.arguments[i].isAtomic():
                for j in range(i + 1, len(self.arguments)):
                    if self.arguments[j].isAtomic():
                        if self.arguments[i].conclusion.isNegation:
                            if self.arguments[i].conclusion.negationOf == self.arguments[j].conclusion:
                                self.isClosed = True
                                self.closureArguments.append(Argument(support=self.arguments[i].support + self.arguments[j].support, conclusion=Literal(stringRepresentation='⊥', isClosure=True)))
                        elif self.arguments[j].conclusion.isNegation:
                            if self.arguments[i].conclusion == self.arguments[j].conclusion.negationOf:
                                self.isClosed = True
                                self.closureArguments.append(Argument(support=self.arguments[i].support + self.arguments[j].support, conclusion=Literal(stringRepresentation='⊥', isClosure=True)))

                        #(id(self))
                        #print([str(arg) for arg in self.closureArguments])
        return self.isClosed, self.closureArguments

    def expandTree(self):
        for i in range(len(self.arguments)):
            leftNodeArgs, rightNodeArgs = applyTableauRule(self.arguments[i])
            if leftNodeArgs:
                self.left = TableauNode(arguments=leftNodeArgs)
                for j in range(len(self.arguments)):
                    if j != i:
                        self.left.addArgument(self.arguments[j])
                
                if rightNodeArgs:
                    self.right = TableauNode(arguments=rightNodeArgs)
                    for j in range(len(self.arguments)):
                        if j != i:
                            self.right.addArgument(self.arguments[j])
                break
        if self.left:
            self.left.expandTree()

        if self.right:
            self.right.expandTree()

        self.nodeExpanded = True

    def evaluate(self):
        pass