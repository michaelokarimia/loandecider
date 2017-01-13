default: lint test-unit

test-unit:
	python -m unittest discover

lint:
	find . -name '*.py' -exec pylint --rcfile=pylint.cfg {} +
