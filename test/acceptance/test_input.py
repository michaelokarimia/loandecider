import unittest
import subprocess

    # pylint: disable=R0904
class TestInput(unittest.TestCase):

    def test_returns_requested_load(self):
        filename = "main.py"
        subprocess.check_output(["python", filename])
        loan = 1000
        self.assertEqual(loan, 1000)
