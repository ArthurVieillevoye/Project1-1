from .Logic.Literal import Literal
from .Logic.Rule import *
from .ArgumentationRule import StrictRule, DefeasibleRule
from .TableauRule import *

def getData():
    a = Literal(stringRepresentation='Person signs a contract', litId=1)
    b = Literal(stringRepresentation='Person is under the age of 14', litId=2)
    c = Literal(stringRepresentation='Guardian approved the contract', litId=3)
    d = Literal(stringRepresentation='Person is bound by the contract', litId=4)

    d1 = DefeasibleRule(a, d, ruleId = 1)
    d2 = DefeasibleRule(antecedent = Rule(a, Operator.AND, b), consequence = createNegation(d), ruleId = 2)
    d3 = DefeasibleRule(antecedent = Rule(Rule(a, Operator.AND, b), Operator.AND, c), consequence = d, ruleId = 3)

    literalsList = [a, b, c] #inital information
    defeasibleRulesList = [d1, d2, d3] #defeasible rules
            
    order = [[0,2,2],[1,0,2],[1,1,0]]

    return [literalsList, defeasibleRulesList, order]