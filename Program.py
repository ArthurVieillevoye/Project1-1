from RuleStructure.Logic.Literal import Literal
from RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule

class Program:
    facts = []
    rules = []

    def addLiteral(self, literal):
        self.facts.append(literal)

    def addRule(self, rule):
        self.rules.append(rule)

    def Evaluate(self):
        # TODO: Here will lie the call or the code of the argumentation tableau ?
        pass
