## spacing

### **Name**

**spacing**(3) - \[MODEL_COMPONENTS\] Smallest distance between two numbers of a given type

### **Syntax**

```fortran
result = spacing(x)
```

### **Description**

Determines the distance between the argument **x** and the nearest adjacent
number of the same type.

### **Arguments**

- **x**
  : Shall be of type _real_.

### **Returns**

The result is of the same type as the input argument **x**.

### **Examples**

Sample program:

```fortran
program demo_spacing
implicit none
integer, parameter :: sgl = selected_real_kind(p=6, r=37)
integer, parameter :: dbl = selected_real_kind(p=13, r=200)

   write(*,*) spacing(1.0_sgl)      ! "1.1920929e-07"          on i686
   write(*,*) spacing(1.0_dbl)      ! "2.220446049250313e-016" on i686
end program demo_spacing
```

Results:

```text
      1.19209290E-07
      2.2204460492503131E-016
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
[**set_exponent**(3)](SET_EXPONENT),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
