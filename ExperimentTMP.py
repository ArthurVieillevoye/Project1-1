import copy
from ASLD.backend.RuleStructure.Logic.Literal import *
from ASLD.backend.RuleStructure import LawImplementation
from ASLD.backend.RuleStructure import NixonLawExample2
from ASLD.backend.RuleStructure import ContractSignedLawExample
from ASLD.backend.RuleStructure.Logic.Rule import *
from ASLD.backend.RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from ASLD.backend.RuleStructure.Argument import *
from ASLD.backend.RuleStructure.TableauNode import TableauNode
from ASLD.backend.RuleStructure.TableauRule import *
from ASLD.backend.Semantics import *
from ASLD.backend.Tableau import *
import json    
from itertools import combinations
import numpy as np

def decod_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


def setLiteralsValue(literals, usersLiteralValue):
    for l in literals:
        l.setValue(False)
        for x in usersLiteralValue:
            if l.literalId == x:
                l.setValue(True)

def getListOfTrue():
    lst =  [14, 17]
    lst = literalsListQuestions = [1,3,5,6,7,8,10,12,13,14,17,33,35,37,40,43,46,49,52,53]

    results = []
    total = 0
    for i in range(len(lst)+1):
        counter = 0
        print(i)
        for combo in combinations(lst, i):
            [literals, defeasibleRules, order, tests] = LawImplementation.getData()
            setLiteralsValue(literals, lst)
            order1 = np.zeros(order.shape)
            if len(runProgramm(literals, order1, defeasibleRules, tests)):
                counter += 1
                total += 1

        results.append(counter)

    return results



def runProgramm(literals, order, defeasibleRules, tests):

    tableau = Tableau(arguments=[], defeasibleRules=defeasibleRules, order=order)

    for clause in literals:
        if clause.interpret():
            tableau.addRootArgument(Argument(support=[clause], conclusion=clause))
        else:
            c2 = createNegation(clause)
            tableau.addRootArgument(Argument(support=[c2], conclusion=c2))


    for test in tests:
        tableau.addRootArgument(createTest(createNegation(test)))
        tableau.addRootArgument(createTest(test))

    #####################
    tableau.evaluate()

    closure = tableau.getArgumentsString(tableau.closureArguments)

    allArgs = tableau.getArgumentsString(tableau.allArguments)

    lastArgs = tableau.getArgumentsString(tableau.getLastArgs(tableau.allArguments))

    groundedExtension, stableExtensions = getExtensions(tableau.allArguments)
    undercuttingArgs = tableau.getUndercuttingArgs(groundedExtension)

    groundedExtensionFilter = tableau.getLastArgs(groundedExtension)
    groundedExtensionTrees = tableau.getTrees(groundedExtensionFilter)
    stableExtensionsFilter = [tableau.getLastArgs(extension) for extension in stableExtensions]

    groundedExtension = tableau.getArgumentsString(groundedExtension)
    groundedExtensionFilter = tableau.getArgumentsString(groundedExtensionFilter)
    undercuttingArgs = tableau.getArgumentsString(undercuttingArgs)

    stableExtensions = [tableau.getArgumentsString(extension) for extension in stableExtensions]
    stableExtensionsFilter = [tableau.getArgumentsString(extension) for extension in stableExtensionsFilter]

    return groundedExtension


print(getListOfTrue())