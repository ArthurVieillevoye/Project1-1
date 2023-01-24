import copy
from .RuleStructure.Logic.Literal import *
from .RuleStructure import LawImplementation
from .RuleStructure import NixonLawExample2
from .RuleStructure import ContractSignedLawExample
from .RuleStructure.Logic.Rule import *
from .RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from .RuleStructure.Argument import *
from .RuleStructure.TableauNode import TableauNode
from .RuleStructure.TableauRule import *
from .Semantics import *
from .Tableau import *
from django.http import JsonResponse, HttpRequest
import json    

def decod_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


def setLiteralsValue(literals, usersLiteralValue):
    for l in literals:
        l.setValue(False)
        for x in usersLiteralValue:
            if l.literalId == x:
                l.setValue(True)


def main(request: HttpRequest()):

    if request.method =='POST':
       body = decod_body(request.body)


    if body["identifier"] == 'Facts':
        # print("facts")
        [literals, defeasibleRules, order, tests] = LawImplementation.getData()
        setLiteralsValue(literals, body["facts"])

    elif body["identifier"] == 'Example One':
        # print("contract")
        # Contract signed
        [literals, defeasibleRules, order, tests] = ContractSignedLawExample.getData()
        setLiteralsValue(literals, body["facts"])
    
    elif body["identifier"] == 'Example Two':
        # print("nixon")
        # Nixon example
        [literals, defeasibleRules, order, tests] = NixonLawExample2.getData()
        setLiteralsValue(literals, body["facts"])

    print(len(body["facts"]))

    
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

    ######################


    tableau.evaluate()

    # print('closed?', flush=True)
    # print(tableau.isClosed, flush=True)

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

    return JsonResponse({'allArgs': allArgs, # ["aaa", "bbb"]
                         'closure': closure, # ["aaa", "bbb"]
                         'groundedExtension': groundedExtension, # ["aaa", "bbb"]
                         'stableExtensions': stableExtensions, # [["aaa", "bbb"], ["ccc", "ddd"]]
                         'groundedExtensionFilter': groundedExtensionFilter, # ["aaa", "bbb"]
                         'stableExtensionsFilter': stableExtensionsFilter, # [["aaa", "bbb"], ["ccc", "ddd"]]
                         'groundedExtensionTrees': groundedExtensionTrees, # [treeJSON1, treeJSON2]
                         'undercuttingArgs': undercuttingArgs}) # ["aaa", "bbb"]
