## maxexponent

### **Name**

**maxexponent**(3) - \[NUMERIC MODEL\] Maximum exponent of a real kind

### **Syntax**

```fortran
result = maxexponent(x)
```

### **Description**

**maxexponent(x)** returns the maximum exponent in the model of the type
of **x**.

### **Arguments**

- **x**
  : Shall be of type _real_.

### **Returns**

The return value is of type _integer_ and of the default integer kind.

### **Examples**

Sample program:

```fortran
program demo_maxexponent
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp) :: x
real(kind=dp) :: y

   print *, minexponent(x), maxexponent(x)
   print *, minexponent(y), maxexponent(y)
end program demo_maxexponent
```

Results:

```text
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

###### fortran-lang intrinsic descriptions
