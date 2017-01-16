from decimal import Decimal
REPAYMENTPERIOD = Decimal(36.0)
class Ratesetter(object):

    def __init__(self, rate, loan):
        self.interest_rate = Decimal(rate)
        self.loan = Decimal(loan)
        self.monthly_repayment = Decimal(0.0)
        self.total_repayment = Decimal(0.0)

    def calculate(self):
        self.monthly_repayment = Decimal(self.get_monthly_repayments())
        self.total_repayment = Decimal(
        self.monthly_repayment * REPAYMENTPERIOD)

    def get_monthly_repayments(self):

        monthly_rate = Decimal((self.interest_rate * 100) / 100 / 12)
        principle = Decimal(self.loan)

        repayments = (Decimal(principle * monthly_rate)) / (1 -((1 + monthly_rate) ** (-REPAYMENTPERIOD)))

        return round(Decimal(repayments), 8)
