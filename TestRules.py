import Literals
import Rules

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

print(r1.interpret())
print(r2.interpret())