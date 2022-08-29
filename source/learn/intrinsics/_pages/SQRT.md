## sqrt

### **Name**

**sqrt**(3) - \[MATHEMATICS\] Square-root function

### **Syntax**

```fortran
result = sqrt(x)

   TYPE(kind=KIND) elemental function sqrt(x) result(value)
   TYPE(kind=KIND),intent(in) :: x
   TYPE(kind=KIND) :: value
```

Where TYPE may be _real_ or _complex_ and **KIND** may be any
kind valid for the declared type.

### **Description**

**sqrt(x)** computes the principal square root of **x**.

In mathematics, a square root of a number **x** is a number **y** such
that **y\*y = x**.

The number whose square root is being considered is known as the
_radicand_.

Every nonnegative number _x_ has two square roots of the same unique
magnitude, one positive and one negative. The nonnegative square root
is called the principal square root.

The principal square root of 9 is 3, for example, even though (-3)\*(-3)
is also 9.

A _real_, _radicand_ must be positive.

Square roots of negative numbers are a special case of complex numbers,
where the components of the _radicand_ need not be positive in order to
have a valid square root.

### **Arguments**

- **x**
  : If **x** is real its value must be greater than or equal to zero.
  The type shall be _real_ or _complex_.

### **Returns**

The return value is of type _real_ or _complex_. The kind type parameter is
the same as **x**.

### **Examples**

Sample program:

```fortran
program demo_sqrt
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x, x2
complex :: z, z2

   x = 2.0_real64
   z = (1.0, 2.0)
   write(*,*)x,z

   x2 = sqrt(x)
   z2 = sqrt(z)
   write(*,*)x2,z2

   x2 = x**0.5
   z2 = z**0.5
   write(*,*)x2,z2

end program demo_sqrt
```

Results:

```text
  2.0000000000000000    (1.00000000,2.00000000)
  1.4142135623730951    (1.27201962,0.786151350)
  1.4142135623730951    (1.27201962,0.786151350)
```

### **Standard**

FORTRAN 77 and later

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
