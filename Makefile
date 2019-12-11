.PHONY=deps test

TESTS=$(wildcard ./tests*/unit-tests/*)

test: deps
	$(info tests)
	echo "Run all tests: $(TESTS)"
	@for test in $(TESTS); do \
		echo "Running Test: $$test"; \
		make -C $$test && \
		make -C $$test clean; \
	done

deps:
	$(info deps)
	pip3 -q install -r requirements.txt
