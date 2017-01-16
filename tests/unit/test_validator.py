import unittest
import app.validator as validator
# pylint: disable=R0904
class TestValidator(unittest.TestCase):

    def test_validates_100(self):
        checker = validator.Validator()
        self.assertTrue(checker.validate(100))

    def test_rejects_102(self):
        checker = validator.Validator()
        self.assertFalse(checker.validate(102))

    def test_rejects_less_than_100(self):
        checker = validator.Validator()
        self.assertFalse(checker.validate(99))

    def test_rejects_0(self):
        checker = validator.Validator()
        self.assertFalse(checker.validate(0))

    def test_rejects_over_15000(self):
        checker = validator.Validator()
        self.assertFalse(checker.validate(15100))

    def test_display_returns_no_message_if_valid(self):
        checker = validator.Validator()
        checker.validate(100)
        self.assertEqual(checker.display, "")

    def test_display_returns_message_when_invalid(self):
        checker = validator.Validator()
        checker.validate(10)
        self.assertEqual(checker.display, "Requested amount of 10 must be a int in an increment of 100 between 100 to 15000")
