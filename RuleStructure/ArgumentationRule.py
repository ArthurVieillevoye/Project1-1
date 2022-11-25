class StrictRules:
    head: None
    body: None

    def isHeadValid(self):
        return self.head.interpret()

    def isDefeasible(self):
        return False

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody
    
    def set_body_value(self, val):
        # TODO: Pay attention, the body can be a logical rule as well --> Need to be taken care of.
        self.body.setValue(val)


class DefeasibleRules:
    head: None
    body: None

    def isHeadValid(self):
        return self.head.interpret()

    def isDefeasible(self):
        return True

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody