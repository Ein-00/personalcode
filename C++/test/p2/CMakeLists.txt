cmake_minimum_required(VERSION 3.10)
project(ImGuiExample)
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_STANDARD 11)

# Include vcpkg toolchain if defined
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
endif()

find_package(glfw3 CONFIG REQUIRED)
find_package(imgui CONFIG REQUIRED)
find_package(glad CONFIG REQUIRED)
find_package(OpenGL REQUIRED)

add_executable(ImGuiExample main.cpp)

# Link libraries
target_link_libraries(ImGuiExample PRIVATE glfw glad::glad imgui::imgui OpenGL::GL)
