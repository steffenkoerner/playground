cmake_minimum_required(VERSION 3.5)

include(GNUInstallDirs)

project(Library 
    LANGUAGES C CXX)

set(CMAKE_INSTALL_PREFIX /home/steffen/LibraryTest)

add_library(MyLib STATIC
    src/helloWorldLibrary.cpp
)

target_include_directories(MyLib
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

add_library(MyLib::MyLib ALIAS MyLib)

install(TARGETS MyLib
    EXPORT MyLibTargets
    ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
)

install(
  DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
  DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
)

install(EXPORT MyLibTargets
    FILE MyLibConfig.cmake
    NAMESPACE MyLib::
    DESTINATION  "${CMAKE_INSTALL_LIBDIR}/cmake/MyLib"
)
