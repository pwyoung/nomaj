.PHONY=deps test

ALL_TESTS=$(wildcard ./tests/*)
TESTS=$(subst "./tests/example-k8s-via-kubespray",, $(ALL_TESTS))

test: deps
	$(info tests)
	echo "Run all tests: $(TESTS)"
	for test in $(TESTS); do \
		echo "Running Test: $$test"; \
		pushd $$test && \
		make test && \
		make clean && \
		popd; \
	done

deps:
	$(info deps)
	pip3 -q install -r requirements.txt
