## exponent

### **Name**

**exponent**(3) - \[MODEL_COMPONENTS\] Exponent function

### **Syntax**

```fortran
result = exponent(x)
```

### **Description**

**exponent**(x) returns the value of the exponent part of **x**. If **x** is
zero the value returned is zero.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type default _integer_.

### **Examples**

Sample program:

```fortran
program demo_exponent
implicit none
real :: x = 1.0
integer :: i
   i = exponent(x)
   print *, i
   print *, exponent(0.0)
end program demo_exponent
```

Results:

```text
              1
              0
```

### **Standard**

Fortran 95 and later

### **See Also**

[**digits**(3)](DIGITS),
[**epsilon**(3)](EPSILON),
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
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
