#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import shutil


class TinyxmlConan(ConanFile):
    name = "tinyxml"
    version = "2.6.2"
    license = "Zlib"
    url = "https://github.com/sintef-ocean/conan-tinyxml"
    author = "SINTEF Ocean"
    homepage = "http://www.grinninglizard.com/tinyxml/"
    description = \
        "TinyXML is a simple, small, C++ XML parser "\
        "that can be easily integrating into other programs."
    topics = ("TinyXML", "XML", "parser")
    settings = "os", "compiler", "build_type", "arch"
    options = { "use_stl": [True, False],
                "fPIC": [True, False]}
    default_options = { "use_stl": True, "fPIC": True }
    exports_sources = "CMakeLists.txt"
    exports = "lib_license/LICENSE"
    source_file = "tinyxml_2_6_2.tar.gz"
    source_subfolder = "tinyxml"
    build_subfolder = "build_subfolder"

    def source(self):
        link = "https://sourceforge.net/projects/tinyxml/files/tinyxml/{}/{}"\
            .format(self.version, self.source_file)
        tools.get(link, sha1="cba3f50dd657cb1434674a03b21394df9913d764")
        shutil.move("CMakeLists.txt", self.source_subfolder + "/CMakeLists.txt")

    def configure(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        if self.settings.os != "Windows":
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.definitions["USE_STL"] = self.options.use_stl
        cmake.configure(source_folder=self.source_subfolder,
                        build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses", src="lib_license",
                  ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tinyxml"]
        if self.settings.build_type == "Debug":
            self.cpp_info.libs[0] += "_d"
        if self.options.use_stl:
            self.cpp_info.defines = ["TIXML_USE_STL"]
        self.cpp_info.name = "TinyXML"
