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
                print lendic
                self.lenders.update(lendic)

        marketfile.close()
