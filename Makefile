test:
	pytest $(ARGS)

coverage:
	coverage run -m pytest

coverage-report: coverage
	coverage report -m

coveralls: coverage-report
	coveralls

.PHONY: test coverage coverage-report coveralls
