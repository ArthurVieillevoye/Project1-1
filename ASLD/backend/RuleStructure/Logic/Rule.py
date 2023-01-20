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
        # This method returns the value of the literal (true, false, or a message if it is still a variable).
        headValue = False
        bodyValue = False

        if type(self.head) == Rule:
            headValue = self.head.interpret(validLiterals)
        elif type(self.head) == Literal:
            for literal in validLiterals:
                if self.head == literal or (self.head.isNegation and literal.isNegation and self.head.negationOf == literal.negationOf):
                    headValue = True
                    break

        if type(self.body) == Rule:
            bodyValue = self.body.interpret(validLiterals)
        elif type(self.body) == Literal:
            for literal in validLiterals:
                if self.body == literal or (self.body.isNegation and literal.isNegation and self.body.negationOf == literal.negationOf):
                    bodyValue = True
                    break

        if (self.operator == Operator.AND):
            return headValue and bodyValue
        elif (self.operator == Operator.OR):
            return headValue or bodyValue

    def constructSupport(self, currentArguments):
        # This method returns support for this rule, if it can be constructed on given arguments, return empty list otherwise.

        headSupport = []
        bodySupport = []

        # check for head and body support in existing arguments
        for arg in currentArguments:
            if self.head == arg.conclusion or (self.head.isNegation and arg.conclusion.isNegation and self.head.negationOf == arg.conclusion.negationOf):
                headSupport = headSupport + arg.support
            if self.body == arg.conclusion or (self.body.isNegation and arg.conclusion.isNegation and self.body.negationOf == arg.conclusion.negationOf):
                bodySupport = bodySupport + arg.support

        if len(headSupport) == 0 and type(self.head) == Rule:
            headSupport = self.head.constructSupport(currentArguments)
        
        if len(bodySupport) == 0 and type(self.body) == Rule:
            bodySupport = self.body.constructSupport(currentArguments)

        if (self.operator == Operator.AND):
            if len(headSupport) > 0 and len(bodySupport) > 0:
                return headSupport + bodySupport
            else:
                return []
        elif (self.operator == Operator.OR):
            if len(headSupport) > 0:
                return headSupport
            elif len(bodySupport) > 0:
                return bodySupport

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