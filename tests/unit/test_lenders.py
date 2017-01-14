import unittest
import io
# pylint: disable=R0904
class TestLender(unittest.TestCase):
    filename = "market_file.csv"

    def test_lenders_parsed_from_file(self):
        marketfile = io.open(self.filename, encoding='utf-8')
        self.assertEqual(marketfile.name, 0, marketfile.name)
        marketfile.close()
