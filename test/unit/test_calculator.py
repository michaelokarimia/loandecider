import unittest
import lib.calculator as calculator

# pylint: disable=R0904
class TestLoanCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_returns_a_decision(self):
        mydecision = self.calculator.getdecision()
        self.assertEqual(mydecision.requestedamount, 1000)
