## tiny

### **Name**

**tiny**(3) - \[NUMERIC MODEL\] Smallest positive number of a real kind

### **Syntax**

```fortran
result = tiny(x)
   real(kind=KIND) function(x)
   real(kind=KIND) :: x
```

where KIND may be any kind supported by type _real_

### **Description**

**tiny(x)** returns the smallest positive (non zero) number of the type
and kind of **x**.

### **Arguments**

- **x**
  : Shall be of type _real_.

### **Returns**

The smallest positive value for the _real_ type of the specified kind.

The return value is of the same type and kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_tiny
implicit none
   print *, 'default real is from',tiny(0.0) ,'to',huge(0.0)
   print *, 'doubleprecision is from ',tiny(0.0d0),'to',huge(0.0d0)
end program demo_tiny
```

Results:

```text
 default real is from 1.17549435E-38 to 3.40282347E+38
 doubleprecision is from 2.2250738585072014E-308 to 1.7976931348623157E+308
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
[**spacing**(3)](SPACING)

###### fortran-lang intrinsic descriptions
