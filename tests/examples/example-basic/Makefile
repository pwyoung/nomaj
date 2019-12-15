
MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY=test bbuild test-vms clean FORCE

test: test-vms

test-vms: build
	$(info test vms)
	bash -x $(MAKEFILE_PATH)/test

build: FORCE
	$(info Test)
	nomaj

clean: FORCE
	$(info Clean)
	@nomaj -x clean

FORCE:
