cmake_minimum_required(VERSION 3.10)

# Set the project name
project(SimpleTextEditor)

# Find wxWidgets package (ensure it's installed and available)
find_package(wxWidgets REQUIRED COMPONENTS core base richtext)

# Include wxWidgets' necessary settings
include(${wxWidgets_USE_FILE})

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable target with the source file(s)
add_executable(SimpleTextEditor WIN32 main.cpp)

# Link wxWidgets libraries to your project
target_link_libraries(SimpleTextEditor ${wxWidgets_LIBRARIES})
