# CUVIS C SDK

## Importing Cuvis C SDK via CMake 

In order to import cuvis to your CMake project, Cuvis must be installed (todo: add link to compatible version). 

First, you need to add the directory containing *FindCuvis.cmake* to *CMAKE_MODULE_PATH*, e.g.:
```
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/")
```

Then you need to run the *find_package* function:
```
find_package(Cuvis REQUIRED)
```

If cuvis is installed to default locations, they are found automatically. Else, locate the cuvis.lib and the directory containing cuvis.h.

Finally, link against *cuvis::cuvis*. In the following example, the tarket *main* is linked against cuvis:
```
add_executable(main main.c)
target_link_libraries(main PRIVATE cuvis::cuvis)
```