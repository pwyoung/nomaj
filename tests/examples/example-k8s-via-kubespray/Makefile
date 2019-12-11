MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
.PHONY=test clean

#NOMAJ=$(MAKEFILE_PATH)/../../../nomaj
NOMAJ='nomaj' # Assumes nomaj is in $PATH


test:
#	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant
#	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible
# 'nomaj' with no args defaults to '-m make'
# which runs the equivalent of 'nomaj -v vagrant && nomaj -v ansible'
	cd $(MAKEFILE_PATH) && $(NOMAJ) 

ansible:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible

clean:
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant -x clean
	cd $(MAKEFILE_PATH) && rm -rf ./build
