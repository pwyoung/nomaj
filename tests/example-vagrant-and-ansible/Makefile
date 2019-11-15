MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)/../../nomaj
.PHONY=test clean

validate: test
	echo "Show the merged config file"
	ls -l $(MAKEFILE_PATH)/config.yaml
	echo "Show the built files"
	ls -ld $(MAKEFILE_PATH)/build/*

test:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible

clean: 
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant -x clean
	cd $(MAKEFILE_PATH) && rm -rf ./build
