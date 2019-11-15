MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)/../../nomaj
.PHONY=test clean

test:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible
	# Note: The above can be replaced with
	#cd $(MAKEFILE_PATH) && $(NOMAJ)
	# Which runs the vagrant and ansible modules and creates a Makefile

ansible:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible

clean:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant -x clean
	cd $(MAKEFILE_PATH) && rm -rf ./build
