cmake_minimum_required(VERSION 3.10)
project(my_app)

# Add coverage flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --coverage")

# Enable testing
enable_testing()
add_subdirectory(googletest-main)
include_directories(googletest-main/googletest/include)

# Main app (no tests here)
add_executable(main_app src/main.cpp src/functions.cpp)

# Test executable (no main.cpp here)
add_executable(run_tests test/test_main.cpp src/functions.cpp)
target_link_libraries(run_tests gtest gtest_main)

# Register tests
add_test(NAME AllTests COMMAND run_tests)
