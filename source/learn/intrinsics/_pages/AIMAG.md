## aimag

### **Name**

**aimag**(3) - \[TYPE:NUMERIC\] Imaginary part of complex number

### **Syntax**

```fortran
    result = aimag(z)

     complex(kind=KIND),elemental :: aimag

     complex(kind=KIND),intent(in) :: z
```
### **Description**

**aimag(z)** yields the imaginary part of complex argument **z**.

This is similar to the modern complex-part-designator **%IM** which also
designates the imaginary part of a value, accept a designator can appear
on the left-hand side of an assignment as well, as in **val%im=10.0**.

### **Arguments**

- **z**
  : The type of the argument shall be _complex_.

### **Returns**

The return value is of type _real_ with the kind type parameter of the
argument.

### **Examples**

Sample program:

```fortran
program demo_aimag
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
complex(kind=real32) z4
complex(kind=real64) z8
    z4 = cmplx(1.e0, 2.e0)
    z8 = cmplx(3.e0_real64, 4.e0_real64,kind=real64)
    print *, aimag(z4), aimag(z8)
    ! an elemental function can be passed an array
    print *
    print *, [z4,z4/2.0,z4+z4,z4**3]
    print *
    print *, aimag([z4,z4/2.0,z4+z4,z4**3])
end program demo_aimag
```
Results:
```text
  2.000000       4.00000000000000

 (1.000000,2.000000) (0.5000000,1.000000) (2.000000,4.000000)
 (-11.00000,-2.000000)

       2.000000       1.000000       4.000000      -2.000000
```
### **See Also**

[**real**(3)](REAL),
[**cmplx**(3)](CMPLX)

### **Standard**

FORTRAN 77 and later

_fortran-lang intrinsic descriptions_
