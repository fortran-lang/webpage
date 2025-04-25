(minexponent)=
## minexponent

### **Name**

**minexponent**(3) - \[NUMERIC MODEL\] Minimum exponent of a real kind

### **Synopsis**

```fortran
    result = minexponent(x)
```

```fortran
     elemental integer function minexponent(x)

      real(kind=**),intent(in) :: x
```

### **Characteristics**

- **x** is a _real_ scalar or array of any _real_ kind
- the result is a default _integer_ scalar

### **Description**

**minexponent**(3) returns the minimum exponent in the model of the
type of **x**.

### **Options**

- **x**
  : A value used to select the kind of _real_ to return a value for.

### **Result**

The value returned is the maximum exponent for the kind of the value
queried

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

Fortran 95

### **See Also**

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
