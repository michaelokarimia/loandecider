import unittest
import app.lenders as lenders
# pylint: disable=R0904
class TestLender(unittest.TestCase):
    filename = "market_file.csv"

    def test_counts_loads_lenders_parsed_from_file(self):
        lenderlist = lenders.Lenders(self.filename)
        lenderlist.load_lenders()
        self.assertEqual(lenderlist.lenderscount, 7)
        self.assertEqual(len(lenderlist.lenders), 7)
        self.assertEqual(lenderlist.lenders['Bob'][0], float(0.075))
        self.assertEqual(lenderlist.lenders['Bob'][1][0], float(640.0))
