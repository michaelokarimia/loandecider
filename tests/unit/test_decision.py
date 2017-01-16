# -*- coding: utf-8 -*-
import unittest
import app.decision as decision

# pylint: disable=R0904
class TestDecision(unittest.TestCase):

    def test_display_prints_all_fields(self):
        subject = decision.Decision()
        subject.create_test_decision()
        display = subject.display()
        expected = 'Requested amount: £300 \n Rate: 6.1%\n Monthly repayments: £30.00'
        expected += '\n Total repayment: £400.00'
        self.assertMultiLineEqual(display, expected)
