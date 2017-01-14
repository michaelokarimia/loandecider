import unittest
import app.lenders as lenders
# pylint: disable=R0904
class TestLender(unittest.TestCase):
    filename = "market_file.csv"

    def test_loads_lenders_parses_from_file(self):
        lenderlist = lenders.Lenders(self.filename)
        lenderlist.load_lenders()
        self.assertEqual(lenderlist.lenders, 1)
