#!/usr/bin/env python
import argparse
import app.approver as approver
import app.lenders as lenders
if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description='Returns a quote for a loan')
    PARSER.add_argument('marketfile', type=str, help='csv formatted file containing marker data')
    PARSER.add_argument('loanamount', type=float, help='integer representing how much the requested loan')

    ARGS = PARSER.parse_args()
    print "arg reader: Requested amount to loan " + str(ARGS.loanamount)
    print "arg reader: File to read: " + str(ARGS.marketfile)

    LENDERS = lenders.Lenders(ARGS.marketfile)
    LENDERS.load_lenders()
    APPROVER = approver.Approver(LENDERS)

    DESCISION = APPROVER.get_decision(ARGS.loanamount)

    print DESCISION.display()
