(sqrt)=
## sqrt

### **Name**

**sqrt**(3) - \[MATHEMATICS\] Square-root function

### **Synopsis**

```fortran
    result = sqrt(x)
```

```fortran
     elemental TYPE(kind=KIND) function sqrt(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **TYPE** may be _real_ or _complex_.
- **KIND** may be any kind valid for the declared type.
- the result has the same characteristics as **x**.

### **Description**

**sqrt**(3) computes the principal square root of **x**.

The number whose square root is being considered is known as the
_radicand_.

In mathematics, a square root of a radicand **x** is a number **y**
such that **y\*y = x**.

Every nonnegative radicand **x** has two square roots of the same unique
magnitude, one positive and one negative. The nonnegative square root
is called the principal square root.

The principal square root of 9 is 3, for example, even though (-3)\*(-3)
is also 9.

Square roots of negative numbers are a special case of complex numbers,
where with **complex** input the components of the _radicand_ need
not be positive in order to have a valid square root.

### **Options**

- **x**
  : The radicand to find the principal square root of.
  If **x** is _real_ its value must be greater than or equal to zero.

### **Result**

The principal square root of **x** is returned.

For a _complex_ result the real part is greater than or equal to zero.

When the real part of the result is zero, the imaginary part has the
same sign as the imaginary part of **x**.

### **Examples**

Sample program:

```fortran
program demo_sqrt
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x, x2
complex :: z, z2

  ! basics
   x = 2.0_real64
   ! complex
   z = (1.0, 2.0)
   write(*,*)'input values ',x,z

   x2 = sqrt(x)
   z2 = sqrt(z)
   write(*,*)'output values ',x2,z2

  ! elemental
  write(*,*)'elemental',sqrt([64.0,121.0,30.0])

  ! alternatives
   x2 = x**0.5
   z2 = z**0.5
   write(*,*)'alternatively',x2,z2

end program demo_sqrt
```

Results:

```text
    input values    2.00000000000000      (1.000000,2.000000)
    output values    1.41421356237310      (1.272020,0.7861513)
    elemental   8.000000       11.00000       5.477226
    alternatively   1.41421356237310      (1.272020,0.7861513)
```

### **Standard**

FORTRAN 77

### **See also**

[**exp**(3)](#exp),
[**log**(3)](#log),
[**log10**(3)](#log10)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
