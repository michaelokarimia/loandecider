default: lint test

test:
	python -m unittest discover

lint:
	find . -name '*.py' -exec pylint --rcfile=pylint.cfg {} +
