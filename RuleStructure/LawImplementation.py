from Logic.Literal import Literal
from Logic.Rule import *
from ArgumentationRule import StrictRule, DefeasibleRule


### Rules for initial situation ###
#Rule 1
l1 = Literal(stringRepresentation='Employed')
l2 = Literal(stringRepresentation='Can make a request')
DefeasibleRule(l1,l2)

# Rule 2
# l1 = Literal(stringRepresentation='Employed')
l3 = Literal(stringRepresentation='less that 10 employees')
r1 = Rule(l1, Operator.AND, l3)
l4 = Literal(stringRepresentation='Cannot make a request')
DefeasibleRule(r1,l4)

# Rule 3
# l1 = Literal(stringRepresentation='Employed')
l5 = Literal(stringRepresentation='Too old')
r2 = Rule(l1, Operator.AND, l5)
# l3 = Literal(stringRepresentation='Cannot make a request')
DefeasibleRule(r2,l4)

# Rule 4
# l1 = Literal(stringRepresentation='Employed')
l6 = Literal(stringRepresentation='Military official')
r3 = Rule(l1, Operator.AND, l6)
# l3 = Literal(stringRepresentation='Cannot make a request')
DefeasibleRule(r3,l4)

# Rule 5
# l1 = Literal(stringRepresentation='Employed')
l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
r4 = Rule(l1, Operator.AND, l7)
# l3 = Literal(stringRepresentation='Cannot make a request')
DefeasibleRule(r4,l4)


#################################################################################
### Rules for first legal action: Request by Employee Change in Working hours ###
# Rule 6
# l2 = Literal(stringRepresentation='Can make a request')
l8 = Literal(stringRepresentation='request is about a change in the working hours')
r5 = Rule(l2, Operator.AND, l8)
l9 = Literal(stringRepresentation='Legal request for a change in working hours')
DefeasibleRule(r5,l9)

# Rule 7
l10 = Literal(stringRepresentation='Request not submitted in writing')
r6 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l10)
l11 = Literal(stringRepresentation='Not Legal request for a change in working hours')
DefeasibleRule(r6, l11)

# Rule 8
l12 = Literal(stringRepresentation='time since last request over a year')
r7 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l12)
DefeasibleRule(r7, l11)

# Rule 9
l13 = Literal(stringRepresentation='Did not work for at least 26 weeks')
r8 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l13)
DefeasibleRule(r8, l11)

# Rule 10
# l7 = Literal(stringRepresentation='Immunity unforseen circumstances') OR ANOTHER ONE ????
r9 = Rule(Rule(l2, Operator.AND, l8), Operator.AND, l7)
DefeasibleRule(r9, l9)

 
##########################################################################
# Rules for first legal action: Request by Employee Change in Working time
# Rule 11
l14 = Literal(stringRepresentation='request is about a change in the working time')
r10 = Rule(l2, Operator.AND, l14)
l15 = Literal(stringRepresentation='Legal request for a change in working time')
DefeasibleRule(r10,l15)

# Rule 12
r11 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l10)
l16 = Literal(stringRepresentation='Not a legal request for a change in working time')
DefeasibleRule(r11, l16)

# Rule 13
r12 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l12)
DefeasibleRule(r12, l16)

# Rule 14
r13 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l13)
DefeasibleRule(r13, l16)

# Rule 15
r14 = Rule(Rule(l2, Operator.AND, l14), Operator.AND, l7)
DefeasibleRule(r14, l15)

###########################################################################
# Rules for first legal action: Request by Employee Change in Working place
# Rule 16
l17 = Literal(stringRepresentation='request is about a change in the working place')
r15 = Rule(l2, Operator.AND, l17)
l18 = Literal(stringRepresentation='Legal request for a change in working place')
DefeasibleRule(r15, l18)

# Rule 17
r16 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l10)
l19 = Literal(stringRepresentation='Not Legal request for a change in working place')
DefeasibleRule(r16, l19)

# Rule 18
r17 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l12)
DefeasibleRule(r17, l19)

# Rule 19
r18 = Rule (Rule(l2, Operator.AND, l17), Operator.AND, l13)
DefeasibleRule(r18, l19)

# Rule 20
r19 = Rule(Rule(l2, Operator.AND, l17), Operator.AND, l7)
DefeasibleRule(r19, l18)


################################################################################
# Rules resulting from legal action: Request by Employee Change in Working hours
# Rule 21
l20 = Literal(stringRepresentation='DUTY Consult Employee About Request Change Working Hours')
DefeasibleRule(l8, l20)

#Rule 22
l21 = Literal(stringRepresentation='DUTY Accept Request Change Working Hours')
DefeasibleRule(l8, l21)

# Rule 23
l22 = Literal(stringRepresentation='No power to Reject Request Change Working Hours')
DefeasibleRule(l8, l22)

# Rule 24
l23 = Literal(stringRepresentation='IMMUNITY Substantial Business Or Service Interests')
r20 = Rule(l8, l23)
l24 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Hours')
DefeasibleRule(l8, l24)

# Rule 25
l25 = Literal(stringRepresentation='power to Reject Request Change Working Hours')
DefeasibleRule(r20, l25)


###############################################################################
# Rules resulting from legal action: Request by Employee Change in Working time
# Rule 26 
l26 = Literal(stringRepresentation='DUTY to Consult Employee About Request Change Working Times')
DefeasibleRule(l15, l26)

# Rule 27
l27 = Literal(stringRepresentation='DUTY to Accept Request Change Working Times')
DefeasibleRule(l15, l27)

#Rule 28
l28 = Literal(stringRepresentation='No POWER to Change Request Change Working Times')
DefeasibleRule(l15, l28)

# Rule 29
l29 = Literal(stringRepresentation='IMMUNITY Interests Of Employee Yield For Reasons Of Reasonableness And Fairness')
r21 = Rule(l15, Operator.AND, l29)
l30 = Literal(stringRepresentation='Not a DUTY to Accept Request Change Working Times')
DefeasibleRule(r21, l30)

# Rule 30
l31 = Literal(stringRepresentation='POWER to Change Request Change Working Times')
DefeasibleRule(r21, l31)

################################################################################
# Rules resulting from legal action: Request by Employee Change in Working place
# Rule 31
l32 = Literal(stringRepresentation='DUTY to Contemplate Request Change Working Place')
DefeasibleRule(l18, l32)    

##############################################################
# Rules for legal action: Decision made on request by Employer
# Rule 32
l33 = Literal(stringRepresentation='DOES Accept Request Change Working Hours')
r22 = Rule(l21, Operator.AND, l33)
l34 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Hours')
DefeasibleRule(r22, l34)

# Rule 33
l35 = Literal(stringRepresentation='Decision On Request Not Sent In Writing')
r23 = Rule(Rule(l21, Operator.AND, l33), Operator.AND, l35)
l36 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Hours')
DefeasibleRule(r23, l36)

# Rule 34
l37 = Literal(stringRepresentation='DOES Reject Request Change Working Hours')
r24 = Rule(l25, Operator.AND, l37)
l38 = Literal(stringRepresentation='LEGAL Rejected Request Change Working Hours')
DefeasibleRule(r24, l38)

# Rule 35
r25 = Rule(Rule(l25, Operator.AND, l37), Operator.AND, l35)
l39 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Hours')
DefeasibleRule(r25, l39)

# Rule 36
l40 = Literal(stringRepresentation='DOES Accept Request Change Working Times')
r26 = Rule(l27, Operator.AND, l40)
l41 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Times')
DefeasibleRule(r26, l41)

# Rule 37
r27 = Rule(Rule(l27, Operator.AND, l40), Operator.AND, l35)
l42 = Literal(stringRepresentation='NOT LEGAL Accepted Request Change Working Times')
DefeasibleRule(r27, l42)

# Rule 38
l43 = Literal(stringRepresentation='DOES Change Request Change Working Times')
r28 = Rule(l31, Operator.AND, l43)
l44 = Literal(stringRepresentation='LEGAL Changed Request Change Working Times')
DefeasibleRule(r28, l44)

# Rule 39
r29 = Rule(Rule(l31, Operator.AND, l43), Operator.AND, l35)
l45 = Literal(stringRepresentation='NOT a LEGAL Changed Request Change Working Times')
DefeasibleRule(r29, l45)

# Rules 40
l46 = Literal(stringRepresentation='DOES Accept Request Change Working Place')
r30 = Rule(l32, Operator.AND, l46)
l47 = Literal(stringRepresentation='LEGAL Accepted Request Change Working Place')
DefeasibleRule(r30, l47)

# Rule 41
r31 = Rule(Rule(l32, Operator.AND, l46), Operator.AND, l35)
l48 = Literal(stringRepresentation='NOT a LEGAL Accepted Request Change Working Place')
DefeasibleRule(r31, l48)

# Rule 42
l49 = Literal(stringRepresentation='DOES Reject Request Change Working Place')
r32 = Rule(l32, Operator.AND, l49)
l50 = Literal(stringRepresentation='LEGAL Rejected Request Change Working Place')
DefeasibleRule(r32, l50)

# Rule 43 
r33 = Rule(Rule(l32, Operator.AND, l49), Operator.AND, l35)
l51 = Literal(stringRepresentation='NOT a LEGAL Rejected Request Change Working Place')
DefeasibleRule(r33, l51)


################################################################
# Rules for legal action: Employee too late with making decision
# Rule 44
l52 = Literal(stringRepresentation='Time Before Commencement Date Request Less Than One Month')
r34 = Rule(l52, Operator.AND, l9)
DefeasibleRule(r34, l34)

# Rule 45
r34 = Rule(Rule(l25, Operator.AND, l52), Operator.AND, l38)
DefeasibleRule(r34, l36)

# Rule 46
# l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
l53 = Literal(stringRepresentation='Time Before Commencement Date Request Less Than Five Days')
r35 = Rule(Rule(l9, Operator.AND, l7), Operator.AND, l53)
DefeasibleRule(r35, l34)

# Rule 47
r36 = Rule(Rule(Rule(l9, Operator.AND, l7), Operator.AND, l53), Operator.AND, l38)
DefeasibleRule(r36, l36)

# Rule 48
r37 = Rule(l15, Operator.AND, l52)
DefeasibleRule(r37, l41)

# Rule 49
r38 = Rule(Rule(l15, Operator.AND, l52), Operator.AND, l44)
DefeasibleRule(r38, l42)

# Rule 50
# l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
r39 = Rule(Rule(l15, Operator.AND, l7), Operator.AND, l53)
DefeasibleRule(r39, l41)

# Rule 51
r40 = Rule(Rule(Rule(l15, Operator.AND, l7), Operator.AND, l53), Operator.AND, l44)
DefeasibleRule(r40, l42)

# Rule 52
r41 = Rule(l18, Operator.AND, l52)
DefeasibleRule(r41, l47)

# Rule 53 
r42 = Rule(Rule(l18, Operator.AND, l52), Operator.AND, l50)
DefeasibleRule(r42, l48)

# Rule 54
# l7 = Literal(stringRepresentation='Immunity unforseen circumstances')
r43 = Rule(Rule(l18, Operator.AND, l7), Operator.AND, l53)
DefeasibleRule(r43, l47)

# Rule 55
r44 = Rule(Rule(Rule(l18, Operator.AND, l7), Operator.AND, l53), Operator.AND, l50)
DefeasibleRule(r44, l48)