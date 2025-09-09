(aint)=
## aint

### **Name**

**aint**(3) - \[NUMERIC\] Truncate toward zero to a whole number

### **Synopsis**

```fortran
    result = aint(x [,kind])
```

```fortran
     elemental real(kind=KIND) function iaint(x,KIND)

      real(kind=**),intent(in)   :: x
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- the result is a real of the default kind unless **kind** is specified.
- **kind** is an _integer_ initialization expression indicating the
  kind parameter of the result.

### **Description**

**aint**(3) truncates its argument toward zero to a whole number.

### **Options**

- **x**
  : the _real_ value to truncate.

- **kind**
  : indicates the kind parameter of the result.

### **Result**

The sign is the same as the sign of **x** unless the magnitude of **x**
is less than one, in which case zero is returned.

Otherwise **aint**(3) returns the largest whole number that does not
exceed the magnitude of **x** with the same sign as the input.

That is, it truncates the value towards zero.

### **Examples**

Sample program:

```fortran
program demo_aint
use, intrinsic :: iso_fortran_env, only : sp=>real32, dp=>real64
implicit none
real(kind=dp) :: x8
   print *,'basics:'
   print *,' just chops off the fractional part'
   print *,  aint(-2.999), aint(-2.1111)
   print *,' if |x| < 1 a positive zero is returned'
   print *,  aint(-0.999), aint( 0.9999)
   print *,' input may be of any real kind'
   x8 = 4.3210_dp
   print *, aint(-x8), aint(x8)
   print *,'elemental:'
   print *,aint([ &
    &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
    &  0.0,   &
    &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])
end program demo_aint
```

Results:

```text
 basics:
  just chops off the fractional part
  -2.000000      -2.000000
  if |x| < 1 a positive zero is returned
  0.0000000E+00  0.0000000E+00
  input may be of any real kind
  -4.00000000000000        4.00000000000000
 elemental:
  -2.000000      -2.000000      -2.000000      -2.000000      -1.000000
  -1.000000      0.0000000E+00  0.0000000E+00  0.0000000E+00   1.000000
   1.000000       2.000000       2.000000       2.000000       2.000000
```

### **Standard**

FORTRAN 77

### **See Also**

[**anint**(3)](#anint),
[**int**(3)](#int),
[**nint**(3)](#nint),
[**selected_int_kind**(3)](#selected_int_kind),
[**ceiling**(3)](#ceiling),
[**floor**(3)](#floor)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
