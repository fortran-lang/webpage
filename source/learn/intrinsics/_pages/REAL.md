(real)=
## real

### **Name**

**real**(3) - \[TYPE:NUMERIC\] Convert to real type

### **Synopsis**

```fortran
  result = real(x [,kind])
```

```fortran
   elemental real(kind=KIND) function real(x,KIND)

    TYPE(kind=**),intent(in) :: x
    integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- the type of **x** may be _integer_, _real_, or _complex_; or a BOZ-literal-constant.
- **kind** is a _integer_ initialization expression (a constant expression)
  - If **kind** is present it defines the kind of the _real_ result
  - if **kind** is not present
    - when **x** is _complex_ the result is a _real_ of the same kind as **x**.
    - when **x** is _real_ or _integer_ the result is a _real_ of default kind
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**real**(3) converts its argument **x** to a _real_ type.

The real part of a complex value is returned. For complex values this
is similar to the modern complex-part-designator **%RE** which also
designates the real part of a _complex_ value.

```fortran
      z=(3.0,4.0)     ! if z is a complex value
      print *, z%re == real(z) ! these expressions are equivalent
```

### **Options**

- **x**
  : An _integer_, _real_, or _complex_ value to convert to _real_.

- **kind**
  : When present the value of **kind** defines the kind of the result.

### **Result**

1.  **real(x)** converts **x** to a default _real_ type if **x** is an _integer_
    or _real_ variable.

2.  **real(x)** converts a _complex_ value to a _real_ type with the
    magnitude of the real component of the input with kind type
    parameter the same as **x**.

3.  **real(x, kind)** is converted to a _real_ type with kind type
    parameter **kind** if **x** is a _complex_, _integer_, or _real_ variable.

### **Examples**

Sample program:

```fortran
program demo_real
use,intrinsic :: iso_fortran_env, only : dp=>real64
implicit none
complex              :: zr = (1.0, 2.0)
doubleprecision      :: xd=huge(3.0d0)
complex(kind=dp) :: zd=cmplx(4.0e0_dp,5.0e0_dp,kind=dp)

   print *, real(zr), aimag(zr)
   print *, dble(zd), aimag(zd)

   write(*,*)xd,real(xd,kind=kind(0.0d0)),dble(xd)
end program demo_real
```

Results:

```
 1.00000000       2.00000000
 4.0000000000000000       5.0000000000000000
 1.7976931348623157E+308  1.7976931348623157E+308  1.7976931348623157E+308
```

### **Standard**

FORTRAN 77

### **See Also**

- [**aimag**(3)](#aimag) - Imaginary part of complex number
- [**cmplx**(3)](#cmplx) - Complex conversion function
- [**conjg**(3)](#conjg) - Complex conjugate function

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
