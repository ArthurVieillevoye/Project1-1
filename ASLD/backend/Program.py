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
        print("facts")
        [literals, defeasibleRules, order] = LawImplementation.getData()
        setLiteralsValue(literals, body["facts"])

    elif body["identifier"] == 'Example One':
        print("contract")
        # Contract signed
        [literals, defeasibleRules, order] = ContractSignedLawExample.getData()
        setLiteralsValue(literals, body["facts"])
    
    elif body["identifier"] == 'Example Two':
        print("nixon")
        # Nixon example
        [literals, defeasibleRules, order] = NixonLawExample2.getData()
        setLiteralsValue(literals, body["facts"])
    
    # for l in literals:
    #     if l.interpret():
    #         print("helooooooo")
    #         print(l.literalId, " , ", l)

    print(body["facts"], flush=True)

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

    # # print('root arguments:')
    # args = [str(arg) for arg in tableau.rootNode.arguments]
    # # print(args)

    # # print('closed?')
    # # print(tableau.isClosed)

    # # print('arguments for closure:')
    # # print([str(arg) for arg in tableau.rootNode.closureArguments])

    # # print('arguments for closure reduced:')
    # closure = list(dict.fromkeys([str(arg)
    #                for arg in tableau.rootNode.closureArguments]))
    # # print(closure)

    # return JsonResponse({'closure': closure})

    ##################

    # a = Literal(stringRepresentation='Person signs a contract')
    # b = Literal(stringRepresentation='Person is under the age of 14')
    # c = Literal(stringRepresentation='Guardian approved the contract')
    # d = Literal(stringRepresentation='Person is bound by the contract')

    # d1 = DefeasibleRule(a, d, ruleId = 1)
    # d2 = DefeasibleRule(antecedent = Rule(a, Operator.AND, b), consequence = createNegation(d), ruleId = 2)
    # d3 = DefeasibleRule(antecedent = Rule(Rule(a, Operator.AND, b), Operator.AND, c), consequence = d, ruleId = 3)

    # sigma = [a, b, c] #inital information
    # D = [d1, d2, d3] #defeasible rules
        
    # order = [[0,2,2],[1,0,2],[1,1,0]]
    
    # tableau = Tableau(arguments=[], defeasibleRules=D, order=order)

    # for clause in sigma:
    #     tableau.addRootArgument(Argument(support=[clause], conclusion=clause))

    # tableau.addRootArgument(createTest(createNegation(d)))
    # tableau.addRootArgument(createTest(d))

    #####################

    # tmp = request.POST["facts"]
    # print("#########################################################", type(tmp))

    # a = Literal(stringRepresentation='Person is Quaker')
    # b = Literal(stringRepresentation='Person is Republican')
    c = Literal(stringRepresentation='Person is Pacifist')

    # d1 = DefeasibleRule(a, c, ruleId = 1)
    # d2 = DefeasibleRule(b, createNegation(c), ruleId = 2)

    # sigma = [a, b] #inital information
    # D = [d1, d2] #defeasible rules
        
    # order = [[0,0],[0,0]]
    
    tableau = Tableau(arguments=[], defeasibleRules=defeasibleRules, order=order)

    for clause in literals:
        if clause.interpret():
            tableau.addRootArgument(Argument(support=[clause], conclusion=clause))
        else:
            c2 = createNegation(clause)
            tableau.addRootArgument(Argument(support=[c2], conclusion=c2))


    tableau.addRootArgument(createTest(createNegation(c)))
    tableau.addRootArgument(createTest(c))

    ######################


    tableau.evaluate()

    print('closed?', flush=True)
    print(tableau.isClosed, flush=True)

    
    # closure = list(set(tableau.closureArguments))
    # closure.sort(key=lambda x: (x.depth, len(x.support)))
    # closure = [str(arg) for arg in closure]

    closure = tableau.getArgumentsString(tableau.closureArguments)

    # allArgs = list(set(tableau.allArguments))
    # allArgs.sort(key=lambda x: (x.depth, len(x.support)))
    # allArgs = [str(arg) for arg in allArgs]

    allArgs = tableau.getArgumentsString(tableau.allArguments)

    # lastArgs = list(set(tableau.getLastArgs(tableau.allArguments)))
    # lastArgs.sort(key=lambda x: (x.depth, len(x.support)))
    # lastArgs = [str(arg) for arg in allArgs]

    lastArgs = tableau.getArgumentsString(tableau.getLastArgs(tableau.allArguments))

    groundedExtension, stableExtensions = getExtensions(tableau.allArguments)
    undercuttingArgs = tableau.getUndercuttingArgs(groundedExtension)

    groundedExtensionFilter = tableau.getLastArgs(groundedExtension)
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
                         'undercuttingArgs': undercuttingArgs}) # ["aaa", "bbb"]
