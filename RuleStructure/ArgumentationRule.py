from typing import Generic, TypeVar, Union

class StrictRule:
    head: None
    body: None

    def isHeadValid(self):
        return self.head.interpret()

    def isDefeasible(self):
        return False

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody


class DefeasibleRule():
    antecedent = None # Union(Literal, Rule, DefeasibleRule)
    consequence = None # Union(Literal, Rule, DefeasibleRule)
    isNegation: bool
    negationOf: None # DefeasibleRule
    orderValue: int

    def __init__(self, antecedent = None, consequence = None, negationOf = None, orderValue: int = 1):
        self.antecedent = antecedent
        self.consequence = consequence
        self.negationOf = negationOf
        self.orderValue = orderValue
        
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False

    def isHeadValid(self):
        return self.head.interpret()

    def isDefeasible(self):
        return True

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody

    def __str__(self):
        if self.isNegation:
            return '(' + str(self.negationOf.antecedent) + ' ~/~> ' + str(self.negationOf.consequence) + ')'
        else:
            return str(self.antecedent) + ' ~~> ' + str(self.consequence)