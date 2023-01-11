from enum import Enum

from .Literal import Literal

class Operator(Enum):
    # This class describes the operator that compose the rule.
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
    # This class contains the description of the logical rules. This class is composed of a head and a body.
    # The head and the body are related by the operator that is set using the previous class (Operator).
    # This class is also composed of a boolean that says if the operation is negated of not.

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

    def interpret(self, validLiterals):
        # This method return the value of the literal (true, false, or a message if it is still a variable).
        headValue = False
        bodyValue = False

        if type(self.head) == Rule:
            headValue = self.head.interpret(validLiterals)
        elif type(self.head) == Literal:
            if self.head in validLiterals:
                headValue = True

        if type(self.body) == Rule:
            bodyValue = self.body.interpret(validLiterals)
        elif type(self.body) == Literal:
            if self.body in validLiterals:
                bodyValue = True

        if (self.operator == Operator.AND):
            return headValue and bodyValue
        elif (self.operator == Operator.OR):
            return headValue or bodyValue

    def setOperator(self, op):
        # Setter method. Set the operator of the rule.
        if (op == 0):
            self.operator = Operator.AND
        elif (op == 1):
            self.operator = Operator.OR

    def setHead(self, newHead):
        # Setter method. Set the head of the rule.
        self.head = newHead

    def setBody(self, newBody):
        # Setter method. Set the body of the rule.
        self.body = newBody

    def __str__(self):
        if self.isNegation:
            return '¬(' + str(self.negationOf) + ')'
        return str(self.head) + ' ' + str(self.operator) + ' ' + str(self.body)