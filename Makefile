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
	$(info Passwordless SSH must work for complex playbooks)
	ssh localhost whoami || echo 'WARNING: passwordless SSH failed. This is used by playbooks such as the K8S installer.'

gsed-on-mac:
	$(info Require 'gsed' on Mac/OSX)
	if uname | grep Darwin &>/dev/null; then gsed --version &>/dev/null; fi

deps: python3 ssh-config passwordless-ssh gsed-on-mac
	$(info deps)
