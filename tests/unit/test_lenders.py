import unittest
import app.lenders as lenders
import app.decision as decision

# pylint: disable=R0904
class TestLender(unittest.TestCase):
    filename = "market_file.csv"

    def test_counts_loads_lenders_parsed_from_file(self):
        lenderlist = lenders.Lenders(self.filename)
        lenderlist.load_lenders()
        self.assertEqual(lenderlist.lenderscount, 7)
        self.assertEqual(len(lenderlist.lenders), 7)
        self.assertGreater(lenderlist.get_available_loan_amount(), 0.0)
        self.assertEqual(lenderlist.lenders['Bob'][0], float(0.075))
        self.assertEqual(lenderlist.lenders['Bob'][1], float(640.0))

    def test_can_load_test_data(self):
        lenderlist = lenders.Lenders(None)
        testdata = {'Bob': [0.075, 640]}
        lenderlist.test_lender_data(testdata)
        self.assertEqual(len(lenderlist.lenders), 1)
        self.assertEqual(lenderlist.lenders['Bob'][0], float(0.075))
        self.assertEqual(lenderlist.lenders['Bob'][1], float(640.0))

    def test_is_sufficient_when_one_offers_exists_for_loans(self):
        lenderlist = lenders.Lenders(None)
        lenderlist.test_lender_data({'Bob': [0.075, 640.3]})
        self.assertEqual(len(lenderlist.lenders), 1)
        self.assertTrue(lenderlist.is_sufficient_offers(60.0))

    def test_is_sufficient_when_multiple_offers_sum_to_match_loans(self):
        lenderlist = lenders.Lenders(None)
        lenderlist.test_lender_data({'Bob': [0.075, 51.0], 'Sue': [0.075, 50.0]})
        self.assertEqual(len(lenderlist.lenders), 2)
        self.assertTrue(lenderlist.is_sufficient_offers(100.0))

    def test_get_decision(self):
        lenderlist = lenders.Lenders(None)
        lenderlist.test_lender_data({'Bob': [0.075, 640.3]})
        testdecision = decision.Decision()
        adecision = lenderlist.get_decision(testdecision)
        self.assertEqual(len(lenderlist.lenders), 1)
        self.assertTrue(lenderlist.is_sufficient_offers(60.0))
        self.assertEqual(adecision.rate, 0.075)
