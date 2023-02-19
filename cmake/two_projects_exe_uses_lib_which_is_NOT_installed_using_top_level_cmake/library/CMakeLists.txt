cmake_minimum_required(VERSION 3.5)

project(Library 
    LANGUAGES C CXX)

set(CMAKE_INSTALL_PREFIX /home/steffen/LibraryTest)

add_library(MyLib STATIC
    src/helloWorldLibrary.cpp
)

target_include_directories(MyLib
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

add_library(MyLib::MyLib ALIAS MyLib)
