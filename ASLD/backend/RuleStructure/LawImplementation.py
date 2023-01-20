from .Logic.Literal import Literal
from .Logic.Rule import *
from .ArgumentationRule import StrictRule, DefeasibleRule
import pandas as pd
import numpy as np
import os

def getData():
    # This class implements the law of the working hours act

    defeasibleRulesList = []

    ### Rules for initial situation ###
    #Rule 1
    l1 = Literal(stringRepresentation='Employed')
    l2 = Literal(stringRepresentation='Can make a request')
    defeasibleRulesList.append(DefeasibleRule(l1,l2, ruleId=1))

    # Rule 2
    # l1 = Literal(stringRepresentation='Employed')
    l3 = Literal(stringRepresentation='less than 10 employees')
    r1 = Rule(l1, Operator.AND, l3)
    l4 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r1,l4, ruleId=2))

    # Rule 3
    # l1 = Literal(stringRepresentation='Employed')
    l5 = Literal(stringRepresentation='Too old')
    r2 = Rule(l1, Operator.AND, l5)
    # l3 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r2,l4, ruleId=3))

    # Rule 4
    # l1 = Literal(stringRepresentation='Employed')
    l6 = Literal(stringRepresentation='Military official')
    r3 = Rule(l1, Operator.AND, l6)
    # l3 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r3,l4, ruleId=4))

    # Rule 5
    # l1 = Literal(stringRepresentation='Employed')
    l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
    r4 = Rule(l1, Operator.AND, l7)
    # l3 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r4,l4, ruleId=5))


    #################################################################################
    ### Rules for first legal action: Request by Employee Change in Working hours ###
    # Rule 6
    # l2 = Literal(stringRepresentation='Can make a request')
    l8 = Literal(stringRepresentation='request is about a change in the working hours')
    r5 = Rule(l2, Operator.AND, l8)
    l9 = Literal(stringRepresentation='Legal request for a change in working hours')
    defeasibleRulesList.append(DefeasibleRule(r5,l9, ruleId=6))

    # Rule 7
    l10 = Literal(stringRepresentation='Request not submitted in writing')
    r6 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l10)
    l11 = Literal(stringRepresentation='Not Legal request for a change in working hours')
    defeasibleRulesList.append(DefeasibleRule(r6, l11, ruleId=7))

    # Rule 8
    l12 = Literal(stringRepresentation='time since last request over a year')
    r7 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l12)
    defeasibleRulesList.append(DefeasibleRule(r7, l11, ruleId=8))

    # Rule 9
    l13 = Literal(stringRepresentation='Did not work for at least 26 weeks')
    r8 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l13)
    defeasibleRulesList.append(DefeasibleRule(r8, l11, ruleId=9))

    # Rule 10
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances') OR ANOTHER ONE ????
    r9 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r9, l9, ruleId=10))

    
    ##########################################################################
    # Rules for first legal action: Request by Employee Change in Working time
    # Rule 11
    l14 = Literal(stringRepresentation='request is about a change in the working time')
    r10 = Rule(l2, Operator.AND, l14)
    l15 = Literal(stringRepresentation='Legal request for a change in working time')
    defeasibleRulesList.append(DefeasibleRule(r10,l15, ruleId=11))

    # Rule 12
    r11 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l10)
    l16 = Literal(stringRepresentation='Not a legal request for a change in working time')
    defeasibleRulesList.append(DefeasibleRule(r11, l16, ruleId=12))

    # Rule 13
    r12 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l12)
    defeasibleRulesList.append(DefeasibleRule(r12, l16, ruleId=13))

    # Rule 14
    r13 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l13)
    defeasibleRulesList.append(DefeasibleRule(r13, l16, ruleId=14))

    # Rule 15
    r14 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r14, l15, ruleId=15))

    ###########################################################################
    # Rules for first legal action: Request by Employee Change in Working place
    # Rule 16
    l17 = Literal(stringRepresentation='request is about a change in the working place')
    r15 = Rule(l2, Operator.AND, l17)
    l18 = Literal(stringRepresentation='Legal request for a change in working place')
    defeasibleRulesList.append(DefeasibleRule(r15, l18, ruleId=16))

    # Rule 17
    r16 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l10)
    l19 = Literal(stringRepresentation='Not Legal request for a change in working place')
    defeasibleRulesList.append(DefeasibleRule(r16, l19, ruleId=17))

    # Rule 18
    r17 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l12)
    defeasibleRulesList.append(DefeasibleRule(r17, l19, ruleId=18))

    # Rule 19
    r18 = Rule (Rule(l2, Operator.AND, l17), Operator.AND, l13)
    defeasibleRulesList.append(DefeasibleRule(r18, l19, ruleId=19))

    # Rule 20
    r19 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r19, l18, ruleId=20))


    ################################################################################
    # Rules resulting from legal action: Request by Employee Change in Working hours
    # Rule 21
    l20 = Literal(stringRepresentation='DUTY Consult Employee About Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(l8, l20, ruleId=21))

    #Rule 22
    l21 = Literal(stringRepresentation='DUTY Accept Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(l8, l21, ruleId=22))

    # Rule 23
    l22 = Literal(stringRepresentation='No power to Reject Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(l8, l22, ruleId=23))

    # Rule 24
    l23 = Literal(stringRepresentation='IMMUNITY Substantial Business Or Service Interests')
    r20 = Rule(l8, l23)
    l24 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(l8, l24, ruleId=24))

    # Rule 25
    l25 = Literal(stringRepresentation='power to Reject Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(r20, l25, ruleId=25))


    ###############################################################################
    # Rules resulting from legal action: Request by Employee Change in Working time
    # Rule 26 
    l26 = Literal(stringRepresentation='DUTY to Consult Employee About Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(l15, l26, ruleId=26))

    # Rule 27
    l27 = Literal(stringRepresentation='DUTY to Accept Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(l15, l27, ruleId=27))

    #Rule 28
    l28 = Literal(stringRepresentation='No POWER to Change Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(l15, l28, ruleId=28))

    # Rule 29
    l29 = Literal(stringRepresentation='IMMUNITY Interests Of Employee Yield For Reasons Of Reasonableness And Fairness')
    r21 = Rule(l15, Operator.AND, l29)
    l30 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r21, l30, ruleId=29))

    # Rule 30
    l31 = Literal(stringRepresentation='POWER to Change Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r21, l31, ruleId=30))

    ################################################################################
    # Rules resulting from legal action: Request by Employee Change in Working place
    # Rule 31
    l32 = Literal(stringRepresentation='DUTY to Contemplate Request Change Working Place')
    defeasibleRulesList.append(DefeasibleRule(l18, l32, ruleId=31))

    ##############################################################
    # Rules for legal action: Decision made on request by Employer
    # Rule 32
    l33 = Literal(stringRepresentation='DOES Accept Request Change Working Hours')
    r22 = Rule(l21, Operator.AND, l33)
    l34 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(r22, l34, ruleId=32))

    # Rule 33
    l35 = Literal(stringRepresentation='Decision On Request Not Sent In Writing')
    r23 = Rule(Rule(l21, Operator.AND, l33), Operator.AND, l35)
    l36 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(r23, l36, ruleId=33))

    # Rule 34
    l37 = Literal(stringRepresentation='DOES Reject Request Change Working Hours')
    r24 = Rule(l25, Operator.AND, l37)
    l38 = Literal(stringRepresentation='LEGAL Rejected Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(r24, l38, ruleId=34))

    # Rule 35
    r25 = Rule(Rule(l25, Operator.AND, l37), Operator.AND, l35)
    l39 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Hours')
    defeasibleRulesList.append(DefeasibleRule(r25, l39, ruleId=35))

    # Rule 36
    l40 = Literal(stringRepresentation='DOES Accept Request Change Working Times')
    r26 = Rule(l27, Operator.AND, l40)
    l41 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r26, l41, ruleId=36))

    # Rule 37
    r27 = Rule(Rule(l27, Operator.AND, l40), Operator.AND, l35)
    l42 = Literal(stringRepresentation='NOT LEGAL Accepted Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r27, l42, ruleId=37))

    # Rule 38
    l43 = Literal(stringRepresentation='DOES Change Request Change Working Times')
    r28 = Rule(l31, Operator.AND, l43)
    l44 = Literal(stringRepresentation='LEGAL Changed Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r28, l44, ruleId=38))

    # Rule 39
    r29 = Rule(Rule(l31, Operator.AND, l43), Operator.AND, l35)
    l45 = Literal(stringRepresentation='NOT a LEGAL Changed Request Change Working Times')
    defeasibleRulesList.append(DefeasibleRule(r29, l45, ruleId=39))

    # Rules 40
    l46 = Literal(stringRepresentation='DOES Accept Request Change Working Place')
    r30 = Rule(l32, Operator.AND, l46)
    l47 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Place')
    defeasibleRulesList.append(DefeasibleRule(r30, l47, ruleId=40))

    # Rule 41
    r31 = Rule(Rule(l32, Operator.AND, l46), Operator.AND, l35)
    l48 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Place')
    defeasibleRulesList.append(DefeasibleRule(r31, l48, ruleId=41))

    # Rule 42
    l49 = Literal(stringRepresentation='DOES Reject Request Change Working Place')
    r32 = Rule(l32, Operator.AND, l49)
    l50 = Literal(stringRepresentation='LEGAL Rejected Request Change Working Place')
    defeasibleRulesList.append(DefeasibleRule(r32, l50, ruleId=42))

    # Rule 43 
    r33 = Rule(Rule(l32, Operator.AND, l49), Operator.AND, l35)
    l51 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Place')
    defeasibleRulesList.append(DefeasibleRule(r33, l51, ruleId=43))


    ################################################################
    # Rules for legal action: Employee too late with making decision
    # Rule 44
    l52 = Literal(stringRepresentation='Time Before Commencement Date Request Less Than One Month')
    r34 = Rule(l52, Operator.AND, l9)
    defeasibleRulesList.append(DefeasibleRule(r34, l34, ruleId=44))

    # Rule 45
    r34 = Rule(Rule(l25, Operator.AND, l52), Operator.AND, l38)
    defeasibleRulesList.append(DefeasibleRule(r34, l36, ruleId=45))

    # Rule 46
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
    l53 = Literal(stringRepresentation='Time Before Commencement Date Request Less Than Five Days')
    r35 = Rule(Rule(l9, Operator.AND, l7), Operator.AND, l53)
    defeasibleRulesList.append(DefeasibleRule(r35, l34, ruleId=46))

    # Rule 47
    r36 = Rule(Rule(Rule(l9, Operator.AND, l7), Operator.AND, l53), Operator.AND, l38)
    defeasibleRulesList.append(DefeasibleRule(r36, l36, ruleId=47))

    # Rule 48
    r37 = Rule(l15, Operator.AND, l52)
    defeasibleRulesList.append(DefeasibleRule(r37, l41, ruleId=48))

    # Rule 49
    r38 = Rule(Rule(l15, Operator.AND, l52), Operator.AND, l44)
    defeasibleRulesList.append(DefeasibleRule(r38, l42, ruleId=49))

    # Rule 50
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
    r39 = Rule(Rule(l15, Operator.AND, l7), Operator.AND, l53)
    defeasibleRulesList.append(DefeasibleRule(r39, l41, ruleId=50))

    # Rule 51
    r40 = Rule(Rule(Rule(l15, Operator.AND, l7), Operator.AND, l53), Operator.AND, l44)
    defeasibleRulesList.append(DefeasibleRule(r40, l42, ruleId=51))

    # Rule 52
    r41 = Rule(l18, Operator.AND, l52)
    defeasibleRulesList.append(DefeasibleRule(r41, l47, ruleId=52))

    # Rule 53 
    r42 = Rule(Rule(l18, Operator.AND, l52), Operator.AND, l50)
    defeasibleRulesList.append(DefeasibleRule(r42, l48, ruleId=53))

    # Rule 54
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
    r43 = Rule(Rule(l18, Operator.AND, l7), Operator.AND, l53)
    defeasibleRulesList.append(DefeasibleRule(r43, l47, ruleId=54))

    # Rule 55
    r44 = Rule(Rule(Rule(l18, Operator.AND, l7), Operator.AND, l53), Operator.AND, l50)
    defeasibleRulesList.append(DefeasibleRule(r44, l48, ruleId=55))

    literalsList = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26,
                    l27,l28,l29,l30,l31,l32,l33,l34,l35,l36,l37,l38,l39,l40,l41,l42,l43,l44,l45,l46,l47,l48,l49,l50,
                    l51,l52,l53]

    for i in range(len(literalsList)):
        literalsList[i].setID(i+1)

    # 0 = No relation
    # 1 = Row stronger than column
    # 2 = column stronger than row
    df = pd.read_csv(
            os.path.realpath(os.path.dirname(__file__))  + '/OrderLawWorkingHours.csv',
            header=None,
            delimiter=';'
        )
    order = df.values

    return [literalsList, defeasibleRulesList, order]