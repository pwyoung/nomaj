MAKEFILE_PATH=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))
TEST_SCRIPT=$(MAKEFILE_PATH)../../create-merged-config-file.py
CONFIG_FILE=$(MAKEFILE_PATH)/config.yaml
OVERRIDES_FILE=$(MAKEFILE_PATH)/overrides.yaml
MERGED_CONFIG_FILE=$(MAKEFILE_PATH)/build/config.yaml
EXPECTED_RESULT=$(MAKEFILE_PATH)/expected_result.yaml
.PHONY=test

test:
	@$(TEST_SCRIPT) \
		-c $(CONFIG_FILE) \
		-o $(OVERRIDES_FILE) \
		-m $(MERGED_CONFIG_FILE)
	@diff $(MERGED_CONFIG_FILE) $(EXPECTED_RESULT)

