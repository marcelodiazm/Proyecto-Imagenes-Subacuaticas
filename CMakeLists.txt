cmake_minimum_required(VERSION 3.0.0)
project(main VERSION 0.1.0)

include(CTest)
enable_testing()

# OJITO el directorio cambia por cada instalacion eso deben cambiarlo
set(OpenCV_DIR C:/Users/vscha/Documents/USM/opencv)

#SET(MY_VARIABLE "option_value" CACHE STRING "Some user-specified option")
#set(DATA "C:/Users/vscha/Documents/USM/2022-2/pdi_real/proyecto/data")


find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable(main main.cpp)

target_link_libraries( main ${OpenCV_LIBS})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)