import unittest
import app.approver as approver

# pylint: disable=R0904
class TestLoanApprover(unittest.TestCase):
    requestedamount = 1000

    def setUp(self):
        lenders = []
        self.approver = approver.Approver(lenders)

    def test_returns_requested_loan(self):
        mydecision = self.approver.getdecision(self.requestedamount)
        self.assertEqual(mydecision.requestedamount, self.requestedamount)

    def test_returns_insufficent_offers(self):
        mydecision = self.approver.getdecision(1000000)
        self.assertEqual(mydecision.insufficent_offers, True)
