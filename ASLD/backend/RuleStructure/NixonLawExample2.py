from .Logic.Literal import Literal
from .Logic.Rule import *
from .ArgumentationRule import StrictRule, DefeasibleRule
from .TableauRule import *

def getData():
    b = Literal(stringRepresentation='Person is Republican', litId=1)
    a = Literal(stringRepresentation='Person is Quaker', litId=2)
    c = Literal(stringRepresentation='Person is Pacifist', litId=3)

    d1 = DefeasibleRule(a, c, ruleId = 1)
    d2 = DefeasibleRule(b, createNegation(c), ruleId = 2)

    literalsList = [a, b] #inital information
    defeasibleRulesList = [d1, d2] #defeasible rules
            
    order = [[0,0],[0,0]]

    tests = [c]

    return [literalsList, defeasibleRulesList, order, tests]