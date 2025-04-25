(atan)=
## atan

### **Name**

**atan**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arctangent AKA inverse tangent function

### **Synopsis**

```fortran
    result = atan([x) | atan(y, x)
```

```fortran
     elemental TYPE(kind=KIND) function atan(y,x)

      TYPE(kind=KIND),intent(in) :: x
      TYPE(kind=**),intent(in),optional :: y
```

### **Characteristics**

- If **y** is present **x** and **y** must both be _real_.
  Otherwise, **x** may be _complex_.
- **KIND** can be any kind supported by the associated type.
- The returned value is of the same type and kind as **x**.

### **Description**

**atan**(3) computes the arctangent of **x**.

### **Options**

- **x**
  : The value to compute the arctangent of.
  if **y** is present, **x** shall be _real_.

- **y**
  : is of the same type and kind as **x**. If **x** is zero, **y**
  must not be zero.

### **Result**

The returned value is of the same type and kind as **x**. If **y** is
present, the result is identical to **atan2(y,x)**. Otherwise, it is the
arc tangent of **x**, where the real part of the result is in radians
and lies in the range
**-PI/2 \<= atan(x) \<= PI/2**

### **Examples**

Sample program:

```fortran
program demo_atan
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
character(len=*),parameter :: all='(*(g0,1x))'
real(kind=real64),parameter :: &
 Deg_Per_Rad = 57.2957795130823208767981548_real64
real(kind=real64) :: x
    x=2.866_real64
    print all, atan(x)

    print all, atan( 2.0d0, 2.0d0),atan( 2.0d0, 2.0d0)*Deg_Per_Rad
    print all, atan( 2.0d0,-2.0d0),atan( 2.0d0,-2.0d0)*Deg_Per_Rad
    print all, atan(-2.0d0, 2.0d0),atan(-2.0d0, 2.0d0)*Deg_Per_Rad
    print all, atan(-2.0d0,-2.0d0),atan(-2.0d0,-2.0d0)*Deg_Per_Rad

end program demo_atan
```

Results:

```text
   1.235085437457879
   .7853981633974483 45.00000000000000
   2.356194490192345 135.0000000000000
   -.7853981633974483 -45.00000000000000
   -2.356194490192345 -135.0000000000000
```

### **Standard**

FORTRAN 77 for a complex argument; and for two
arguments Fortran 2008

### **See Also**

[**atan2**(3)](#atan2), [**tan**(3)](#tan)

### **Resources**

- [wikipedia: inverse trigonometric functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
