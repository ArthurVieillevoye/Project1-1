from typing import Generic, TypeVar, Union

class StrictRule:
    # The strict rules are the rules that have the priority over the other rules. These rules must be true/
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
    # These class describes the defeasible rules.
    # The defeasible rules are the main rules that are used by the program to find a solution to a case.
    # This defeasible rule is composed of a head and a consequence. When the head is true, the consequence can be set to True.

    antecedent = None # Union(Literal, Rule, DefeasibleRule)
    consequence = None # Union(Literal, Rule, DefeasibleRule)

    def __init__(self, antecedent, consequence):
        self.antecedent = antecedent
        self.consequence = consequence

    def isHeadValid(self):
        # This method returns the value of the head (wheather the head is true or false).
        return self.head.interpret()

    def isDefeasible(self):
        #This methods return a boolean saying that the method is defeasible.
        return True

    def setHead(self, newHead):
        # Set the head of the rule to newHead.
        self.head = newHead
    
    def setBody(self, newBody):
        # Set the head of the rule to newBody.
        self.body = newBody

    def __str__(self):
        return str(self.antecedent) + ' ~~> ' + str(self.consequence)