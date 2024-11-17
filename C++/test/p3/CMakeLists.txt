cmake_minimum_required(VERSION 3.10)
project(MyGTKApp)

set(CMAKE_CXX_STANDARD 11)

# Adjust the vcpkg path if necessary
set(CMAKE_TOOLCHAIN_FILE "C:/path/to/vcpkg/scripts/buildsystems/vcpkg.cmake")

find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK REQUIRED gtk+-3.0)

add_executable(MyGTKApp main.cpp)

target_include_directories(MyGTKApp PRIVATE ${GTK_INCLUDE_DIRS})
target_link_libraries(MyGTKApp PRIVATE ${GTK_LIBRARIES})
