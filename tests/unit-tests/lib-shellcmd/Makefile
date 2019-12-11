MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
.PHONY=test clean

# TODO: replace this with a proper PyTest

test:
	$(info Test)
	$(MAKEFILE_PATH)/test.py

clean:
	$(info Clean)
