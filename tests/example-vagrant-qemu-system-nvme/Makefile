MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
NOMAJ=$(MAKEFILE_PATH)../../nomaj
.PHONY=test clean

test:
	@$(NOMAJ) -m vagrant

clean:
	@$(NOMAJ) -m vagrant -x clean
