(precision)=
## precision

### **Name**

**precision**(3) - \[NUMERIC MODEL\] Decimal precision of a real kind

### **Synopsis**

```fortran
    result = precision(x)
```

```fortran
     integer function precision(x)

      TYPE(kind=**),intent(in) :: x
```

### **Characteristics**

- **x** shall be of type _real_ or _complex_. It may be a scalar or an array.
- the result is a default _integer_ scalar.

### **Description**

**precision**(3) returns the decimal precision in the model of the type
of **x**.

### **Options**

- **x**
  : the type and kind of the argument are used to determine which number
  model to query. The value of the argument is not unused; it may even
  be undefined.

### **Result**

The precision of values of the type and kind of **x**

<!--
   Result Value. The result has the value INT ((p - 1) * LOG10 (b)) + k, where b and p are as defined in 16.4
   for the model representing real numbers with the same value for the kind type parameter as X, and where k is 1
   if b is an integral power of 10 and 0 otherwise.
-->

### **Examples**

Sample program:

```fortran
program demo_precision
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp)    :: x(2)
complex(kind=dp) :: y

   print *, precision(x), range(x)
   print *, precision(y), range(y)

end program demo_precision
```

Results:

```text
  >           6          37
  >          15         307
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
[**nearest**(3)](#nearest),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
