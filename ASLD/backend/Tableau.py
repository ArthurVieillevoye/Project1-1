import copy
from .RuleStructure.Logic.Literal import *
from .RuleStructure.Logic.Rule import *
from .RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from .RuleStructure.Argument import *
from .RuleStructure.TableauNode import TableauNode
from .RuleStructure.TableauRule import *
from .Semantics import *

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