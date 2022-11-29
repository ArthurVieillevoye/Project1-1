from enum import Enum

class LitValue(Enum):
    # This is the enum class to set the type of literal.
    FALSE = 0
    TRUE = 1
    VARIABLE = 2

class Literal:
    # This is the class that describe the literal (the smallest part of the logic)

    value: LitValue
    stringRepresentation: str
    isNegation: bool
    negationOf: None # Literal
    isTest: bool

    def __init__(self, stringRepresentation: str = None, negationOf = None, isTest=False):
        self.stringRepresentation = stringRepresentation
        self.negationOf = negationOf
        self.isTest = isTest
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False
        
        if isTest:
            if self.stringRepresentation:
                self.stringRepresentation = self.stringRepresentation + '?'
            if self.isNegation:
                self.negationOf.stringRepresentation = self.negationOf.stringRepresentation + '?'

    def interpret(self):
        # This method return the value of the literal (true, false, or a message if it is still a variable).
        if self.value == LitValue.VARIABLE:
            return 'This literal is still a variable'
        else :
            return (self.value == LitValue.TRUE)

    def setValue(self, newVal):
        # Setter method. Set the value of the literal.
        if (newVal):
            self.value = LitValue.TRUE
        else: 
            self.value = LitValue.FALSE

    def __str__(self):
        if self.isNegation:
            return '¬' + str(self.negationOf)
        else:
            return self.stringRepresentation