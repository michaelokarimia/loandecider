import unittest
import lib.calculator as calculator

# pylint: disable=R0904
class TestLoanCalculator(unittest.TestCase):
    requestedamount = 1000

    def setUp(self):

        self.calculator = calculator.Calculator()

    def test_returns_requested_loan(self):
        mydecision = self.calculator.getdecision(self.requestedamount)
        self.assertEqual(mydecision.requestedamount, self.requestedamount)

    def test_returns_insufficent_offers(self):
        mydecision = self.calculator.getdecision(1000000)
        self.assertEqual(mydecision.insufficent_offers, True)
