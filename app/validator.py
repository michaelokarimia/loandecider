class Validator(object):

    def __init__(self):
        self.display = ""

    def validate(self, value):
        if (value % 100 == 0) and value >= 100 and value <= 15000:
            return True
        self.display = 'Requested amount of {0} must be a int in an increment of 100 between 100 to 15000'.format(value)
        return False
