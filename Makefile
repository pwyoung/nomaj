.PHONY=deps test

TESTS=$(wildcard ./tests*/unit-tests/*)
# Edit this during dev to run just one test
#TESTS=./tests/unit-tests/module-make
#TESTS=./tests/unit-tests/module-ansible
#TESTS=./tests/unit-tests/module-vagrant

SSHCFG=$$HOME/.ssh/config

default: test

FORCE:

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

python3: FORCE
	$(info Install pips)
	pip3 -q install -r requirements.txt

ssh-config: FORCE
	$(info SSH config file must exist)
	test -f $(SSHCFG) || echo "creating $(SSHCFG)" && touch $(SSHCFG)

passwordless-ssh: FORCE
	$(info Passwordless SSH must work)
	ssh localhost whoami || echo 'WARNING: passwordless SSH failed. This is used by complex Ansible playbooks such as the K8S installer.'

os-packages: FORCE
	$(info Install os-package dependencies)
	./deps/nomaj-deps.sh

deps: python3 ssh-config passwordless-ssh
	$(info deps)

