class StrictRules:
    head : None
    body : None

    def isHeadValid(self):
        return self.head.inserpret()

    def isDefeasibleRules(self):
        return False

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody

class DefeasibleRules:
    head : None
    body : None

    def isHeadValid(self):
        return self.head.inserpret()

    def isDefeasibleRules(self):
        return True

    def setHead(self, newHead):
        self.head = newHead
    
    def setBody(self, newBody):
        self.body = newBody