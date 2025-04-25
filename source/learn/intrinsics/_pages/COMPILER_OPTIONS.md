(compiler_options)=
## compiler_options

### **Name**

**compiler_options**(3) - \[COMPILER:INQUIRY\] Options passed to the compiler

### **Synopsis**

```fortran
    result = compiler_options()
```

```fortran
     character(len=:) function compiler_options()
```

### **Characteristics**

- the return value is a default-kind _character_ variable with
  system-dependent length.

### **Description**

**compiler_options**(3) returns a string with the options used for
compiling.

### **Options**

None.

### **Result**

The result contains the compiler flags used to compile the file
containing the **compiler_options**(3) call.

### **Examples**

Sample program:

```fortran
program demo_compiler_version
use, intrinsic :: iso_fortran_env, only : compiler_version
use, intrinsic :: iso_fortran_env, only : compiler_options
implicit none
   print '(4a)', &
      'This file was compiled by ', &
      compiler_version(),           &
      ' using the options ',        &
      compiler_options()
end program demo_compiler_version
```

Results:

```text
This file was compiled by GCC version 10.3.0 using
the options -I build/gfortran_2A42023B310FA28D
-mtune=generic -march=x86-64 -auxbase-strip
build/gfortran_2A42023B310FA28D/compiler_options/app_main.f90.o
-g -Wall -Wextra -Wimplicit-interface -fPIC -fmax-errors=1
-fcheck=bounds -fcheck=array-temps -fbacktrace
-fcoarray=single -J build/gfortran_2A42023B310FA28D
-fpre-include=/usr/include/finclude/math-vector-fortran.h

This file was compiled by nvfortran 21.5-0 LLVM
using the options app/main.f90 -c -Minform=inform
-Mbackslash -Mbounds -Mchkptr -Mchkstk -traceback -module
build/nvfortran_78229DCE997517A4 -Ibuild/nvfortran_78229DCE997517A4 -o
build/nvfortran_78229DCE997517A4/compiler_options/app_main.f90.o

This file was compiled by Intel(R) Fortran Intel(R) 64 Compiler Classic
for applications running on Intel(R) 64, Version 2021.3.0 Build
20210609_000000 using the options -Ibuild/ifort_5C58216731706F11
-c -warn all -check all -error-limit 1 -O0 -g -assume
byterecl -traceback -module build/ifort_5C58216731706F11 -o
build/ifort_5C58216731706F11/compiler_options/app_main.f90.o
```

### **Standard**

Fortran 2008

### **See Also**

[**compiler_version**(3)](#compiler_version),
**iso_fortran_env**(7)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
