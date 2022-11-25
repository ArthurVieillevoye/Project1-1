import copy
from RuleStructure.Logic.Literal import *
from RuleStructure.Logic.Rule import *
from RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from RuleStructure.Argument import *
from RuleStructure.TableauNode import TableauNode
from RuleStructure.TableauRule import *

class Tableau:
    rootNode: TableauNode
    defeasibleRules: List[DefeasibleRule]
    isClosed: bool
    closureArguments: List[Argument]

    def __init__(self, arguments: List[Argument], defeasibleRules: List[DefeasibleRule]):
        self.defeasibleRules = defeasibleRules
        self.rootNode = TableauNode(arguments=arguments, defeasibleRules=defeasibleRules)
        self.isClosed = False
        self.closureArguments = []

    def addRootArgument(self, argument):
        self.rootNode.arguments.append(argument)

    def addDefeasibleRules(self, rule):
        self.defeasibleRules.append(rule)

    def evaluate(self):
        tableauChanged = False
        self.isClosed, self.closureArguments = self.rootNode.checkClosure()
        while not self.isClosed and not tableauChanged:
            tableauChanged = self.rootNode.expandTree()
            self.rootNode.checkDefeasibleRules()
            self.isClosed, self.closureArguments = self.rootNode.checkClosure()

                        


if __name__ == '__main__':
    p = Literal(stringRepresentation='p')
    q = Literal(stringRepresentation='q')
    r = Literal(stringRepresentation='r')
    s = Literal(stringRepresentation='s')

    sigma = [Rule(p, Operator.OR, q), Literal(stringRepresentation='¬q', negationOf=q)] #inital information
    D = [DefeasibleRule(p, r), DefeasibleRule(r, s)] #defeasible rules

    
    tableau = Tableau(arguments=[], defeasibleRules=D)

    for clause in sigma:
        tableau.addRootArgument(Argument(support=[clause], conclusion=clause))

    for defRule in D:
        tableau.addRootArgument(createTest(defRule.antecedent, TestReason.DEFEASIBLE_RULE))

    tableau.addRootArgument(createTest(s, TestReason.TARGET_CONCLUSION))

    tableau.evaluate()

    print('root arguments:')
    print([str(arg) for arg in tableau.rootNode.arguments])

    print('left node arguments:')
    print([str(arg) for arg in tableau.rootNode.left.arguments])

    print('right node arguments:')
    print([str(arg) for arg in tableau.rootNode.right.arguments])

    print('arguments for closure:')
    print([str(arg) for arg in tableau.rootNode.closureArguments])
                