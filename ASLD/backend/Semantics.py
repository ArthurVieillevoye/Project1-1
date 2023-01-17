import copy
from .RuleStructure.Logic.Literal import *
from .RuleStructure.Logic.Rule import *
from .RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from .RuleStructure.Argument import *
from .RuleStructure.TableauNode import TableauNode
from .RuleStructure.TableauRule import *
# tableau class

class label(Enum):
    # This class describes the labels for the labeling approach to find extensions
    IN = 0
    OUT = 1
    UNDEC = 2

def getGroundedExtension(arguments):
    labels = {}
    for arg in arguments:
        if len(arg.attackedBy) == 0:
            labels[arg] = label.IN
        else:
            labels[arg] = label.UNDEC

    print(labels)
