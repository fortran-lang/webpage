## minexponent

### **Name**

**minexponent**(3) - \[NUMERIC MODEL\] Minimum exponent of a real kind

### **Syntax**

```fortran
result = minexponent(x)
```

### **Description**

**minexponent(x)** returns the minimum exponent in the model of the type
of **x**.

### **Arguments**

- **x**
  : Shall be of type _real_.

### **Returns**

The return value is of type _integer_ and of the default integer kind.

### **Examples**

Sample program:

```fortran
program demo_minexponent
use, intrinsic :: iso_fortran_env, only : &
 &real_kinds, real32, real64, real128
implicit none
real(kind=real32) :: x
real(kind=real64) :: y
    print *, minexponent(x), maxexponent(x)
    print *, minexponent(y), maxexponent(y)
end program demo_minexponent
```

Expected Results:

```
        -125         128
       -1021        1024
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
