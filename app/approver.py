import app.decision as descision
import app.ratesetter as ratesetter
class Approver(object): # pylint: disable=too-few-public-methods
    def __init__(self, thelenders):
        self.lenders = thelenders

    def get_decision(self, requestedamount):
        currentdecision = descision.Decision()
        currentdecision.requestedamount = requestedamount

        currentdecision = self.get_lender_approval(currentdecision)

        return currentdecision

    def get_lender_approval(self, currentdescision):

        currentdescision = self.lenders.get_decision(currentdescision)

        if currentdescision.insufficent_offers:
            return currentdescision

        ratecalculator = ratesetter.Ratesetter(rate=currentdescision.rate, loan=currentdescision.requestedamount)

        ratecalculator.calculate()

        currentdescision.rate = round(ratecalculator.interest_rate, 4)
        currentdescision.monthlyrepayment = round(ratecalculator.monthly_repayment, 2)
        currentdescision.totalrepayment = round(ratecalculator.total_repayment, 2)
        return currentdescision
