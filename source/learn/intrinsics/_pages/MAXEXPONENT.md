(maxexponent)=
## maxexponent

### **Name**

**maxexponent**(3) - \[NUMERIC MODEL\] Maximum exponent of a real kind

### **Synopsis**

```fortran
    result = maxexponent(x)
```

```fortran
     elemental integer function maxexponent(x)

      real(kind=**),intent(in)   :: x
```

### **Characteristics**

- **x** is a _real_ scalar or array of any _real_ kind
- the result is a default _integer_ scalar

### **Description**

**maxexponent**(3) returns the maximum exponent in the model of the
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
program demo_maxexponent
use, intrinsic :: iso_fortran_env, only : real32,real64,real128
implicit none
character(len=*),parameter :: g='(*(g0,1x))'
   print  g,  minexponent(0.0_real32),   maxexponent(0.0_real32)
   print  g,  minexponent(0.0_real64),   maxexponent(0.0_real64)
   print  g,  minexponent(0.0_real128),  maxexponent(0.0_real128)
end program demo_maxexponent
```

Results:

```text
   -125 128
   -1021 1024
   -16381 16384
```

### **Standard**

Fortran 95

### **See Also**

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**minexponent**(3)](#minexponent),
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
