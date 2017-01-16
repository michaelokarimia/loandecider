import codecs
class Lenders(object):

    def __init__(self, filename):
        self.filename = filename
        self.lenderscount = 0
        self.lenders = dict()

    def load_lenders(self):

        with codecs.open(self.filename, 'r', encoding='utf-8') as marketfile:
            marketfile.readline() #assumes first line is columns names in csv file

            for line in marketfile:
                self.lenderscount += 1
                mylist = line.split(',')
                lendic = {mylist[0]:[float(mylist[1]), float(mylist[2])]}
                self.lenders.update(lendic)

        marketfile.close()

    def is_sufficient_offers(self, loanrequest):
        if len(self.lenders) == 0:
            return False
        amount_available = self.get_available_loan_amount()
        if loanrequest > amount_available:
            return False
        return True

    def test_lender_data(self, test_lender_data):
        self.lenders = test_lender_data
        self.lenderscount = 0

    def get_available_loan_amount(self):
        runningtotal = 0.0

        offers = {key:value[1] for key, value in self.lenders.items()}

        for dummy_key, value in offers.items():
            runningtotal += value
        return runningtotal

    def get_decision(self, adecision):
        if self.is_sufficient_offers(adecision.requestedamount):
            adecision.rate = 0.075
        return adecision

    def get_best_rate_from_lenders(self, loan):

        offers = {key:value for key, value in self.lenders.items()}
        print "offers {0}".format(offers)

        bestrate = 1.0
        for dummy_key, value in offers.items():
            print "value is {0}".format(value)
            print "value loan is {0}".format(value[1])
            print "value rate is {0}".format(value[0])

            if value[1] >= loan and value[0] < bestrate:
                bestrate = value[0]

        print bestrate
        return bestrate
