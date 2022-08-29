## set_exponent

### **Name**

**set_exponent**(3) - \[MODEL_COMPONENTS\] Set the exponent of the model

### **Syntax**

```fortran
result = set_exponent(x, i)
```

### **Description**

**set_exponent(x, i)** returns the real number whose fractional part is
that of **x** and whose exponent part is **i**.

### **Arguments**

- **x**
  : Shall be of type _real_.

- **i**
  : Shall be of type _integer_.

### **Returns**

The return value is of the same type and kind as **x**. The real number
whose fractional part is that that of **x** and whose exponent part if **i** is
returned; it is **fraction(x) \* radix(x)\*\*i**.

### **Examples**

Sample program:

```fortran
program demo_setexp
implicit none
real :: x = 178.1387e-4
integer :: i = 17
   print *, set_exponent(x, i), fraction(x) * radix(x)**i
end program demo_setexp
```

Results:

```text
      74716.7891       74716.7891
```

### **Standard**

Fortran 95 and later

### **See Also**

[**digits**(3)](DIGITS),
[**epsilon**(3)](EPSILON),
[**exponent**(3)](EXPONENT),
[**fraction**(3)](FRACTION),
[**huge**(3)](HUGE),
[**maxexponent**(3)](MAXEXPONENT),
[**minexponent**(3)](MINEXPONENT),
[**nearest**(3)](NEAREST),
[**precision**(3)](PRECISION),
[**radix**(3)](RADIX),
[**range**(3)](RANGE),
[**rrspacing**(3)](RRSPACING),
[**scale**(3)](SCALE),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

###### fortran-lang intrinsic descriptions
