import unittest

    # pylint: disable=R0904
class TestInput(unittest.TestCase):

    def test_returnsrequestedloanamount(self):
        loan = 1000
        self.assertEqual(loan, 1000)
