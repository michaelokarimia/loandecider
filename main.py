#!/usr/bin/env python
import argparse
import app.approver as approver
if __name__ == '__main__':

    print 'Starting app'
    LENDERS = []

    PARSER = argparse.ArgumentParser(description='Returns a quote for a loan')
    PARSER.add_argument('loanamount', type=int, help='integer representing how much the requested loan')

    ARGS = PARSER.parse_args()
    print "arg reader: Requested amount to loan " + str(ARGS.loanamount)

    APPROVER = approver.Approver(LENDERS)

    DESCISION = APPROVER.get_decision(ARGS.loanamount)

    print DESCISION.display()
