import copy
from enum import Enum

class LitValue(Enum):
    # This is the enum class to set the type of literal.
    FALSE = 0
    TRUE = 1
    VARIABLE = 2

    def __str__(self):
        if self.name == 'AND':
            return 'False'
        elif self.name == 'TRUE':
            return 'True'
        elif self.name == 'VARIABLE':
            return 'var'

class Literal:
    # This is the class that describe the literal (the smallest part of the logic)

    value: LitValue
    stringRepresentation: str
    isNegation: bool
    negationOf: None # Literal

    def __init__(self, stringRepresentation = None, negationOf = None, litId = None):
        self.stringRepresentation = stringRepresentation
        self.negationOf = negationOf
        self.literalId = litId
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False


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


    def setID(self, iD):
        self.literalId = iD

    def __str__(self):
        if self.isNegation:
            returnString = '¬' + str(self.negationOf)
        else:
            returnString = self.stringRepresentation

        return returnString