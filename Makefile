.PHONY=deps test

TESTS=$(wildcard ./tests*/unit-tests/*)
# Edit this during dev to run just one test
#TESTS=./tests/unit-tests/module-make
#TESTS=./tests/unit-tests/module-ansible
#TESTS=./tests/unit-tests/module-vagrant

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

python3:
	$(info Install pips)
	pip3 -q install -r requirements.txt

ssh-config:
	$(info SSH config file must exist)
	test -f $(SSHCFG) || echo "creating $(SSHCFG)" && touch $(SSHCFG)

passwordless-ssh:
	$(info Passwordless SSH must work)
	ssh localhost whoami || echo 'WARNING: passwordless SSH failed.'

deps: python3 ssh-config passwordless-ssh
	$(info deps)
