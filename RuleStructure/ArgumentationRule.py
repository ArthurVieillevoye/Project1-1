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

    def __init__(self, antecedent, consequence):
        self.antecedent = antecedent
        self.consequence = consequence

    def isHeadValid(self):
        return self.head.interpret()

    def isDefeasible(self):
        return True

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody

    def __str__(self):
        return str(self.antecedent) + ' ~~> ' + str(self.consequence)