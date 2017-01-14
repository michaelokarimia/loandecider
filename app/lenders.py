import io

class Lenders(object):

    def __init__(self, filename):
        self.filename = filename
        self.lenderscount = 0

    def load_lenders(self):
        marketfile = io.open(self.filename, encoding='utf-8')
        marketfile.readline() #assumes first line is columns names in csv file

        for line in marketfile:
            print line
            self.lenderscount += 1

        marketfile.close()
