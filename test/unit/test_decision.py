# -*- coding: utf-8 -*-
import unittest
import lib.decision as decision

# pylint: disable=R0904
class TestDecision(unittest.TestCase):

    def test_display_prints_all_fields(self):
        subject = decision.Decision()
        display = subject.display()
        expected = 'Requested amount: £0 \n Rate: 0.0%\n Monthly repayments: £0'
        expected += '\n Total repayment: £0'
        self.assertMultiLineEqual(display, expected)
