from enum import Enum
from RuleStructure.Logic.Literal import Literal
from typing import List, Union
from RuleStructure.Logic.Rule import *
from RuleStructure.Argument import *

def createNegation(clause):
    if type(clause) == Literal:
        return Literal(negationOf=clause)
    elif type(clause) == Rule:
        return Rule(negationOf=clause)

def applyTableauRule(argument):
    if argument.conclusion.isNegation:
        if argument.conclusion.negationOf.isNegation:
            return [Argument(support=argument.support, conclusion=argument.conclusion.negationOf.negationOf)] \
                   ,None
        elif argument.conclusion.negationOf.operator == Operator.OR:
            return [Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.negationOf.head)) \
                    ,Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.negationOf.body))] \
                    ,None
        elif argument.conclusion.negationOf.operator == Operator.AND:
            return [Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.negationOf.head))] \
                  ,[Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.negationOf.body))]   
        
        elif argument.conclusion.negationOf.operator == Operator.IF:
            return [Argument(support=argument.support, conclusion=argument.conclusion.negationOf.head) \
                   ,Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.negationOf.body))] \
                   ,None
        elif argument.conclusion.negationOf.operator == Operator.IFF:
            return [Argument(support=argument.support, conclusion=createNegation(clause=Rule(head=argument.conclusion.negationOf.head, operator=Operator.IF, body=argument.conclusion.negationOf.body)))] \
                  ,[Argument(support=argument.support, conclusion=createNegation(clause=Rule(head=argument.conclusion.negationOf.body, operator=Operator.IF, body=argument.conclusion.negationOf.head)))]
    else:
        if argument.conclusion.operator == Operator.AND:
            return [Argument(support=argument.support, conclusion=argument.conclusion.head) \
                   ,Argument(support=argument.support, conclusion=argument.conclusion.body)] \
                   ,None

        elif argument.conclusion.operator == Operator.OR:
            return [Argument(support=argument.support, conclusion=argument.conclusion.head)] \
                  ,[Argument(support=argument.support, conclusion=argument.conclusion.body)]

        elif argument.conclusion.operator == Operator.IF:
            return [Argument(support=argument.support, conclusion=createNegation(clause=argument.conclusion.head))] \
                  ,[Argument(support=argument.support, conclusion=argument.conclusion.body)]

        elif argument.conclusion.operator == Operator.IFF:
            return [Argument(support=argument.support, conclusion=Rule(head=argument.conclusion.head, operator=Operator.IF, body=argument.conclusion.body)) \
                   ,Argument(support=argument.support, conclusion=Rule(head=argument.conclusion.body, operator=Operator.IF, body=argument.conclusion.head))] \
                   ,None

    return None, None