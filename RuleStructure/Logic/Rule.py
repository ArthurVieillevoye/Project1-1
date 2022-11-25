from enum import Enum
import RuleStructure.Logic.Literals


class Operator(Enum):
    AND = 0
    OR = 1
    # IF = 2
    # IFF = 3

def __str__(self):
    return self.name
Operator.__str__ = __str__

class Rule:
    head = None # Union(Rule, Literal)
    operator : Operator
    body : None # Union(Rule, Literal)

    def __init__(self, head, operator: Operator, body):
        self.head = head 
        self.operator = operator
        self.body = body

    def interpret(self):
        if (self.operator == Operator.AND):
            return self.head.interpret() and self.body.interpret()
        elif (self.operator == Operator.OR):
            return self.head.interpret() or self.body.interpret()

    def setOperator(self, op):
        if (op == 0):
            self.operator = Operator.AND
        elif (op == 1):
            self.operator = Operator.OR

    def setHead(self, newHead):
        self.head = newHead

    def setBody(self, newBody):
        self.body = newBody

    def __str__(self):
        return self.head.stringRepresentation + ' ' + str(self.operator) + ' ' + self.body.stringRepresentation