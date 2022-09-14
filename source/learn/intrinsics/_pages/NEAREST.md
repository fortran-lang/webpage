## nearest

### **Name**

**nearest**(3) - \[MODEL_COMPONENTS\] Nearest representable number

### **Syntax**

```fortran
result = nearest(x, s)
```

### **Description**

**nearest(x, s)** returns the processor-representable number nearest to
**x** in the direction indicated by the sign of **s**.

### **Arguments**

- **x**
  : Shall be of type _real_.

- **s**
  : Shall be of type _real_ and not equal to zero.

### **Returns**

The return value is of the same type as **x**. If **s** is positive, **nearest**
returns the processor-representable number greater than **x** and nearest to
it. If **s** is negative, **nearest** returns the processor-representable number
smaller than **x** and nearest to it.

### **Examples**

Sample program:

```fortran
program demo_nearest
implicit none

   real :: x, y
   x = nearest(42.0, 1.0)
   y = nearest(42.0, -1.0)
   write (*,"(3(g20.15))") x, y, x - y

!  write (*,"(3(g20.15))") &
!   nearest(tiny(0.0),1.0), &
!   nearest(tiny(0.0),-1.0), &
!   nearest(tiny(0.0),1.0) -nearest(tiny(0.0),-1.0)

!  write (*,"(3(g20.15))") &
!   nearest(huge(0.0),1.0), &
!   nearest(huge(0.0),-1.0), &
!   nearest(huge(0.0),1.0)- nearest(huge(0.0),-1.0)

end program demo_nearest
```

Results:

```text
   42.0000038146973    41.9999961853027    .762939453125000E-05
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
[**precision**(3)](PRECISION),
[**radix**(3)](RADIX),
[**range**(3)](RANGE),
[**rrspacing**(3)](RRSPACING),
[**scale**(3)](SCALE),
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
