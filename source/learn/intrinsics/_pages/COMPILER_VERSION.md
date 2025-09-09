(compiler_version)=
## compiler_version

### **Name**

**compiler_version**(3) - \[COMPILER:INQUIRY\] Compiler version string

### **Synopsis**

```fortran
    result = compiler_version()
```

```fortran
     character(len=:) function compiler_version()
```

### **Characteristics**

- The return value is a default-kind scalar _character_ with
  system-dependent length.

### **Description**

**compiler_version**(3) returns a string containing the name and
version of the compiler.

### **Options**

None.

### **Result**

The return value contains the name of the compiler and its version
number used to compile the file containing the **compiler_version**(3)
call.

### **Examples**

Sample program:

```fortran
program demo_compiler_version
use, intrinsic :: iso_fortran_env, only : compiler_version
implicit none
   print '(2a)', &
      'This file was compiled by ', &
      compiler_version()
end program demo_compiler_version
```

Results:

```text
This file was compiled by GCC version 10.3.0

This file was compiled by Intel(R) Fortran Intel(R) 64 Compiler
Classic for applications running on Intel(R) 64, Version 2021.3.0 Build
20210609_000000

This file was compiled by nvfortran 21.5-0 LLVM
```

### **Standard**

Fortran 2008

### **See Also**

[**compiler_options**(3)](#compiler_options),
**iso_fortran_env**(7)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
