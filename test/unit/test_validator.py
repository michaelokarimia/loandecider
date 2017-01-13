import unittest
import lib.validator as validator

# pylint: disable=R0904
class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = validator.Validator()

    def test_validate(self):
        thing_that_is_true = self.validator.isvalid()
        self.assertTrue(thing_that_is_true)

    def rejects_missing_arguments(self):
        self.validator.isvalid()
        print type(self.validator)
