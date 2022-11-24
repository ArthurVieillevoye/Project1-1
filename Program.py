import copy
from RuleStructure.Logic.Literal import *
from RuleStructure.Logic.Rule import *
from RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from RuleStructure.Argument import *
from RuleStructure.TableauNode import TableauNode
from RuleStructure.TableauRule import *

class Tableau:
    rootNode: TableauNode
    defeasbileRules: List[DefeasibleRule]
    isClosed: bool = False
    closureArguments: List[Argument]

    def __init__(self, arguments: List[Argument], defeasbileRules: List[DefeasibleRule]):
        self.defeasbileRules = defeasbileRules=defeasbileRules
        self.rootNode = TableauNode(arguments=arguments)

    def addRootArgument(self, argument):
        self.rootNode.arguments.append(argument)

    def addDefeasibleRules(self, rule):
        self.defeasbileRules.append(rule)

    def evaluate(self):
        self.isClosed, self.closureArguments = self.rootNode.checkClosure()
        self.rootNode.expandTree()
        self.isClosed, self.closureArguments = self.rootNode.checkClosure()

                        


if __name__ == '__main__':
    p = Literal(stringRepresentation='p')
    q = Literal(stringRepresentation='q')
    r = Literal(stringRepresentation='r')
    s = Literal(stringRepresentation='s')

    sigma = [Rule(p, Operator.OR, q), Literal(stringRepresentation='¬q', negationOf=q)] #inital information
    D = [DefeasibleRule(p, r), DefeasibleRule(r, s)] #defeasible rules

    
    tableau = Tableau([], D)

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
                

