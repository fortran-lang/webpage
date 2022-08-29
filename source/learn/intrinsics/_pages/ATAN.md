## atan

### **Name**

**atan**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arctangent function

### **Syntax**

```fortran
  - result = __atan(y, x)__

   TYPE(kind=KIND):: atan
   TYPE(kind=KIND,intent(in) :: x
   TYPE(kind=KIND,intent(in),optional :: y
```

where **TYPE** may be _real_ or _complex_ and **KIND** may be any **KIND** supported
by the associated type. If **y** is present **x** is \_real`.

### **Description**

**atan(x)** computes the arctangent of **x**.

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_; if **y** is present, **x**
  shall be _real_.

- **y**
  : Shall be of the same type and kind as **x**. If **x** is zero, **y**
  must not be zero.

### **Returns**

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

FORTRAN 77 and later for a complex argument; and for two
arguments Fortran 2008 or later

### **See Also**

- [wikipedia: inverse trigonometric functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

[**atan2**(3)](ATAN2), [**tan**(3)](TAN)

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
