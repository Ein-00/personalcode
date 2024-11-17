cmake_minimum_required(VERSION 3.10)
project(WxProject)

# Specify C++ version
set(CMAKE_CXX_STANDARD 11)

# Point to the vcpkg toolchain file
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif()

# Find Boost package

find_package(wxWidgets CONFIG REQUIRED)
# Add the executable
add_executable(WxProject WIN32  main.cpp)

# Link Boost libraries
target_link_libraries(WxProject PRIVATE wx::core wx::base)
