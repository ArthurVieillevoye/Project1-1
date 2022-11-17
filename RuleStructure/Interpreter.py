import pickle
import Rules
import Literals

class Interpreter:
    def saveRules(self, list_of_rules):
        with open('RuleStructure\\rules_data.pkl', 'wb') as outp:
            for r in list_of_rules:
                pickle.dump(r, outp, pickle.HIGHEST_PROTOCOL)
    
    def readRules(self):
        with open('RuleStructure\\rules_data.pkl', 'rb') as inp:
            rule1 = pickle.load(inp)


if __name__ == 'main':
    a = Literals.Literals()
    b = Literals.Literals()

    a.setValue(True)
    b.setValue(False)

    r1 = Rules.Rules()
    r1.setOperator(1)
    r1.setHead(a)
    r1.setBody(b)

    r2 = Rules.Rules()
    r2.setOperator(0)
    r2.setHead(a)
    r2.setBody(b)

    inter = Interpreter()
    inter.saveRules([r1, r2])