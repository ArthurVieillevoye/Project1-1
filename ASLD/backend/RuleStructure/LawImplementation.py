from .TableauRule import createNegation
from .Logic.Literal import Literal
from .Logic.Rule import *
from .ArgumentationRule import *
import pandas as pd
import os

def getData():
    # This class implements the law of the working hours act

    defeasibleRulesList = []

    ### Rules for initial situation ###
    #Rule 1
    l1 = Literal(stringRepresentation='Requestor is employed at company')
    l2 = Literal(stringRepresentation='Requestor can make a request')
    defeasibleRulesList.append(DefeasibleRule(l1,l2, ruleId=1))

    # Rule 2
    # l1 = Literal(stringRepresentation='Employed')
    l3 = Literal(stringRepresentation='Company has less than 10 employees')
    r1 = Rule(l1, Operator.AND, l3)
    #l4 = Literal(stringRepresentation='Cannot make a request')
    l4 = createNegation(l2)
    defeasibleRulesList.append(DefeasibleRule(r1,l4, ruleId=2))

    # Rule 3
    # l1 = Literal(stringRepresentation='Employed')
    l5 = Literal(stringRepresentation='Requestor reached retirement age')
    r2 = Rule(l1, Operator.AND, l5)
    defeasibleRulesList.append(DefeasibleRule(r2,l4, ruleId=3))

    # Rule 4
    # l1 = Literal(stringRepresentation='Employed')
    l6 = Literal(stringRepresentation='Requestor is military official')
    r3 = Rule(l1, Operator.AND, l6)
    # l3 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r3,l4, ruleId=4))

    # Rule 5
    # l1 = Literal(stringRepresentation='Employed')
    l7 = Literal(stringRepresentation='Immunity due to unforseen circumstances')
    r4 = Rule(l1, Operator.AND, l7)
    # l3 = Literal(stringRepresentation='Cannot make a request')
    defeasibleRulesList.append(DefeasibleRule(r4,l2, ruleId=5))


    #################################################################################
    ### Rules for first legal action: Request by Employee Change in Working hours ###
    # Rule 6
    # l2 = Literal(stringRepresentation='Can make a request')
    l8 = Literal(stringRepresentation='Request is about a change in the working hours')
    r5 = Rule(l2, Operator.AND, l8)
    l9 = Literal(stringRepresentation='Legal request for a change in working hours')
    defeasibleRulesList.append(DefeasibleRule(r5,l9, ruleId=6))

    # Rule 7
    l10 = Literal(stringRepresentation='Request was submitted in writing')
    r6 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, createNegation(l10))
    # l11 = Literal(stringRepresentation='Not Legal request for a change in working hours')
    l11 = createNegation(l9)
    defeasibleRulesList.append(DefeasibleRule(r6, l11, ruleId=7))

    # Rule 8
    l12 = Literal(stringRepresentation='Time since last request is over a year')
    r7 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, createNegation(l12))
    defeasibleRulesList.append(DefeasibleRule(r7, l11, ruleId=8))

    # Rule 9
    l13 = Literal(stringRepresentation='Requestor worked at company for at least 26 weeks')
    r8 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, createNegation(l13))
    defeasibleRulesList.append(DefeasibleRule(r8, l11, ruleId=9))

    # Rule 10
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances') OR ANOTHER ONE ????
    r9 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r9, l9, ruleId=10))

    
    ##########################################################################
    # Rules for first legal action: Request by Employee Change in Working time
    # Rule 11
    l14 = Literal(stringRepresentation='Request is about a change in the working time')
    r10 = Rule(l2, Operator.AND, l14)
    l15 = Literal(stringRepresentation='Legal request for a change in working time')
    defeasibleRulesList.append(DefeasibleRule(r10, l15, ruleId=11))

    # Rule 12
    r11 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, createNegation(l10))
    #l16 = Literal(stringRepresentation='Not a legal request for a change in working time')
    l16 = createNegation(l15)
    defeasibleRulesList.append(DefeasibleRule(r11, l16, ruleId=12))

    # Rule 13
    r12 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, createNegation(l12))
    defeasibleRulesList.append(DefeasibleRule(r12, l16, ruleId=13))

    # Rule 14
    r13 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, createNegation(l13))
    defeasibleRulesList.append(DefeasibleRule(r13, l16, ruleId=14))

    # Rule 15
    r14 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r14, l15, ruleId=15))

    ###########################################################################
    # Rules for first legal action: Request by Employee Change in Working place
    # Rule 16
    l17 = Literal(stringRepresentation='Request is about a change in the working place')
    r15 = Rule(l2, Operator.AND, l17)
    l18 = Literal(stringRepresentation='Legal request for a change in working place')
    defeasibleRulesList.append(DefeasibleRule(r15, l18, ruleId=16))

    # Rule 17
    r16 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, createNegation(l10))
    # l19 = Literal(stringRepresentation='Not Legal request for a change in working place')
    l19 = createNegation(l18)
    defeasibleRulesList.append(DefeasibleRule(r16, l19, ruleId=17))

    # Rule 18
    r17 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, createNegation(l12))
    defeasibleRulesList.append(DefeasibleRule(r17, l19, ruleId=18))

    # Rule 19
    r18 = Rule (Rule(l2, Operator.AND, l17), Operator.AND, createNegation(l13))
    defeasibleRulesList.append(DefeasibleRule(r18, l19, ruleId=19))

    # Rule 20
    r19 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l7)
    defeasibleRulesList.append(DefeasibleRule(r19, l18, ruleId=20))


    ################################################################################
    # Rules resulting from legal action: Request by Employee Change in Working hours
    # Rule 21
    l20 = Literal(stringRepresentation='Duty of employer to consult employee about request (change working hours)')
    defeasibleRulesList.append(DefeasibleRule(l9, l20, ruleId=21))

    #Rule 22
    l21 = Literal(stringRepresentation='Duty of employer to accept request (change working hours)')
    defeasibleRulesList.append(DefeasibleRule(l9, l21, ruleId=22))

    # Rule 24
    l23 = Literal(stringRepresentation='Immunity due to substantial business interests')
    r20 = Rule(l9, Operator.AND, l23)
    # l24 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Hours')
    l24 = createNegation(l21)
    defeasibleRulesList.append(DefeasibleRule(r20, l24, ruleId=24))

    # Rule 25
    l25 = Literal(stringRepresentation='Power of employer to reject request (change working hours)')
    defeasibleRulesList.append(DefeasibleRule(r20, l25, ruleId=25))

    # Rule 23
    # l22 = Literal(stringRepresentation='No power to Reject Request Change Working Hours')
    l22 = createNegation(l25)
    defeasibleRulesList.append(DefeasibleRule(l9, l22, ruleId=23))


    ###############################################################################
    # Rules resulting from legal action: Request by Employee Change in Working time
    # Rule 26 
    l26 = Literal(stringRepresentation='Duty of employer to consult employee about request (change working times)')
    defeasibleRulesList.append(DefeasibleRule(l15, l26, ruleId=26))

    # Rule 27
    l27 = Literal(stringRepresentation='Duty of employer to accept request (change working times)')
    defeasibleRulesList.append(DefeasibleRule(l15, l27, ruleId=27))

    # Rule 29
    l29 = Literal(stringRepresentation='Immunity due for reasons of reasonableness and fairness')
    r21 = Rule(l15, Operator.AND, l29)
    # l30 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Times')
    l30 = createNegation(l27)
    defeasibleRulesList.append(DefeasibleRule(r21, l30, ruleId=29))

    # Rule 30
    l31 = Literal(stringRepresentation='Power of employer to change request (change working times)')
    defeasibleRulesList.append(DefeasibleRule(r21, l31, ruleId=30))

    #Rule 28
    # l28 = Literal(stringRepresentation='No POWER to Change Request Change Working Times')
    l28 = createNegation(l31)
    defeasibleRulesList.append(DefeasibleRule(l15, l28, ruleId=28))

    ################################################################################
    # Rules resulting from legal action: Request by Employee Change in Working place
    # Rule 31
    l32 = Literal(stringRepresentation='Duty of employer to contemplate request (change working place)')
    defeasibleRulesList.append(DefeasibleRule(l18, l32, ruleId=31))

    ##############################################################
    # Rules for legal action: Decision made on request by Employer
    # Rule 32
    l33 = Literal(stringRepresentation='Employer accepts request (change working hours)')
    r22 = Rule(l21, Operator.AND, l33)
    l34 = Literal(stringRepresentation='Legally accepted request (change working hours)')
    defeasibleRulesList.append(DefeasibleRule(r22, l34, ruleId=32))

    # Rule 33
    l35 = Literal(stringRepresentation='Decision on request was sent in writing')
    r23 = Rule(Rule(l21, Operator.AND, l33), Operator.AND, createNegation(l35))
    # l36 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Hours')
    l36 = createNegation(l34)
    defeasibleRulesList.append(DefeasibleRule(r23, l36, ruleId=33))

    # Rule 34
    l37 = Literal(stringRepresentation='Employer rejects request (change working hours)')
    r24 = Rule(l25, Operator.AND, l37)
    l38 = Literal(stringRepresentation='Legally rejected request (change working hours)')
    defeasibleRulesList.append(DefeasibleRule(r24, l38, ruleId=34))

    # Rule 35
    r25 = Rule(Rule(l25, Operator.AND, l37), Operator.AND, createNegation(l35))
    # l39 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Hours')
    l39 = createNegation(l38)
    defeasibleRulesList.append(DefeasibleRule(r25, l39, ruleId=35))

    # Rule 36
    l40 = Literal(stringRepresentation='Employer accepts request (change working times)')
    r26 = Rule(l27, Operator.AND, l40)
    l41 = Literal(stringRepresentation='Legally accepted request (change working times)')
    defeasibleRulesList.append(DefeasibleRule(r26, l41, ruleId=36))

    # Rule 37
    r27 = Rule(Rule(l27, Operator.AND, l40), Operator.AND, createNegation(l35))
    # l42 = Literal(stringRepresentation='NOT LEGAL Accepted Request Change Working Times')
    l42 = createNegation(l41)
    defeasibleRulesList.append(DefeasibleRule(r27, l42, ruleId=37))

    # Rule 38
    l43 = Literal(stringRepresentation='Employer changes request (change working times)')
    r28 = Rule(l31, Operator.AND, l43)
    l44 = Literal(stringRepresentation='Legally changed request (change working times)')
    defeasibleRulesList.append(DefeasibleRule(r28, l44, ruleId=38))

    # Rule 39
    r29 = Rule(Rule(l31, Operator.AND, l43), Operator.AND, createNegation(l35))
    # l45 = Literal(stringRepresentation='NOT a LEGAL Changed Request Change Working Times')
    l45 = createNegation(l44)
    defeasibleRulesList.append(DefeasibleRule(r29, l45, ruleId=39))

    # Rules 40
    l46 = Literal(stringRepresentation='Employer accepts request (change working place)')
    r30 = Rule(l32, Operator.AND, l46)
    l47 = Literal(stringRepresentation='Legally accepted request (change working place)')
    defeasibleRulesList.append(DefeasibleRule(r30, l47, ruleId=40))

    # Rule 41
    r31 = Rule(Rule(l32, Operator.AND, l46), Operator.AND, createNegation(l35))
    # l48 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Place')
    l48 = createNegation(l47)
    defeasibleRulesList.append(DefeasibleRule(r31, l48, ruleId=41))

    # Rule 42
    l49 = Literal(stringRepresentation='Employer rejects request (change working place)')
    r32 = Rule(l32, Operator.AND, l49)
    l50 = Literal(stringRepresentation='Legally rejected request (change working place)')
    defeasibleRulesList.append(DefeasibleRule(r32, l50, ruleId=42))

    # Rule 43 
    r33 = Rule(Rule(l32, Operator.AND, l49), Operator.AND, createNegation(l35))
    # l51 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Place')
    l51 = createNegation(l50)
    defeasibleRulesList.append(DefeasibleRule(r33, l51, ruleId=43))


    ################################################################
    # Rules for legal action: Employer too late with making decision
    # Rule 44
    l52 = Literal(stringRepresentation='Less than one month until commencement date of request')
    r34 = Rule(l52, Operator.AND, l9)
    defeasibleRulesList.append(DefeasibleRule(r34, l34, ruleId=44))

    # Rule 45
    r34 = Rule(Rule(l25, Operator.AND, l52), Operator.AND, l38)
    defeasibleRulesList.append(DefeasibleRule(r34, l36, ruleId=45))

    # Rule 46
    # l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
    l53 = Literal(stringRepresentation='Less than five days until commencement date of request')
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

    literalsListQuestions = [l1,l3,l5,l6,l7,l8,l10,l12,l13,l14,l17,
                    l33,l35,l37,l40,l43,l46,l49,
                    l52,l53]

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

    tests = [l2, l9, l15, l18, l20, l21, l25, l26, l27, l29, l31, l32, l34, l38, l41, l44, l47, l50]

    return [literalsListQuestions, defeasibleRulesList, order, tests]