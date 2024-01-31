BUILD_GENERATOR= "Ninja"
BUILD_TYPE ?= Debug

BUILD_DIR_X86 ?= build

# Defaults to building the project
all: build

# Configure poetry
configure:
	poetry install

# Configure CMake
configure_x86: configure
	@cmake -G $(BUILD_GENERATOR) \
	-S . \
	-B $(BUILD_DIR_X86) \
	-DCMAKE_BUILD_TYPE=$(BUILD_TYPE)

# Build
build: configure_x86
	@cmake --build $(BUILD_DIR_X86) --config $(BUILD_TYPE)

# Clean build directory
clean:
	@echo Cleaning build directory...
	@rm -rf $(BUILD_DIR_X86)
	@echo Cleaned!

