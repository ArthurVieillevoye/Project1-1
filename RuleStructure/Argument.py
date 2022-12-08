from enum import Enum
from RuleStructure.Logic.Literal import Literal
from typing import List, Union
from RuleStructure.Logic.Rule import Rule


def createTest(literal: Literal):
    if literal.isNegation:
        testLiteral = literal.negationOf
    else:
        testLiteral = Literal(negationOf=literal, isTest=True)
    return Argument(support=[testLiteral], conclusion=testLiteral)
    
class Argument:
    support: List
    conclusion = None

    def __init__(self, support: List, conclusion):
        self.support = support
        self.conclusion = conclusion

    def isAtomic(self):
        return type(self.conclusion) == Literal and (not self.conclusion.isNegation or not self.conclusion.negationOf.isNegation)

    def getSupportString(self, supportItem):
        if isinstance(supportItem, list):
            return '{' + ', '.join(self.getSupportString(arg) for arg in supportItem) + '}'
        else:
            return str(supportItem)

    def __str__(self):
        return '({' + ', '.join(self.getSupportString(arg) for arg in self.support) + '}, ' + str(self.conclusion) + ')'
