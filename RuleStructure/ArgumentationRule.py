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
    # This defeasible rule is composed of an head antecedent a consequence. When the antecedent is true, the consequence can be set to True.

    antecedent = None # Union(Literal, Rule, DefeasibleRule)
    consequence = None # Union(Literal, Rule, DefeasibleRule)

    # indication whether the consequence is a negated defeasible rule like: a ~~> (b ~/~> c) (or a ~~> not(b ~~> c))
    isNegation: bool

    # defeasible rule which is the negated consequence in case of negated rule
    negationOf: None # DefeasibleRule

    # value by which to order rules in case of contradictions
    orderValue: int

    # indicates, whether the rule was already applied in the current Node (True after antecedent holds and no undercutting defeaters)
    wasApplied: bool

    # indicates, whether the rule was defeated by an undercutting defeater
    isDefeated: bool



    def __init__(self, 
                 antecedent = None, 
                 consequence = None, 
                 negationOf = None, 
                 orderValue: int = 1
                ):
        self.antecedent = antecedent
        self.consequence = consequence
        self.negationOf = negationOf
        self.orderValue = orderValue
        self.wasApplied = False
        self.isDefeated = False
        
        if negationOf:
            self.isNegation = True
        else:
            self.isNegation = False

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

    # set conseqence to defeated (this is undercutting defeater)
    def defeatConsequence(self):
        if type(self.consequence) == DefeasibleRule and self.consequence.isNegation:
            self.consequence.negationOf.isDefeated = True
            self.consequence.negationOf.resetConsequence()
    
    # reset "defeated" flag on consequence if this rule was undercutting defeater, but defeated by another undercutting defeater
    def resetConsequence(self):
        if type(self.consequence) == DefeasibleRule and self.consequence.isNegation:
            self.consequence.negationOf.isDefeated = False


    def __str__(self):
        if self.isNegation:
            return '(' + str(self.negationOf.antecedent) + ' ~/~> ' + str(self.negationOf.consequence) + ')'
        else:
            return str(self.antecedent) + ' ~~> ' + str(self.consequence)