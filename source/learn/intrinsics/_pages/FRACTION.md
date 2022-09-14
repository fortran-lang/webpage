## fraction

### **Name**

**fraction**(3) - \[MODEL_COMPONENTS\] Fractional part of the model representation

### **Syntax**

```fortran
y = fraction(x)
```

### **Description**

**fraction(x)** returns the fractional part of the model representation
of **x**.

### **Arguments**

- **x**
  : The type of the argument shall be a _real_.

### **Returns**

The return value is of the same type and kind as the argument. The
fractional part of the model representation of **x** is returned; it is
**x \* radix(x)\*\*(-exponent(x))**.

### **Examples**

Sample program:

```fortran
program demo_fraction
implicit none
real :: x
   x = 178.1387e-4
   print *, fraction(x), x * radix(x)**(-exponent(x))
end program demo_fraction
```

Results:

```text
     0.570043862      0.570043862
```

### **Standard**

Fortran 95 and later

### **See Also**

[**digits**(3)](DIGITS),
[**epsilon**(3)](EPSILON),
[**exponent**(3)](EXPONENT),
[**huge**(3)](HUGE),
[**maxexponent**(3)](MAXEXPONENT),
[**minexponent**(3)](MINEXPONENT),
[**nearest**(3)](NEAREST),
[**precision**(3)](PRECISION),
[**radix**(3)](RADIX),
[**range**(3)](RANGE),
[**rrspacing**(3)](RRSPACING),
[**scale**(3)](SCALE),
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
