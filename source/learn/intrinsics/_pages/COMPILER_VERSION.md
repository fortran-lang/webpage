## compiler_version

### **Name**

**compiler_version**(3) - \[COMPILER INQUIRY\] Compiler version string

### **Syntax**

```fortran
str = compiler_version()
```

### **Description**

**compiler_version**(3) returns a string containing the name and
version of the compiler.

### **Arguments**

None.

### **Returns**

The return value is a default-kind string with system-dependent length.
It contains the name of the compiler and its version number.

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

```
   This file was compiled by GCC version 5.4.0 using the options
   -I /usr/include/w32api -I /home/urbanjs/V600/lib/CYGWIN64_GFORTRAN
   -mtune=generic -march=x86-64 -g -Wunused -Wuninitialized -Wall
   -std=f2008 -fbounds-check -fbacktrace -finit-real=nan
   -fno-range-check -frecord-marker=4
   -J /home/urbanjs/V600/lib/CYGWIN64_GFORTRAN
```

### **Standard**

Fortran 2008

### **See Also**

[**compiler_options**(3)](COMPILER_OPTIONS),
**iso_fortran_env**(7)

_fortran-lang intrinsic descriptions_
