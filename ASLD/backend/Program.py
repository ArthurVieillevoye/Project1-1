import copy
from .RuleStructure.Logic.Literal import *
from .RuleStructure.Logic.Rule import *
from .RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from .RuleStructure.Argument import *
from .RuleStructure.TableauNode import TableauNode
from .RuleStructure.TableauRule import *
from django.http import JsonResponse
# tableau class


class Tableau:
    rootNode: TableauNode
    defeasibleRules: List[DefeasibleRule]
    isClosed: bool
    closureArguments: List[Argument]
    allArguments: List[Argument]
    order: List

    def __init__(self, arguments: List[Argument], defeasibleRules: List[DefeasibleRule], order):
        self.defeasibleRules = defeasibleRules
        self.rootNode = TableauNode(
            arguments=arguments, defeasibleRules=defeasibleRules, order=order)
        self.isClosed = False
        self.closureArguments = []
        self.order = order

    def addRootArgument(self, argument):
        self.rootNode.addArgument(argument)

    def addDefeasibleRules(self, rule):
        self.defeasibleRules.append(rule)

    def evaluate(self):
        tableauChanged = True
        # check if tableau is already closed (contradiction) with initial information
        #self.isClosed, self.closureArguments = self.rootNode.checkClosure()

        # apply tableau rules and evaluate defeasible rules until either the tableau is closed, or no more changes are possible
        while tableauChanged:
            tableauChanged = False
            # apply tableau rule to create left (and right) child nodes
            tableauChanged = self.rootNode.expandTree()
            # evaluate defeasible rules
            tableauChanged = self.rootNode.checkDefeasibleRules() or tableauChanged
            # check for contradictions and create undercutting arguments
            tableauChanged = self.rootNode.checkContradiction() or tableauChanged
            # check if tableau changed
            self.isClosed, self.closureArguments = self.rootNode.checkClosure()

        self.allArguments = self.rootNode.getAllArguments()        


def main(request):
    # p = Literal(stringRepresentation='p')
    # q = Literal(stringRepresentation='q')
    # r = Literal(stringRepresentation='r')
    # s = Literal(stringRepresentation='s')

    # #sigma = [Rule(createNegation(clause=createNegation(clause=p)), Operator.OR, q), createNegation(clause=q)] #inital information
    # sigma = [Rule(p, Operator.OR, q), createNegation(clause=q)] #inital information
    # D = [DefeasibleRule(p, r), DefeasibleRule(r, s)] #defeasible rules

    # tableau = Tableau(arguments=[], defeasibleRules=D)

    # for clause in sigma:
    #     tableau.addRootArgument(Argument(support=[clause], conclusion=clause))

    # #for defRule in D:
    # #    tableau.addRootArgument(createTest(defRule.antecedent, TestReason.DEFEASIBLE_RULE))

    # tableau.addRootArgument(createTest(s))

    # tableau.evaluate()

    # print('root arguments:')
    # print([str(arg) for arg in tableau.rootNode.arguments])

    # print('left node arguments:')
    # print([str(arg) for arg in tableau.rootNode.left.arguments])

    # print('right node arguments:')
    # print([str(arg) for arg in tableau.rootNode.right.arguments])

    # print('closed?')
    # print(tableau.isClosed)

    # print('arguments for closure:')
    # print([str(arg) for arg in tableau.rootNode.closureArguments])

    # print('arguments for closure reduced:')
    # print(list(dict.fromkeys([str(arg) for arg in tableau.rootNode.closureArguments])))

    # a = Literal(stringRepresentation='Person signs a contract')
    # b = Literal(stringRepresentation='Person is under the age of 14')
    # c = Literal(stringRepresentation='Guardian approved the contract')
    # d = Literal(stringRepresentation='Person is bound by the contract')

    # d1 = DefeasibleRule(a, d)
    # d2 = DefeasibleRule(b, createNegation(d1))
    # d3 = DefeasibleRule(c, createNegation(d2))

    # sigma = [a, b, c]  # inital information
    # D = [d1, d2, d3]  # defeasible rules

    # tableau = Tableau(arguments=[], defeasibleRules=D)

    # for clause in sigma:
    #     tableau.addRootArgument(Argument(support=[clause], conclusion=clause))

    # tableau.addRootArgument(createTest(d))

    # tableau.evaluate()

    # print('root arguments:')
    # args = [str(arg) for arg in tableau.rootNode.arguments]
    # print(args)

    # print('closed?')
    # print(tableau.isClosed)

    # print('arguments for closure:')
    # print([str(arg) for arg in tableau.rootNode.closureArguments])

    # print('arguments for closure reduced:')
    # closure = list(dict.fromkeys([str(arg)
    #                for arg in tableau.rootNode.closureArguments]))
    # print(closure)

    a = Literal(stringRepresentation='Person signs a contract')
    b = Literal(stringRepresentation='Person is under the age of 14')
    c = Literal(stringRepresentation='Guardian approved the contract')
    d = Literal(stringRepresentation='Person is bound by the contract')

    d1 = DefeasibleRule(a, d, ruleId = 1)
    d2 = DefeasibleRule(antecedent = Rule(a, Operator.AND, b), consequence = createNegation(d), ruleId = 2)
    d3 = DefeasibleRule(antecedent = Rule(Rule(a, Operator.AND, b), Operator.AND, c), consequence = d, ruleId = 3)

    sigma = [a, b, c] #inital information
    D = [d1, d2, d3] #defeasible rules
        
    order = [[0,2,2],[1,0,2],[1,1,0]]
    
    tableau = Tableau(arguments=[], defeasibleRules=D, order=order)

    for clause in sigma:
        tableau.addRootArgument(Argument(support=[clause], conclusion=clause))

    tableau.addRootArgument(createTest(createNegation(d)))
    tableau.addRootArgument(createTest(d))

    tableau.evaluate()

    print('root arguments:', flush=True)
    print([str(arg) for arg in tableau.rootNode.arguments], flush=True)

    print('closed?', flush=True)
    print(tableau.isClosed, flush=True)

    #print('arguments for closure:')
    #print([str(arg) for arg in tableau.rootNode.closureArguments])

    #print('arguments for closure reduced:')
    #print(list(dict.fromkeys([str(arg) for arg in tableau.rootNode.closureArguments])))

    closure = list(set([str(arg) for arg in tableau.rootNode.closureArguments]))

    allArgs = list(set([str(arg) for arg in tableau.allArguments]))

    return JsonResponse({'closure': allArgs + closure})

    print('arguments for closure reduced:')
    print(list(dict.fromkeys([str(arg) for arg in tableau.rootNode.closureArguments])))