#!/usr/bin/env python
import argparse
import lib.calculator as calculator
if __name__ == '__main__':
    print 'Starting app'

    PARSER = argparse.ArgumentParser(description='Returns a quote for a loan')
    PARSER.add_argument('loanamount', type=int, help='integer representing how much the requested loan')

    ARGS = PARSER.parse_args()
    print "Requested amount to loan " + str(ARGS.loanamount)

    CALCULATOR = calculator.Calculator()

    DESCISION = CALCULATOR.getdecision(ARGS.loanamount)

    print DESCISION.display()
