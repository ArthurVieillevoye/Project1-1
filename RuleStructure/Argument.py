from enum import Enum
from Logic.Literal import Literal
from typing import List

class TestReason(Enum):
    TARGET_CONCLUSION = 0
    DEFEASIBLE_RULE = 1

def createTest(literal: Literal, testReason: TestReason):
    return Argument(support=[Literal('!' + str(literal) + '?', literal)], conclusion=Literal('!' + str(literal), literal), isTest=True, testReason=testReason)
    
class Argument:
    support: List[Literal]
    conclusion: Literal
    isTest: bool
    testReason: TestReason

    def __init__(self, support: List[Literal], conclusion: Literal, isTest: bool = False, testReason: TestReason = None):
        self.support = support
        self.conclusion = conclusion
        self.isTest = isTest
        self.testReason = testReason

    def __str__(self):
        return '({' + ', '.join(str(arg) for arg in self.support) + '}, ' + str(self.conclusion) + ')'
