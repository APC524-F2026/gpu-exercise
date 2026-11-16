cmake_minimum_required(VERSION 3.18...4.4)
project(Minuit2SimpleExample LANGUAGES CXX CUDA)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_executable(mandelbrot_area_serial src/serial.cpp src/mandelbrot_area.cpp)
add_executable(mandelbrot_area_gpu src/gpu.cu src/mandelbrot_area.cu)

if(DEFINED SKBUILD)

  # === CONFIGURE BINDING HERE ===

endif()
