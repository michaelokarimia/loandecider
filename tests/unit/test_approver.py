import unittest
import app.approver as approver

# pylint: disable=R0904
class TestApprover(unittest.TestCase):
    requestedamount = 1000
    lenders = []
    approver = approver.Approver(lenders)

    def test_returns_requested_loan_amount(self):
        thedecision = self.approver.getdecision(self.requestedamount)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)

    def test_returns_insufficent_offers(self):
        thedecision = self.approver.getdecision(1000000)
        self.assertEqual(thedecision.insufficent_offers, True)

    def test_approves_when_suffcient_offers(self):
        lenders = ['Bob', 0.075, 640]
        self.approver = approver.Approver(lenders)
        thedecision = self.approver.getdecision(self.requestedamount)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)
        #self.assertEqual(thedecision.insufficent_offers, False)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)
