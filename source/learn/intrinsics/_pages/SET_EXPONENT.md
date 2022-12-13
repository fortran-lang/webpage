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

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

 _fortran-lang intrinsic descriptions_
