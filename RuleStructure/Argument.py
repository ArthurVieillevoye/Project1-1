from enum import Enum
from RuleStructure.Logic.Literal import Literal
from typing import List, Union
from RuleStructure.Logic.Rule import Rule

class TestReason(Enum):
    TARGET_CONCLUSION = 0
    DEFEASIBLE_RULE = 1

def createTest(literal: Literal, testReason: TestReason):
    return Argument(support=[Literal('¬' + str(literal) + '?', literal)], conclusion=Literal('¬' + str(literal), literal), isTest=True, testReason=testReason)
    
class Argument:
    support: List
    conclusion = None
    isTest: bool
    testReason: TestReason

    def __init__(self, support: List, conclusion, isTest: bool = False, testReason: TestReason = None):
        self.support = support
        self.conclusion = conclusion
        self.isTest = isTest
        self.testReason = testReason

    def isAtomic(self):
        return type(self.conclusion) == Literal

    def __str__(self):
        return '({' + ', '.join(str(arg) for arg in self.support) + '}, ' + str(self.conclusion) + ')'