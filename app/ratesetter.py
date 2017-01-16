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
        self.compound_interest_total_repayments(
        self.loan, self.interest_rate, REPAYMENTPERIOD))

    def compound_interest_total_repayments(self, loan, rate, months):
        #print loan
        if months == 0:
            return loan
        else:
            return self.compound_interest_total_repayments((loan
            * (Decimal(1.0) + rate) - self.monthly_repayment), rate, months - 1)

    def get_monthly_repayments(self):

        monthly_rate = Decimal((self.interest_rate * 100) / 100 / 12)
        principle = Decimal(self.loan)
        print "principle {0}".format(principle)
        print "rate as decimal {0}".format(monthly_rate)

        repayments = (principle * monthly_rate) / (1 -((1 + monthly_rate) ** (-REPAYMENTPERIOD)))

        print "repayments {0}".format(repayments)

        return Decimal(repayments)
