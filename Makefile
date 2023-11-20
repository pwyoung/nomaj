.PHONY=deps test

TESTS=$(wildcard ./tests*/unit-tests/*)
# Edit this during dev to run just one test
#TESTS=./tests/unit-tests/module-make
#TESTS=./tests/unit-tests/module-ansible
#TESTS=./tests/unit-tests/module-vagrant

#default: test
default: deps

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

setup-script: FORCE
	$(info Install os-package dependencies)
	./deps/nomaj-deps.sh

python3: setup-script
	$(info Install pips)
	pip3 -q install -r requirements.txt

passwordless-ssh: setup-script
	$(info Passwordless SSH must work)
	@ssh localhost whoami || echo 'WARNING: passwordless SSH failed. This is used by complex Ansible playbooks such as the K8S installer.'

deps: python3 passwordless-ssh
	$(info Installed dependencies for nomaj)
	$(info Run 'make test' to run tests)

