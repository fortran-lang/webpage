(fraction)=
## fraction

### **Name**

**fraction**(3) - \[MODEL_COMPONENTS\] Fractional part of the model representation

### **Synopsis**

```fortran
    result = fraction(x)
```

```fortran
     elemental real(kind=KIND) function fraction(x)

      real(kind=KIND),intent(in) :: fraction
```

### **Characteristics**

- **x** is of type _real_
- The result has the same characteristics as the argument.

### **Description**

**fraction**(3) returns the fractional part of the model representation
of **x**.

### **Options**

- **x**
  : The value to interrogate

### **Result**

The fractional part of the model representation of **x** is returned;
it is **x \* radix(x)\*\*(-exponent(x))**.

If **x** has the value zero, the result is zero.

If **x** is an IEEE NaN, the result is that NaN.

If **x** is an IEEE infinity, the result is an IEEE NaN.

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
     0.5700439      0.5700439
```

### **Standard**

Fortran 95

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
