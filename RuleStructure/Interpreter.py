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
    pass