from RuleStructure.Logic.Literals import Literals
from RuleStructure.Logic.Rules import Rules
from RuleStructure.ArgumentationRule import StrictRules, DefeasibleRules

class Program:
    facts = []
    strictrules = []
    defeasiblerules = []

    def addLiteral(self, literal):
        self.facts.append(literal)

    def addRule(self, rule):
        if (not rule.isDefeasible()):
            self.strictrules.append(rule)
        else:
            self.defeasiblerules.append(rule)

    def evaluate(self):
        for r in self.defeasiblerules:
            if r.isHeadValid():
                r.body.setValue(True)
            else:
                r.body.setValue(False)
        
            print(r.body.value)

        for r in self.strictrules:
            if r.isHeadValid():
                r.body.setValue(True)
            else:
                r.body.setValue(False)


if __name__ == '__main__':
    p = Program()

    a = Literals()
    b = Literals()
    c = Literals()
    p.addLiteral(a)
    p.addLiteral(b)
    p.addLiteral(c)

    a.setValue(True)
    b.setValue(False)

    r1 = Rules()
    r1.setOperator(0)
    r1.setHead(a)
    r1.setBody(b)

    r2 = Rules()
    r2.setOperator(1)
    r2.setHead(a)
    r2.setBody(b)

    sRule = StrictRules()
    sRule.setHead(r1)
    sRule.setBody(c)

    dRule = DefeasibleRules()
    dRule.setHead(r2)
    dRule.setBody(c)

    p.addRule(sRule)
    p.addRule(dRule)
    p.evaluate()

    print(c.value)