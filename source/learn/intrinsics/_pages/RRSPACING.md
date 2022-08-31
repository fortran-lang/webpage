## rrspacing

### **Name**

**rrspacing**(3) - \[MODEL_COMPONENTS\] Reciprocal of the relative spacing

### **Syntax**

```fortran
result = rrspacing(x)
```

### **Description**

**rrspacing(x)** returns the reciprocal of the relative spacing of model
numbers near **x**.

### **Arguments**

- **x**
  : Shall be of type _real_.

### **Returns**

The return value is of the same type and kind as **x**. The value returned
is equal to **abs(fraction(x)) \* float(radix(x))\*\*digits(x)**.

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
[**scale**(3)](SCALE),
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

###### fortran-lang intrinsic descriptions
