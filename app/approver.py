import app.decision as descision
class Approver(object): # pylint: disable=too-few-public-methods
    """Calculates loan decisions"""
    def __init__(self, thelenders):
        self.lenders = thelenders

    def get_decision(self, requestedamount):
        """Returns a loan decision"""
        currentdescision = descision.Decision()
        currentdescision.requestedamount = requestedamount

        return self.get_lender_approval(currentdescision)

    def get_lender_approval(self, currentdescision):

        if self.lenders.get_offers_for_loan(currentdescision):
            currentdescision.insufficent_offers = True
        else:
            currentdescision.insufficent_offers = False

        return currentdescision
