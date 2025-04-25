(radix)=
## radix

### **Name**

**radix**(3) - \[NUMERIC MODEL\] Base of a numeric model

### **Synopsis**

```fortran
   result = radix(x)
```

```fortran
    integer function radix(x)

     TYPE(kind=**),intent(in) :: x(..)
```

### **Characteristics**

- **x** may be scalar or an array of any _real_ or _integer_ type.
- the result is a default integer scalar.

### **Description**

**radix**(3) returns the base of the internal model representing the
numeric entity **x**.

In a positional numeral system, the radix or base is the number of
unique digits, including the digit zero, used to represent numbers.

This function helps to represent the internal computing model
generically, but will be 2 (representing a binary machine) for any
common platform for all the numeric types.

### **Options**

- **x**
  : used to identify the type of number to query.

### **Result**

The returned value indicates what base is internally used to represent
the type of numeric value **x** represents.

### **Examples**

Sample program:

```fortran
program demo_radix
implicit none
   print *, "The radix for the default integer kind is", radix(0)
   print *, "The radix for the default real kind is", radix(0.0)
   print *, "The radix for the doubleprecision real kind is", radix(0.0d0)
end program demo_radix
```

Results:

```text
 >  The radix for the default integer kind is           2
 >  The radix for the default real kind is           2
 >  The radix for the doubleprecision real kind is           2
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
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
