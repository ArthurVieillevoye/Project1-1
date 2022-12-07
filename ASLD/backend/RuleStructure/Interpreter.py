import pickle
from Logic.Rule import *
from Logic.Literal import Literal
from ArgumentationRule import DefeasibleRule
from Argument import *

class Interpreter:
    # This class is used to save the rules and to read the rules from a file.
    # Those rules will be the implementation of the laws.

    def saveRules(self, list_of_rules):
        # This methods saves the rules in a file using Pickle.
        with open('RuleStructure\\rules_data.pkl', 'wb') as outp:
            for r in list_of_rules:
                pickle.dump(r, outp, pickle.HIGHEST_PROTOCOL)
    
    def readRules(self):
        # This method reads the rules from a file.
        with open('RuleStructure\\rules_data.pkl', 'rb') as inp:
            rule1 = pickle.load(inp)


if __name__ == '__main__':
    pass