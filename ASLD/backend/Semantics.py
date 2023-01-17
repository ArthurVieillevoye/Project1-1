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

def doLabeling(labels):
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

    return labels

def getStableExtensions(labels):
    labels1 = labels.copy()
    labels2 = labels.copy()

    for arg in labels:
        if labels[arg] == Label.UNDEC:
            labels1[arg] = Label.IN
            labels2[arg] = Label.OUT
            break

    labels1 = doLabeling(labels1)
    labels2 = doLabeling(labels2)
    stableExtensions = []

    extension = []
    isStable = True

    for arg, label in labels1.items():
        if label == Label.IN:
            extension.append(arg)
        elif label == Label.UNDEC:
            isStable = False

    if isStable:
        stableExtensions.append(extension)
    
    extension = []
    isStable = True

    for arg, label in labels2.items():
        if label == Label.IN:
            extension.append(arg)
        elif label == Label.UNDEC:
            isStable = False

    if isStable:
        stableExtensions.append(extension)

    return stableExtensions

def getExtensions(arguments):
    labels = {}
    for arg in arguments:
        if len(arg.attackedBy) == 0:
            labels[arg] = Label.IN
        else:
            labels[arg] = Label.UNDEC

    labels = doLabeling(labels)

    for arg in sorted(labels, key = lambda x: (x.depth, len(x.support))):
        print(arg, labels[arg])

    extension = []
    isGrounded = True

    for arg, label in labels.items():
        if label == Label.IN:
            extension.append(arg)
        elif label == Label.UNDEC:
            isGrounded = False

    if isGrounded:
        groundedExtension = extension
        groundedExtension.sort(key = lambda x: (x.depth, len(x.support)))
        groundedExtension = [str(arg) for arg in groundedExtension]

        stableExtensions = [extension]
    else:
        groundedExtension = []
        stableExtensions = getStableExtensions(labels)
    
    stableExtensions.sort(key = lambda x: len(x))
    for i in range(len(stableExtensions)):
        stableExtensions[i].sort(key = lambda x: (x.depth, len(x.support)))
        stableExtensions[i] = [str(arg) for arg in stableExtensions[i]]

    return groundedExtension, stableExtensions

