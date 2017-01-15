import unittest
import app.ratesetter as ratesetter
# pylint: disable=R0904
class TestRatesetter(unittest.TestCase):
    def test_calculates_interest(self):
        rate = ratesetter.Ratesetter(rate=0.075, loan=100.0)
        rate.calculate()
        self.assertEqual(round(rate.monthly_repayment, 2), 2.78)
        self.assertEqual(round(rate.total_repayment, 2), 175.0)
        self.assertEqual(rate.interest_rate, 0.5)
