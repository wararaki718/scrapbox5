cmake_minimum_required(VERSION 3.14)
project(cmake_sample)

# GoogleTest requires at least C++14
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

add_executable(a.out main.cpp hello.cpp)
