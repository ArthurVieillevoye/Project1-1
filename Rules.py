from enum import Enum
import Literals

class RuleType(Enum):
    STRICT = 0
    DEFEASIBLE = 1

class Operator(Enum):
    AND = 0
    OR = 1
    # IF = 2
    # IFF = 3

class Rules:
    type: RuleType
    head : Literals
    body : Literals
    operator : Operator

    def interpret(self):
        if (self.operator == Operator.AND):
            return self.head.interpret() and self.body.interpret()
        if (self.operator == Operator.OR):
            return self.head.interpret and self.body.interpret()

    def setOperator(self, op):
        if (op == 0):
            self.operator = Operator.AND
        elif (op == 1):
            self.operator = Operator.OR

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody