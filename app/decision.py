# pylint: disable=too-few-public-methods
# -*- coding: utf-8 -*-
from decimal import Decimal

TWOPLACES = Decimal(10) ** -2
ONEPLACE = Decimal(10) ** -1


class Decision(object):
    def __init__(self):
        self.requestedamount = 0
        self.rate = 0.0
        self.monthlyrepayment = 0
        self.totalrepayment = 0
        self.insufficent_offers = True

    def display(self):
        if self.insufficent_offers:
            return "Unable to offer a loan as there are insufficent offers"
        output = "Requested amount: £{0} \n Rate: {1}%".format(self.requestedamount, Decimal(self.rate * 100).quantize(ONEPLACE))
        output += "\n Monthly repayments: £{0}\n Total repayment: £{1}".format(Decimal(self.monthlyrepayment).quantize(TWOPLACES), Decimal(self.totalrepayment).quantize(TWOPLACES))
        return output
    def create_test_decision(self):
        self.requestedamount = 300
        self.rate = 0.0612
        self.monthlyrepayment = 30
        self.totalrepayment = 400
        self.insufficent_offers = False
