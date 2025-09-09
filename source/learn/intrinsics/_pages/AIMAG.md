(aimag)=
## aimag

### **Name**

**aimag**(3) - \[TYPE:NUMERIC\] Imaginary part of complex number

### **Synopsis**

```fortran
    result = aimag(z)
```

```fortran
     elemental complex(kind=KIND) function aimag(z)

      complex(kind=KIND),intent(in) :: z
```

### **Characteristics**

- The type of the argument **z** shall be _complex_ and any supported
  _complex_ kind

- The return value is of type _real_ with the kind type parameter of
  the argument.

### **Description**

**aimag**(3) yields the imaginary part of the complex argument **z**.

This is similar to the modern complex-part-designator **%IM** which also
designates the imaginary part of a value, accept a designator can appear
on the left-hand side of an assignment as well, as in **val%im=10.0**.

### **Options**

- **z**
  : The _complex_ value to extract the imaginary component of.

### **Result**

The return value is a _real_ value with the magnitude and sign of the
imaginary component of the argument **z**.

That is, If **z** has the value **(x,y)**, the result has the value
**y**.

### **Examples**

Sample program:

```fortran
program demo_aimag
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
character(len=*),parameter :: g='(*(1x,g0))'
complex              :: z4
complex(kind=real64) :: z8
   ! basics
    z4 = cmplx(1.e0, 2.e0)
    print *, 'value=',z4
    print g, 'imaginary part=',aimag(z4),'or', z4%im

    ! other kinds other than the default may be supported
    z8 = cmplx(3.e0_real64, 4.e0_real64,kind=real64)
    print *, 'value=',z8
    print g, 'imaginary part=',aimag(z8),'or', z8%im

    ! an elemental function can be passed an array
    print *
    print *, [z4,z4/2.0,z4+z4,z4**3]
    print *
    print *, aimag([z4,z4/2.0,z4+z4,z4**3])

end program demo_aimag
```

Results:

```text
 value= (1.00000000,2.00000000)
 imaginary part= 2.00000000 or 2.00000000
 value= (3.0000000000000000,4.0000000000000000)
 imaginary part= 4.0000000000000000 or 4.0000000000000000

 (1.00000000,2.00000000) (0.500000000,1.00000000) (2.00000000,4.00000000)
 (-11.0000000,-2.00000000)

   2.00000000       1.00000000       4.00000000      -2.00000000
```

### **Standard**

FORTRAN 77

### **See Also**

- [**cmplx**(3)](#cmplx) - Complex conversion function
- [**conjg**(3)](#conjg) - Complex conjugate function
- [**real**(3)](#real) - Convert to real type

Fortran has strong support for _complex_ values, including many intrinsics
that take or produce _complex_ values in addition to algebraic and
logical expressions:

[**abs**(3)](#abs),
[**acosh**(3)](#acosh),
[**acos**(3)](#acos),
[**asinh**(3)](#asinh),
[**asin**(3)](#asin),
[**atan2**(3)](#atan2),
[**atanh**(3)](#atanh),
[**atan**(3)](#atan),
[**cosh**(3)](#cosh),
[**cos**(3)](#cos),
[**co_sum**(3)](#co_sum),
[**dble**(3)](#dble),
[**dot_product**(3)](#dot_product),
[**exp**(3)](#exp),
[**int**(3)](#int),
[**is_contiguous**(3)](#is_contiguous),
[**kind**(3)](#kind),
[**log**(3)](#log),
[**matmul**(3)](#matmul),
[**precision**(3)](#precision),
[**product**(3)](#product),
[**range**(3)](#range),
[**rank**(3)](#rank),
[**sinh**(3)](#sinh),
[**sin**(3)](#sin),
[**sqrt**(3)](#sqrt),
[**storage_size**(3)](#storage_size),
[**sum**(3)](#sum),
[**tanh**(3)](#tanh),
[**tan**(3)](#tan),
[**unpack**(3)](#unpack),

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
