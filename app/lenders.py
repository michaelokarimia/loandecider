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
                lendic = {mylist[0]:[float(mylist[1]), [float(mylist[2])]]}
                #print lendic
                self.lenders.update(lendic)

        marketfile.close()

        runningtotal = 0.0

        offers = {key:value[1] for key, value in self.lenders.items()}
        #print offers

        for lender, value in offers.items():
            runningtotal += value[0]
            print lender
            print value
        print runningtotal

    def get_offers_for_loan(self, loanrequest):
        if len(self.lenders) == 0:
            return False
        amount_available = self.lenders.values()[0][1]
        if loanrequest > amount_available:
            return False
        print "available amount to load is {0}".format(amount_available)
        return True

    def test_lender_data(self, test_lender_data):
        self.lenders = test_lender_data
        self.lenderscount = 0
