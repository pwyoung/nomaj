TESTS = $(wildcard tests/*)
.PHONY=test

test:
	@for test in $(TESTS) ; do \
		echo "Test: $$test"; \
		make -C $$test; \
	done

