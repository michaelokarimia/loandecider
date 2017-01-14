default: lint test-unit run

test-unit:
	python -m unittest discover

lint:
	find . -name '*.py' -exec pylint --rcfile=pylint.cfg {} +

run:
	python main.py 999
