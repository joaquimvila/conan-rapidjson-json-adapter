from conans import ConanFile, CMake, tools


class RapidjsonadapterConan(ConanFile):
    name = "RapidJSONAdapter"
    version = "0.1"
    description = "C++ JSON adapter based on rapidjson"
    url = "https://github.com/systelab/conan-rapidjson-json-adapter"
    homepage = "https://github.com/systelab/cpp-rapidjson-json-adapter"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "rapidjson", "json", "wrapper")	
    license = "MIT"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
	sources_folder = "src"

    def source(self):
        git = tools.Git(folder=self.sources_folder)
        git.clone("https://github.com/systelab/cpp-rapidjson-json-adapter.git", "static_shared")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.sources_folder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=self.sources_folder)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["RapidJSONAdapter"]
