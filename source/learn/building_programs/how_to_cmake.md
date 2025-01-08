# A brief introduction to CMake 

In a [previous section](project_make.md) the concept of Makefiles was introduced. Here, an alternative build system - CMake, is discussed. 

[CMake](https://cmake.org/) is a very popular build system heavily popularized and used within the C/C++ community. CMake is an open-source
project within the Kitware organization. 

Formally, CMake is a build-system generator. In short, CMake uses user coded directives to scan the source code to build and generates the 
files that can be used to compile the code, for example, Makefiles. As discussed in the Makefiles section, the module dependencies are up to the 
programmer to figure out. CMake automates this and allows the programmer to not worry about module dependencies. 

Additionally, CMake has myriad of features embedded into its "language" that allow for simple addition of dependencies, external libraries, etc. 

However, CMake removes the Makefile from the programmer. Thus, you don't have as fine grained control of how each file is compiled. This is a particular 
reason why some programmers dislike CMake. 

CMake can be downloaded from [here](https://cmake.org/download/). CMake cross-platform capabilities, allowing you to use it as a single build system 
to deploy on Mac, Windows, Linux with little overhead.

To exemplify the extendability of CMake we will build a small yet fun project. 

## A simple example 

Start by git cloning the following Github repository: 

We will do a example that compiles a project that contains both fixed and free format files, this will let us showcase some of CMake's cool features. 
Our directory structure is simple:

    .
    ├── CMakeLists.txt
    ├── source
        ├── CMakeLists.txt
        ├── main.f90
        └── f90
            ├── CMakeLists.txt        
            ├── module1.f90
            ├── module2.f90
            ├── module3.f90
        └── f77
            ├── CMakeLists.txt 
            ├── subroutine.f

By having a file in fixed format I will exemplify how you can adapt a modern build system into a project that might be using outdated
language features/standards. 

Old F77 routines rarely used `modules` and rely on free-floating subroutines, which sometimes depend on modules, as the code has been "modernized". 

Strategies for modernization are discussed in a later section. But first, let's isolate the f77 routines from the newer f90 ones. We will achieve 
this with CMake by putting the f77 routines in a separate static library to those written in f90. Our target is to compile two static libraries:

- f90 library
- f77 library

Finally, the executable main.f90 will be created and linked to the static libraries which contains the needed subroutines/modules.

We start by creating our top level CMakeLists.txt file. Which will set the compilers, libraries, and final project:

```
# set the minimum version
cmake_minimum_required(VERSION 3.22)

# Set the project name and specify that it is a Fortran project
project(MyFortranProject LANGUAGES Fortran)

# Set the directory to store the compiled Fortran modules (.mod files)
set(CMAKE_Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)

# create libraries for the f90 and f77 code
add_library(f90_lib STATIC)
add_library(f77_lib STATIC)

# Ensure the module files from the library are stored in the module directory
set_target_properties(f90_lib PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_Fortran_MODULE_DIRECTORY})

# Set compile flags for the module library (-Wall)
target_compile_options(f90_lib PRIVATE -Wall)

# Add the executable target for the main Fortran file in the source/ directory
add_executable(main_executable source/main.f90)

# Set compile flags for the main executable (-O3)
target_compile_options(main_executable PRIVATE -O3)

# Make sure the main executable can find the modules in the specified directory
target_include_directories(main_executable PRIVATE ${CMAKE_Fortran_MODULE_DIRECTORY})

# Link the libraries into the main executable 
target_link_libraries(main_executable PRIVATE f90_lib f77_lib)

# now, where are our source files?
add_subdirectory(source)
```

Now, we need to create the CMakeLists.txt files that help define our project. The next CMakeLists.txt file is at the source/ level: 

```
#add subdirectories f90 and f77 to the source directory
add_subdirectory(f90)
add_subdirectory(f77)
```

You can see that this is a very simple way of handling source directories, if there were more in here, they can simply be added to the project 
by doing `add_subdirectory(xyz)`. Now, each directory, which now contains source files, needs to have its own CMakeLists.txt:

```
# this is source/f90
# add the f90 file
# add the *.f90 sources we've chosen to the target static library we've created
target_sources(f90_lib PRIVATE module1.f90 module2.f90 module3.f90)
```

Similarly, the f77...

```
# this is source/f77
# add the f77 file
# add the *.f77 sources we've chosen to the target static library we've created
target_sources(f77_lib PRIVATE subroutine.f)
```

Now we're ready to build and compile our project. From the top level directory, we now create a `build` directory where we will actually compile the project:

```
mkdir build
cd build
cmake ../
make -j 
```

Once you execute the CMake step, you should see something similar to:

```
-- The Fortran compiler identification is GNU 9.4.0
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /usr/bin/f95 - skipped
-- Configuring done (0.6s)
-- Generating done (0.0s)
-- Build files have been written to: /home/jorgegv/personal-dev/fortran/fortran-cmake/build
```

Which indicates that is has found the gfortran compiler and the needed dependencies to create a build. Inside the build/ directory, there will now be 
certain files:

```
CMakeCache.txt  CMakeFiles  Makefile  cmake_install.cmake  modules  source
```

These are the files that control the entire build system of the project. From here, simply doing `make -j` will build our app correctly. 

## More complex module dependencies

CMake, like humans, is not perfect and will fail for complex module dependencies if you perform a parallel build (`make -j`) with sufficient cores. 
This is because race conditions between files and modules are generated which cannot be fullfilled. To prevent this happening and ensuring
that your compilation never fails due to parallel race conditions, one can create dependencies between libraries. For example: I know 
that my free floating, legacy subroutines, depend on certain modules being built; but I have 700 files to compile and want to use the 128 cores
of my machine... `make -j` fails. 

Because we were smart, we have separated files into libraries of their own, so we can set a dependency on f77 library needing f90 library to be 
compiled first. This can be done by `add_dependencies(f77_lib f90_lib)` this has told CMake that before you can start compiling the 
f77 library, f90 needs to be done first. 

This is mostly an edge case but you should be aware of this happening. With regular Make it cannot happen because you've explicitly
written the dependencies of each module and each file. 


