
MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY=test clean

test: test-vms

test-vms: build
	$(info test vms)
	bash -x $(MAKEFILE_PATH)/test

build:
	$(info Test)
	nomaj

clean:
	$(info Clean)
	@nomaj -x clean
