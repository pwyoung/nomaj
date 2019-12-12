# This assumes:
# - nomaj is in $PATH
# - All defaults should be used

MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
PWD=$(shell pwd)

.PHONY=test clean

test: test-vms

test-vms: build
	$(info test vms)
	bash -x $(MAKEFILE_PATH)/test

build: check_dir
	$(info Test)
	@nomaj

clean: check_dir
	$(info Clean)
	@nomaj -x clean

check_dir:
	if [ "$(MAKEFILE_PATH)" != "$(PWD)/" ]; \
		then echo "This should be run from the test directory: $(MAKEFILE_PATH)"; \
	fi
