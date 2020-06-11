cmake_minimum_required(VERSION 3.1.2)
project (TinyXML CXX)

set(TARGET tinyxml)
set(CMAKE_DEBUG_POSTFIX "_d" CACHE STRING "Generate debug library name with a postfix.")
set(tinyXML_HDR tinystr.h tinyxml.h)

set(tinyXML_SRC
  tinystr.cpp       tinyxml.cpp
  tinyxmlerror.cpp  tinyxmlparser.cpp) #  xmltest.cpp)

#add_definitions( -DTIXML_USE_STL ) # add as option in package?

add_library(${TARGET} ${tinyXML_SRC})

target_include_directories(${TARGET}
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/>
    $<INSTALL_INTERFACE:include/>
  )

set_target_properties(${TARGET} PROPERTIES PUBLIC_HEADER "${tinyXML_HDR}")

install(TARGETS ${TARGET}
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
  PUBLIC_HEADER DESTINATION include
  )
