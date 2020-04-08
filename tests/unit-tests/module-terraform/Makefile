MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)/../../../nomaj
.PHONY=validate test clean

validate: test
	echo "Show the merged config file"
	ls -l $(MAKEFILE_PATH)/config.yaml
	echo "Show the built files"
	ls -ld $(MAKEFILE_PATH)/build/*

test:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m terraform

clean:
	cd $(MAKEFILE_PATH) && rm -rf ./build
