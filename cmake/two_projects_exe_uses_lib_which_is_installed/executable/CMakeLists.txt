cmake_minimum_required(VERSION 3.5)

set (CMAKE_CXX_STANDARD 14)
project(Executable)

find_package(MyLib CONFIG REQUIRED)

add_executable(${PROJECT_NAME}_executable
    src/helloWorldExecutable.cpp
)

target_include_directories(${PROJECT_NAME}_executable
    PRIVATE
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(${PROJECT_NAME}_executable
    PRIVATE
        MyLib::MyLib
)


