from decimal import Decimal
REPAYMENTPERIOD = Decimal(36.0)
class Ratesetter(object):

    def __init__(self, rate, loan):
        self.interest_rate = Decimal(rate)
        self.loan = Decimal(loan)
        self.monthly_repayment = Decimal(0.0)
        self.total_repayment = Decimal(0.0)

    def calculate(self):
        self.monthly_repayment = Decimal((self.loan/REPAYMENTPERIOD)*self.interest_rate)
        self.total_repayment = Decimal(
        self.compound_interest_total_repayments(
        self.loan, self.interest_rate, REPAYMENTPERIOD))

    def compound_interest_total_repayments(self, loan, rate, months):
        print loan
        if months == 0:
            return loan
        else:
            return self.compound_interest_total_repayments(loan -self.monthly_repayment
            + (loan * rate), rate, months -1)
