MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)../../../nomaj
.PHONY=test clean

test:
	$(info Test)
	@cd $(MAKEFILE_PATH) && $(NOMAJ)

clean:
	$(info Clean)
	@cd $(MAKEFILE_PATH) && $(NOMAJ) -x clean
