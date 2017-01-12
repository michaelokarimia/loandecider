#!/usr/bin/env python
'''Validates input'''
class Validator(object): # pylint: disable=too-few-public-methods
    """Module which validates input"""
    def __init__(self):
        self.rules = [True]

    def validate(self):
        """Validates text against validation rules"""
        return self.rules[0]


if __name__ == '__main__':
    print 'Hello world'
    MYVALIDATOR = Validator()
    print MYVALIDATOR.validate()
