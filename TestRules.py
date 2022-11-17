import RuleStructure.Logic.Literals as Literals
import RuleStructure.Logic.Rules as Rules

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

r3 = Rules.Rules()
r3.setOperator(0)
r3.setHead(r1)
r3.setBody(a)

print(r1.interpret())
print(r2.interpret())
print(r3.interpret())