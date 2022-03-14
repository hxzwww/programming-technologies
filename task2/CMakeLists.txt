cmake_minimum_required(VERSION 3.4.0)

project(task2)

execute_process(
    COMMAND python3 preparing.py                                                
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/A                                   
    ) 

add_custom_command(
    OUTPUT index.h
    COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py
    )

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)

add_executable(C C/main.cpp)
add_custom_target(RUNGENERATOR DEPENDS index.h)
add_dependencies(C RUNGENERATOR)

add_subdirectory(B)
target_link_libraries(C B)

target_include_directories(C PRIVATE ${CMAKE_SOURCE_DIR})
