import os


class Interpreter:
    def read(self):
        with open('Interpreter\\savedRules.txt') as f:
            print(f.readlines())


inter = Interpreter()
inter.read()