# This assumes:
# - nomaj is in $PATH
# - All defaults should be used

MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

.PHONY=test clean


test: check_dir
	$(info Test)
	@nomaj

clean: check_dir
	$(info Clean)
	@nomaj -x clean

check_dir:
	if [ "$(MAKEFILE_PATH)" != "$(pwd)" ]; \
		then echo "This should be run from the test directory: $(MAKEFILE_PATH)"; \
	fi
