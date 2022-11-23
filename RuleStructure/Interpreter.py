import pickle
from Logic.Rule import *
from Logic.Literal import Literal
from ArgumentationRule import DefeasibleRule
from Argument import *

class Interpreter:
    def saveRules(self, list_of_rules):
        with open('RuleStructure\\rules_data.pkl', 'wb') as outp:
            for r in list_of_rules:
                pickle.dump(r, outp, pickle.HIGHEST_PROTOCOL)
    
    def readRules(self):
        with open('RuleStructure\\rules_data.pkl', 'rb') as inp:
            rule1 = pickle.load(inp)


if __name__ == '__main__':

    p = Literal(stringRepresentation='p')
    q = Literal(stringRepresentation='q')
    r = Literal(stringRepresentation='r')
    s = Literal(stringRepresentation='s')

    sigma = [Rule(p, Operator.OR, q), Literal(stringRepresentation='!q', negationOf=q)] #inital information
    D = [DefeasibleRule(p, r), DefeasibleRule(r, s)] #defeasible rules

    root_arguments = []

    for clause in sigma:
        root_arguments.append(Argument(support=[clause], conclusion=clause))

    for defRule in D:
        root_arguments.append(createTest(defRule.antecedent, TestReason.DEFEASIBLE_RULE))

    root_arguments.append(createTest(s, TestReason.TARGET_CONCLUSION))

    print([str(arg) for arg in root_arguments])
