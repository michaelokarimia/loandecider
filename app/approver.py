import app.decision as descision
class Approver(object): # pylint: disable=too-few-public-methods
    """Calculates loan decisions"""
    def __init__(self, lendersDict):
        self.lenders = lendersDict

    def getdecision(self, requestedamount):
        """Returns a loan decision"""
        currentdescision = descision.Decision()
        currentdescision.requestedamount = requestedamount

        if len(self.lenders) == 0:
            return currentdescision

        return currentdescision
