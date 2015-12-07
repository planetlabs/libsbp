# Generic makefile
#
# Standard Make file that is able to build a .tar.gz install
# file and install it to a satellite
#
# @author Derek Parham (derek@cosmogia.com)
#

include ../../makefiles/makefile.defs

SBP_GEN_BIN = generator.py
SBP_SC_YAML = ../../messages/yaml/sc
SBP_SC_AUTOGEN_DIR = sbp
SBP_SC_VERSION = 0.0

messages:
	@echo Generating SBP messages $<
	$(SBP_GEN_BIN) -i $(SBP_SC_YAML) -o $(SBP_SC_AUTOGEN_DIR) --python -r $(SBP_SC_VERSION)


