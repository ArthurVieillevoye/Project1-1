from Logic.Literal import Literal
from Logic.Rule import *
from ArgumentationRule import StrictRule, DefeasibleRule
from TableauRule import *

a = Literal(stringRepresentation='Person signs a contract')
b = Literal(stringRepresentation='Person is under the age of 14')
c = Literal(stringRepresentation='Guardian approved the contract')
d = Literal(stringRepresentation='Person is bound by the contract')

d1 = DefeasibleRule(a, d, ruleId = 1)
d2 = DefeasibleRule(antecedent = Rule(a, Operator.AND, b), consequence = createNegation(d), ruleId = 2)
d3 = DefeasibleRule(antecedent = Rule(Rule(a, Operator.AND, b), Operator.AND, c), consequence = d, ruleId = 3)

sigma = [a, b, c] #inital information
D = [d1, d2, d3] #defeasible rules
        
order = [[0,2,2],[1,0,2],[1,1,0]]