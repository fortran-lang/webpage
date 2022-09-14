## radix

### **Name**

**radix**(3) - \[NUMERIC MODEL\] Base of a model number

### **Syntax**

```fortran
result = radix(x)
```

### **Description**

**radix(x)** returns the base of the model representing the entity **x**.

### **Arguments**

- **x**
  : Shall be of type _integer_ or _real_

### **Returns**

The return value is a scalar of type _integer_ and of the default integer
kind.

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
    The radix for the default integer kind is           2
    The radix for the default real kind is           2
    The radix for the doubleprecision real kind is          2
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
[**range**(3)](RANGE),
[**rrspacing**(3)](RRSPACING),
[**scale**(3)](SCALE),
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

_fortran-lang intrinsic descriptions_
