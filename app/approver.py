import app.decision as descision
import app.ratesetter as ratesetter
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

        if self.lenders.is_sufficient_offers(currentdescision.requestedamount):
            currentdescision.insufficent_offers = False
        else:
            currentdescision.insufficent_offers = True

        ratecalculator = ratesetter.Ratesetter(rate=0.07, loan=currentdescision.requestedamount)

        ratecalculator.calculate()

        currentdescision.rate = round(ratecalculator.interest_rate, 2)
        currentdescision.monthlyrepayment = round(ratecalculator.monthly_repayment, 2)
        currentdescision.totalrepayment = round(ratecalculator.total_repayment, 2)
        return currentdescision
