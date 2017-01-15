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

            #print "All lenders are {0} who are a type of{1}".format(self.lenders, type(self.lenders))

        marketfile.close()

    def is_sufficient_offers(self, loanrequest):
        print "number of lenders {0}".format(len(self.lenders))
        if len(self.lenders) == 0:
            return False
        amount_available = self.get_available_loan_amount() #self.lenders.values()[0][1]
        #print "requested amount {0}".format(loanrequest)
        #print "available amount to loan is {0}".format(amount_available)
        if loanrequest > amount_available:
            return False
        return True

    def test_lender_data(self, test_lender_data):
        self.lenders = test_lender_data
        self.lenderscount = 0

    def get_available_loan_amount(self):
        runningtotal = 0.0

        offers = {key:value[1] for key, value in self.lenders.items()}
        print "offers: {0}".format(offers)
        print "offers is a type of {0}".format(type(offers))

        for lender, value in offers.items():
            print "lender key  {0}".format(lender)
            print "value is a type of {0}".format(type(value))
            print "value is {0}".format(value)
            runningtotal += value
        print runningtotal
        return runningtotal
