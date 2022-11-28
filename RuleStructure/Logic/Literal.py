from enum import Enum

class LitValue(Enum):
    FALSE = 0
    TRUE = 1
    VARIABLE = 2

class Literal:
    value: LitValue
    stringRepresentation: str
    isNegation: bool
    negationOf: None # Literal

    def __init__(self, stringRepresentation: str = None, negationOf = None):
        self.stringRepresentation = stringRepresentation
        self.negationOf = negationOf
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False

    def interpret(self):
        if self.value == LitValue.VARIABLE:
            return 'This literal is still a variable'
        else :
            return (self.value == LitValue.TRUE)

    def setValue(self, newVal):
        if (newVal):
            self.value = LitValue.TRUE
        else: 
            self.value = LitValue.FALSE

    def __str__(self):
        if self.isNegation:
            return '¬' + str(self.negationOf)
        else:
            return self.stringRepresentation