## precision

### **Name**

**precision**(3) - \[NUMERIC MODEL\] Decimal precision of a real kind

### **Syntax**

```fortran
result = precision(x)
```

### **Description**

**precision(x)** returns the decimal precision in the model of the type
of **x**.

### **Arguments**

- **x**
  : Shall be of type _real_ or _complex_.

### **Returns**

The return value is of type _integer_ and of the default integer kind.

### **Examples**

Sample program:

```fortran
program demo_precision
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp) :: x(2)
complex(kind=dp) :: y

   print *, precision(x), range(x)
   print *, precision(y), range(y)
end program demo_precision
```

Results:

```text
              6          37
             15         307
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
[**radix**(3)](RADIX),
[**range**(3)](RANGE),
[**rrspacing**(3)](RRSPACING),
[**scale**(3)](SCALE),
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
