# pylint: disable=too-few-public-methods
# -*- coding: utf-8 -*-
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
        output = "Requested amount: £{0} \n Rate: {1}%".format(self.requestedamount, self.rate)
        output += "\n Monthly repayments: £{0}\n Total repayment: £{1}".format(self.monthlyrepayment, self.totalrepayment)
        return output
    def create_test_decision(self):
        self.requestedamount = 300
        self.rate = 8.0
        self.monthlyrepayment = 30
        self.totalrepayment = 400
        self.insufficent_offers = False
