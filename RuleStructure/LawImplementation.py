from Logic.Literal import *
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