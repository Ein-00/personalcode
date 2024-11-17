cmake_minimum_required(VERSION 3.10)
project(BoostExample)

# Specify C++ version
set(CMAKE_CXX_STANDARD 11)

# Point to the vcpkg toolchain file
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif()

# Find Boost package
find_package(Boost REQUIRED COMPONENTS filesystem)

# Add the executable
add_executable(BoostExample main.cpp)

# Link Boost libraries
target_link_libraries(BoostExample Boost::filesystem)
