(digits)=
## digits

### **Name**

**digits**(3) - \[NUMERIC MODEL\] Significant digits in the numeric model

### **Synopsis**

```fortran
    result = digits(x)
```

```fortran
     integer function digits(x)

      TYPE(kind=KIND),intent(in) :: x(..)
```

### **Characteristics**

- **x** an _integer_ or _real_ scalar or array

- The return value is an _integer_ of default kind.

### **Description**

**digits**(3) returns the number of significant digits of the internal
model representation of **x**. For example, on a system using a 32-bit
floating point representation, a default real number would likely
return 24.

### **Options**

- **x**
  : a value of the type and kind to query

### **Result**

The number of significant digits in a variable of the type and kind
of **x**.

### **Examples**

Sample program:

```fortran
program demo_digits
implicit none
integer :: i = 12345
real :: x = 3.143
doubleprecision :: y = 2.33d0
   print *,'default integer:', digits(i)
   print *,'default real:   ', digits(x)
   print *,'default doubleprecision:', digits(y)
end program demo_digits
```

Results:

```text
 >  default integer:          31
 >  default real:             24
 >  default doubleprecision:          53
```

### **Standard**

Fortran 95

### **See Also**

[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
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
