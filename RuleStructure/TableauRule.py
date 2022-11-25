from enum import Enum
from RuleStructure.Logic.Literal import Literal
from typing import List, Union
from RuleStructure.Logic.Rule import *
from RuleStructure.Argument import *

def applyTableauRule(argument):
    if type(argument.conclusion) == Rule:
        if argument.conclusion.operator == Operator.AND:
            return [Argument(support=argument.support, conclusion=argument.conclusion.head) \
                   ,Argument(support=argument.support, conclusion=argument.conclusion.body)] \
                   ,None

        if argument.conclusion.operator == Operator.OR:
            return [Argument(support=argument.support, conclusion=argument.conclusion.head)] \
                  ,[Argument(support=argument.support, conclusion=argument.conclusion.body)]

    return None, None