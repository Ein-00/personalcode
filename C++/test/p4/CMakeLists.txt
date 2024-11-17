cmake_minimum_required(VERSION 3.10)
project(SimpleTextEditor)

set(CMAKE_CXX_STANDARD 17)
 
# Include vcpkg toolchain if defined
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif()

find_package(unofficial-nana CONFIG REQUIRED)

add_executable(SimpleTextEditor main.cpp)
target_link_libraries(SimpleTextEditor PRIVATE unofficial::nana::nana)
