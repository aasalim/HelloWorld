BUILD_GENERATOR= "Ninja"
BUILD_TYPE ?= Debug
CONAN_FLAGS ?=
BUILD_DIR_X86 ?= build

# Defaults to building the project
all: build

# Configure poetry
pre-configure:
	poetry install

# Configure CMake
configure: pre-configure
	poetry run conan install . --build=missing -s build_type=$(BUILD_TYPE) $(CONAN_FLAGS)

# Build
build: configure
	poetry run conan build . -s build_type=$(BUILD_TYPE) $(CONAN_FLAGS)

# Clean build directory
clean:
	@echo Cleaning build directory...
	@rm -rf $(BUILD_DIR_X86)
	@echo Cleaned!
	
conansource:
	conan source .

conanclean:
	conan remove "*" -c

conancreate:
	conan create .
	
conanlist:
	conan list "*"
