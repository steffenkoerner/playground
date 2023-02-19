cmake_minimum_required(VERSION 3.5)

project(HelloWorld)

add_library(${PROJECT_NAME}_library
    src/helloWorldLibrary.cpp
)

add_library(${PROJECT_NAME}::${PROJECT_NAME}_library ALIAS ${PROJECT_NAME}_library)

target_include_directories(${PROJECT_NAME}_library
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_executable(${PROJECT_NAME}_executable
    src/helloWorldExecutable.cpp
)

target_include_directories(${PROJECT_NAME}_executable
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}_executable
    PRIVATE
        ${PROJECT_NAME}_library
)
