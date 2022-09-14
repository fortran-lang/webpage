## asinh

### **Name**

**asinh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Inverse hyperbolic sine function

### **Syntax**

```fortran
result = asinh(x)

    elemental TYPE(kind=KIND) function asinh(x)
    TYPE(kind=KIND) :: x
```

Where the returned value has the kind of the input value
and TYPE may be _real_ or _complex_

### **Description**

**asinh(x)** computes the inverse hyperbolic sine of **x**.

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_.

### **Returns**

The return value is of the same type and kind as **x**. If **x** is _complex_, the
imaginary part of the result is in radians and lies between
**-PI/2 \<= aimag(asinh(x)) \<= PI/2**.

### **Examples**

Sample program:

```fortran
program demo_asinh
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=dp), dimension(3) :: x = [ -1.0d0, 0.0d0, 1.0d0 ]

    write (*,*) asinh(x)

end program demo_asinh
```

Results:

```text
  -0.88137358701954305  0.0000000000000000  0.88137358701954305
```

### **Standard**

Fortran 2008 and later

### **See Also**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

Inverse function: [**sinh**(3)](SINH)

_fortran-lang intrinsic descriptions_
