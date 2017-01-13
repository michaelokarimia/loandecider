import unittest
import lib.validator as validator

# pylint: disable=R0904
class TestValidator(unittest.TestCase):

    def setUp(self):
        self.subject = validator.Validator()

    def test_validate(self):
        thing_that_is_true = True
        self.assertTrue(thing_that_is_true)

    def test_validator(self):
        print type(self.subject)
