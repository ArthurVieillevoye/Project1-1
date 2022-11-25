from enum import Enum

class LitValue(Enum):
    FALSE = 0
    TRUE = 1
    VARIABLE = 2
    # TODO: Add the negation.

class Literals:
    def __init__(self) -> None:
        self.value = LitValue.VARIABLE

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