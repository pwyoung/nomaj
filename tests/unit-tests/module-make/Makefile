MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)../../../nomaj
.PHONY=test clean

test:
	$(info Test make)
	@cd $(MAKEFILE_PATH) && $(NOMAJ) -m make

clean:
	$(info Clean make)
	@cd $(MAKEFILE_PATH) && $(NOMAJ) -m make -x clean
