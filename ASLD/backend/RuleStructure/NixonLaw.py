from Logic.Literal import Literal
from Logic.Rule import *
from ArgumentationRule import StrictRule, DefeasibleRule
from TableauRule import *


a = Literal(stringRepresentation='Person is Quaker')
b = Literal(stringRepresentation='Person is Republican')
c = Literal(stringRepresentation='Person is Pacifist')

d1 = DefeasibleRule(a, c, ruleId = 1)
d2 = DefeasibleRule(b, createNegation(c), ruleId = 2)

sigma = [a, b] #inital information
D = [d1, d2] #defeasible rules
        
order = [[0,0],[0,0]]