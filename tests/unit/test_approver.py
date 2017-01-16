import unittest
import app.approver as approver
import app.lenders as thelenders

# pylint: disable=R0904
class TestApprover(unittest.TestCase):
    requestedamount = 500

    approver = approver.Approver(None)

    def setUp(self):
        lenders = thelenders.Lenders(None)
        lenders.test_lender_data({})
        self.approver = approver.Approver(lenders)


    def test_returns_requested_loan_amount(self):
        lenders = thelenders.Lenders(None)
        lenders.test_lender_data({})
        self.approver = approver.Approver(lenders)
        thedecision = self.approver.get_decision(self.requestedamount)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)

    def test_declines_and_returns_insufficent_offers(self):
        lenders = thelenders.Lenders(None)
        lenders.test_lender_data({})

        self.approver = approver.Approver(lenders)
        thedecision = self.approver.get_decision(100)
        self.assertEqual(thedecision.insufficent_offers, True)

    def test_approves_when_one_sufficent_offers(self):
        lenders = thelenders.Lenders(None)
        lenders.test_lender_data({'Bob': [0.075, 640]})
        self.approver = approver.Approver(lenders)
        thedecision = self.approver.get_decision(self.requestedamount)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)
        self.assertEqual(thedecision.insufficent_offers, False)

    def test_declines_when_multiple_offers_below_loan(self):
        lenders = thelenders.Lenders(None)
        lenders.test_lender_data({'Bob': [0.075, 100], 'Keith': [0.5, 400], 'Ian': [0.02, 100]})
        self.approver = approver.Approver(lenders)
        thedecision = self.approver.get_decision(self.requestedamount)
        self.assertEqual(thedecision.requestedamount, self.requestedamount)
        self.assertEqual(thedecision.insufficent_offers, True)
