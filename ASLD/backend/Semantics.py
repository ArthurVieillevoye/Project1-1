import copy
from .RuleStructure.Logic.Literal import *
from .RuleStructure.Logic.Rule import *
from .RuleStructure.ArgumentationRule import StrictRule, DefeasibleRule
from .RuleStructure.Argument import *
from .RuleStructure.TableauNode import TableauNode
from .RuleStructure.TableauRule import *
# tableau class

class Label(Enum):
    # This class describes the labels for the labeling approach to find extensions
    IN = 0
    OUT = 1
    UNDEC = 2

def getExtension(arguments):
    labels = {}
    for arg in arguments:
        if len(arg.attackedBy) == 0:
            labels[arg] = Label.IN
        else:
            labels[arg] = Label.UNDEC

    labelsChanged = True

    while labelsChanged:
        labelsChanged = False

        for arg in labels:
            if labels[arg] == Label.IN:
                for attacked in arg.attacks:
                    if labels[attacked] == Label.IN:
                        a = 1/0
                    elif labels[attacked] == Label.UNDEC:
                        labels[attacked] = Label.OUT
                        labelsChanged = True
            elif labels[arg] == Label.UNDEC:
                isIn = True
                for attacker in arg.attackedBy:
                    if labels[attacker] != Label.OUT:
                        isIn = False
                        break
                
                if isIn:
                    labels[arg] = Label.IN
                    labelsChanged = True

    for arg in sorted(labels, key = lambda x: (x.depth, len(x.support))):
        print(arg, labels[arg])

    extension = []
    isStable = True
    isGrounded = True

    for arg, label in labels.items():
        if label == Label.IN:
            extension.append(arg)
        elif label == Label.UNDEC:
            isStable = False
            isGrounded = False

    if isGrounded:
        groundedExtension = extension
        stableExtensions = [extension]
        return groundedExtension, stableExtensions
    else:
        groundedExtension = None
        stableExtensions = [extension]

