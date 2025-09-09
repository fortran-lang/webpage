(nearest)=
## nearest

### **Name**

**nearest**(3) - \[MODEL_COMPONENTS\] Nearest representable number

### **Synopsis**

```fortran
    result = nearest(x, s)
```

```fortran
     elemental real(kind=KIND) function nearest(x,s)

      real(kind=KIND),intent(in) :: x
      real(kind=**),intent(in) :: s
```

### **Characteristics**

- **x** may be a _real_ value of any kind.
- **s** may be a _real_ value of any kind.
- The return value is of the same type and kind as **x**.
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**nearest**(3) returns the processor-representable number nearest to
**x** in the direction indicated by the sign of **s**.

### **Options**

- **x**
  : the value to find the nearest representable value of

- **s**
  : a non-zero value whose sign is used to determine the direction in
  which to search from **x** to the representable value.

  If **s** is positive, **nearest** returns the processor-representable
  number greater than **x** and nearest to it.

  If **s** is negative, **nearest** returns the processor-representable
  number smaller than **x** and nearest to it.

### **Result**

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

Fortran 95

### **See Also**

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions_
