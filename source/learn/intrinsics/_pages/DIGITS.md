## digits

### **Name**

**digits**(3) - \[NUMERIC MODEL\] Significant digits function

### **Syntax**

```fortran
result = digits(x)
    function digits(x)
    type(integer(kind=kind(0)))      :: digits
    type(TYPE(kind=KIND)),intent(in) :: x(..)
```

where TYPE may be _integer_ or _real_ and KIND is any kind supported by
TYPE.

### **Description**

**digits(x)** returns the number of significant digits of the internal
model representation of **x**. For example, on a system using a 32-bit
floating point representation, a default real number would likely return 24.

### **Arguments**

- **x**
  : The type may be a scalar or array of type _integer_ or _real_.

### **Returns**

The return value is of type _integer_ of default kind.

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

Typical Results:

```
    default integer:                  31
    default real:                     24
    default doubleprecision:          53
```

### **Standard**

Fortran 95 and later

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
