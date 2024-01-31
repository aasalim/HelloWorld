from conan import ConanFile

# CMake Dependencies
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout

class BasicConanfile(ConanFile):
    name = "helloworld"
    version = "1.0"
    description = "A basic recipe"
    license = "<Your project license goes here>"
    homepage = "<Your project homepage goes here>"

    # Check the documentation for the rest of the available attributes
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    # The requirements method allows you to define the dependencies of your recipe
    def requirements(self):
        # Each call to self.requires() will add the corresponding requirement
        # to the current list of requirements
        # Uncommenting this line will add the zlib/1.2.13 dependency to your project
        # self.requires("zlib/1.2.13")
        pass

    # The build_requirements() method is functionally equivalent to the requirements() one,
    # being executed just after it. It's a good place to define tool requirements,
    # dependencies necessary at build time, not at application runtime
    def build_requirements(self):
        # Each call to self.tool_requires() will add the corresponding build requirement
        # Uncommenting this line will add the cmake >=3.15 build dependency to your project
        # self.requires("cmake/[>=3.15]")
        pass
    
    def layout(self):
        cmake_layout(self)
                     
    # The purpose of generate() is to prepare the build, generating the necessary files, such as
    # Files containing information to locate the dependencies, environment activation scripts,
    # and specific build system files among others
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    # This method is used to build the source code of the recipe using the desired commands.
    def build(self):
        # You can use your command line tools to invoke your build system
        # or any of the build helpers provided with Conan in conan.tools
        # self.run("g++ ...")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # The actual creation of the package, once it's built, is done in the package() method.
    # Using the copy() method from tools.files, artifacts are copied
    # from the build folder to the package folder
    def package(self):
        # copy(self, "*.h", self.source_folder, join(self.package_folder, "include"), keep_path=False)
        pass
