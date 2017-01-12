Works on python 2.7

Setup

Assumes you already have pip installed

To lint the code first install pylint `sudo apt-get install pylint` for Debian based os'

Then to lint the code execute
`find . -name '*.py' -exec pylint --reports=no {} +`

Tests

To run the tests

`python -m unittest discover`
