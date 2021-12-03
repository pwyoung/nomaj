.PHONY=deps test

TESTS=$(wildcard ./tests*/unit-tests/*)
TESTS=./tests/unit-tests/module-make

SSHCFG=$$HOME/.ssh/config

test: deps
	$(info tests)
	echo "Run all tests: $(TESTS)"
	@for test in $(TESTS); do \
		echo "Running Test: $$test"; \
		make -C $$test && \
		echo "Test $$test is running." && \
		sleep 5 && \
		make -C $$test clean; \
	done

deps:
	$(info deps)
	pip3 -q install -r requirements.txt
	test -f $(SSHCFG) || echo "creating $(SSHCFG)" && touch $(SSHCFG)
