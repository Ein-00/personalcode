cmake_minimum_required(VERSION 3.10)
project(FmtExample)

# Include vcpkg toolchain if defined
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif()

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Find fmt package
set(CMAKE_PREFIX_PATH "C:/Users/Dell/Desktop/Programming/C++/test/installed/x64-windows/share")

find_package(fmt CONFIG REQUIRED)
# Add executable
add_executable(FmtExample main.cpp)

# Link fmt
target_link_libraries(FmtExample PRIVATE fmt::fmt)
