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

    def addDefeasibleRules(self, rule):
        self.defeasibleRules.append(rule)

    def getLastArgs(self, arguments):
        lastArgs = []
        for arg1 in arguments:
            if not (len(arg1.support) == 1 and arg1.support[0] == arg1.conclusion) \
                and not (type(arg1.conclusion) == DefeasibleRule):
                isUsed = False
                for arg2 in arguments:
                    if arg2.isArgumentInArgument(arg1):
                        isUsed = True
                        break
                if not isUsed:
                    lastArgs.append(arg1)
                    
        return lastArgs

    def getUndercuttingArgs(self, arguments):
        undercuttingArgs = []
        for arg in arguments:
            if type(arg.conclusion) == DefeasibleRule and arg.conclusion.isNegation:
                undercuttingArgs.append(arg)
                    
        return undercuttingArgs

    def getArgumentsString(self, arguments):
        strArgs = list(set(arguments))
        strArgs.sort(key=lambda x: (x.depth, len(x.support)))
        strArgs = [str(arg) for arg in strArgs]
                    
        return strArgs



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