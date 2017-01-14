import io

class Lenders(object):

    def __init__(self, filename):
        self.filename = filename
        self.lenders = 0

    def load_lenders(self):
        marketfile = io.open(self.filename, encoding='utf-8')
        marketfile.read()
        marketfile.close()
