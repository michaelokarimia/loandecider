#Setup

A simple console app which calculates loan decisions for prospective borrowers to
obtain a quote from our pool of lenders for 36 month loans

Works on python 2.7

Assumes you already have pip installed

To lint the code first install pylint `sudo apt-get install pylint` for Debian based os'

Then to lint the code, run
`make lint`

#Tests

To execute the tests, run:

`make test-unit`

To execute the application with some sample data and example loan, run:

`make run`


To lint, unit test and execute the program with some default values run

`make`
