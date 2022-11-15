from enum import Enum

class RuleType(Enum):
    STRICT = 0
    DEFEASIBLE = 1

class Rules:
    type: RuleType