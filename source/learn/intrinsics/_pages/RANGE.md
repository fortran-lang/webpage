(range)=
## range

### **Name**

**range**(3) - \[NUMERIC MODEL\] Decimal exponent range of a numeric kind

### **Synopsis**

```fortran
    result = range(x)
```

```fortran
      integer function range (x)

       TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** may be of type _integer_, _real_, or _complex_. It may be a scalar or an array.
- **KIND** is any kind supported by the type of **x**
- the result is a default _integer_ scalar

### **Description**

**range**(3) returns the decimal exponent range in the model of the
type of **x**.

Since **x** is only used to determine the type and kind being
interrogated, the value need not be defined.

### **Options**

- **x**
  : the value whose type and kind are used for the query

### **Result**

Case (i)
: For an integer argument, the result has the value

```fortran
    int (log10 (huge(x)))
```

Case (ii)
: For a real argument, the result has the value

```fortran
     int(min (log10 (huge(x)), -log10(tiny(x) )))
```

Case (iii)
: For a complex argument, the result has the value

```fortran
    range(real(x))
```

### **Examples**

Sample program:

```fortran
program demo_range
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp)    :: x(2)
complex(kind=dp) :: y
   print *, precision(x), range(x)
   print *, precision(y), range(y)
end program demo_range
```

Results:

```text
 >            6          37
 >           15         307
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
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
