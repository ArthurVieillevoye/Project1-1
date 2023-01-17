from enum import Enum
from .Logic.Literal import Literal
from typing import List, Union
from .Logic.Rule import Rule


def createTest(literal: Literal):
    if literal.isNegation:
        #testLiteral = Literal(stringRepresentation=str(literal.negationOf), isTest=True)
        testLiteral = literal.negationOf
        #testLiteral.isTest = True
    else:
        testLiteral = Literal(negationOf=literal)
        #testLiteral = Literal(negationOf=literal)
    return Argument(support=[testLiteral], conclusion=testLiteral, isTest=True)
    
class Argument:
    support: List
    conclusion = None
    attacks: List
    attackedBy: List
    isTest: bool
    depth: int

    def __init__(self, support: List, conclusion, isTest=False):
        self.support = support
        self.conclusion = conclusion
        self.isTest = isTest
        self.attacks = []
        self.attackedBy = []
        self.depth = 0
        self.calcDepth()

    def calcDepth(self):
        maxDepth = 0
        for item in self.support:
            if type(item) == Argument and item.depth > maxDepth:
                maxDepth = item.depth

        self.depth = 1 + maxDepth

    def isAtomic(self):
        return type(self.conclusion) == Literal and (not self.conclusion.isNegation or not self.conclusion.negationOf.isNegation)

    def getSupportString(self, supportItem):
        if isinstance(supportItem, list):
            return '{' + ', '.join(self.getSupportString(arg) for arg in supportItem) + '}'
        else:
            return str(supportItem)

    def __str__(self):
        support = ', '.join(self.getSupportString(arg) for arg in self.support)
        conclusion = str(self.conclusion)

        if self.isTest:
            support = support + '?'
            conclusion = conclusion + '?'
        return '({' + support + '}, ' + conclusion + ')'
