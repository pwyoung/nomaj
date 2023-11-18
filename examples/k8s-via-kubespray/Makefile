MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
.PHONY=test clean ansible FORCE

#NOMAJ=$(MAKEFILE_PATH)/../../../nomaj/nomaj
NOMAJ='nomaj' # Assumes nomaj is in $PATH

default: test

FORCE:

# 'nomaj' defaults args (if none are given) are '-m make'.
# 'nomaj -m make' runs the equivalent of 'nomaj -v vagrant && nomaj -v ansible'
build: FORCE
	cd $(MAKEFILE_PATH) && $(NOMAJ)

test: build
	cd $(MAKEFILE_PATH)/bin && ./run_k8s_nomaj

clean: FORCE
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m vagrant -x clean
	cd $(MAKEFILE_PATH) && rm -rf ./build
	vagrant global-status --prune

################################################################################
# Conveniences
################################################################################

ansible: FORCE
	cd $(MAKEFILE_PATH) && $(NOMAJ) -m ansible

suspend:
	cd $(MAKEFILE_PATH)build/vagrant && vagrant suspend

resume:
	cd $(MAKEFILE_PATH)build/vagrant && vagrant resume
