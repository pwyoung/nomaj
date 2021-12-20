MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ='nomaj' # Assumes nomaj is in $PATH
.PHONY=test clean

test:
	$(info Test make)
	@cd $(MAKEFILE_PATH) && $(NOMAJ) -m make
	@ssh node-1 lsblk

clean:
	$(info Clean make)
	@cd $(MAKEFILE_PATH) && $(NOMAJ) -m make -x clean
