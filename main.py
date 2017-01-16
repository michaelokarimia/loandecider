#!/usr/bin/env python
import argparse
import app.approver as approver
import app.lenders as lenders
import app.validator as validator
if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description='Returns a quote for a loan')
    PARSER.add_argument('marketfile', type=str, help='csv formatted file containing marker data')
    PARSER.add_argument('loanamount', type=float, help='integer representing how much the requested loan. Must be increment of 100 from 100 to 15000 inclusive')

    ARGS = PARSER.parse_args()
    VALIDATOR = validator.Validator()

    if not VALIDATOR.validate(ARGS.loanamount):
        print VALIDATOR.display
    else:

        LENDERS = lenders.Lenders(ARGS.marketfile)
        LENDERS.load_lenders()
        APPROVER = approver.Approver(LENDERS)

        DESCISION = APPROVER.get_decision(ARGS.loanamount)

        print DESCISION.display()
