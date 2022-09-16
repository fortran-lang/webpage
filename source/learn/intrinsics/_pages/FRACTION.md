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

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

 _fortran-lang intrinsic descriptions_
