import app.decision as descision
class Calculator(object): # pylint: disable=too-few-public-methods
    """Calculates loan decisions"""
    def __init__(self):
        self.lenders = []

    def getdecision(self, requestedamount):
        """Returns a load decision"""
        currentdescision = descision.Decision()
        currentdescision.requestedamount = requestedamount

        if len(self.lenders) == 0:
            return currentdescision

        return currentdescision
