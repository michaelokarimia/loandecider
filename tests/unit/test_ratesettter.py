import unittest
import app.ratesetter as ratesetter
# pylint: disable=R0904
class TestRatesetter(unittest.TestCase):
    def test_calculates_interest(self):
        calculator = ratesetter.Ratesetter(rate=0.075, loan=100.0)
        calculator.calculate()
        self.assertEqual(round(calculator.monthly_repayment, 2), 3.11)
        self.assertEqual(round(calculator.total_repayment, 2), 832.24)
        self.assertEqual(round(calculator.interest_rate, 3), 0.075)

    def test_gets_monthly_repayments(self):
        calculator = ratesetter.Ratesetter(rate=0.075, loan=100.0)
        monthlyrepayment = calculator.get_monthly_repayments()
        self.assertEqual(round(monthlyrepayment, 2), 3.11)
