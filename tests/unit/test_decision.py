# -*- coding: utf-8 -*-
import unittest
import app.decision as decision

# pylint: disable=R0904
class TestDecision(unittest.TestCase):

    def test_display_prints_all_fields(self):
        subject = decision.Decision()
        subject.create_test_decision()
        display = subject.display()
        expected = 'Requested amount: £300 \n Rate: 8.0%\n Monthly repayments: £30'
        expected += '\n Total repayment: £400'
        self.assertMultiLineEqual(display, expected)
