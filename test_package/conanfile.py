#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class TinyxmlTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_paths", "cmake_find_package")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not tools.cross_building(self.settings):
            cmake.test()

    def imports(self):
        pass

    def test(self):
        if not tools.cross_building(self.settings):
            print("SUCCESS")
        else:
            print("NOT_RUN (cross-building)");
