import app.decision as descision
class Approver(object): # pylint: disable=too-few-public-methods
    """Calculates loan decisions"""
    def __init__(self, lendersDict):
        self.lenders = lendersDict

    def get_decision(self, requestedamount):
        """Returns a loan decision"""
        currentdescision = descision.Decision()
        currentdescision.requestedamount = requestedamount

        return self.get_lender_approval(currentdescision)

    def get_lender_approval(self, currentdescision):
        available_loan_amount = self.get_available_loan_amount()

        if available_loan_amount < currentdescision.requestedamount:
            currentdescision.insufficent_offers = True
        else:
            currentdescision.insufficent_offers = False

        return currentdescision

    def get_available_loan_amount(self):
        amount_available = 0
        if len(self.lenders) == 0:
            return 0
        return amount_available
