from enum import Enum

class LitValue(Enum):
    FALSE = 0
    TRUE = 1
    VARIABLE = 2

    
class Literals:
    value: LitValue

    def interpret():
        if self.value == LitValue.VARIABLE:
            return 'This literal is still a variable'
        else :
            return (self.value == LitValue.TRUE)

    def modifyValue(newVal):
        if (newVal):
            value = LitValue.TRUE
        else: 
            value = LitValue.FALSE