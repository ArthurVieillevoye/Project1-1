from enum import Enum
import RuleStructure.Logic.Literal

class Operator(Enum):
    AND = 0
    OR = 1
    IF = 2
    IFF = 3

    def __str__(self):
        if self.name == 'AND':
            return '∧'
        elif self.name == 'OR':
            return '∨'
        elif self.name == 'IF':
            return '-->'
        elif self.name == 'IFF':
            return '<-->'

class Rule:
    head = None # Union(Rule, Literal)
    operator : Operator
    body : None # Union(Rule, Literal)
    isNegation: bool
    negationOf: None # Rule

    def __init__(self, head = None, operator: Operator = None, body = None, negationOf = None):
        self.head = head 
        self.operator = operator
        self.body = body
        self.negationOf = negationOf
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False

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
        if self.isNegation:
            return '¬(' + str(self.negationOf) + ')'
        return str(self.head) + ' ' + str(self.operator) + ' ' + str(self.body)