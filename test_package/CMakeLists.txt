cmake_minimum_required(VERSION 3.13)
project(TinyxmlTest CXX)

include("${CMAKE_BINARY_DIR}/conan_paths.cmake")

add_executable(xmltest xmltest.cpp)
find_package(TinyXML REQUIRED)
target_link_libraries(xmltest TinyXML::TinyXML)

if(MSVC)
  target_compile_definitions(xmltest PRIVATE -D_CRT_SECURE_NO_WARNINGS) # strcpy, fopen
endif()

enable_testing()
add_test(NAME xmltest COMMAND xmltest)
