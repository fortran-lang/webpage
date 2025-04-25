(tiny)=
## tiny

### **Name**

**tiny**(3) - \[NUMERIC MODEL\] Smallest positive number of a real kind

### **Synopsis**

```fortran
    result = tiny(x)
```

```fortran
     real(kind=KIND) function tiny(x)

      real(kind=KIND) :: x
```

### **Characteristics**

- **x** may be any _real_ scalar or array
- the result has the same type and kind as **x**

### **Description**

**tiny**(3) returns the smallest positive (non zero) number of the
type and kind of **x**.

For real **x**

```fortran
   result = 2.0**(minexponent(x)-1)
```

### **Options**

- **x**
  : The value whose kind is used to determine the model type to query

### **Result**

The smallest positive value for the _real_ type of the specified kind.

### **Examples**

Sample program:

```fortran
program demo_tiny
implicit none
   print *, 'default real is from', tiny(0.0), 'to',huge(0.0)
   print *, 'doubleprecision is from ', tiny(0.0d0), 'to',huge(0.0d0)
end program demo_tiny
```

Results:

```text
 default real is from 1.17549435E-38 to 3.40282347E+38
 doubleprecision is from 2.2250738585072014E-308 to
 1.7976931348623157E+308
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
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
