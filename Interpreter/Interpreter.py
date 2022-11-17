
class Interpreter:
    def read(self):
        f = open('Interpreter\\savedRules.txt', 'r')
        self.translateRules(f.readlines())
    
    def translateRules(self,r):
        for rule in r:
            rule = rule.split('V')




inter = Interpreter()
inter.read()