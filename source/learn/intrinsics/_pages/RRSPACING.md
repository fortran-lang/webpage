(rrspacing)=
## rrspacing

### **Name**

**rrspacing**(3) - \[MODEL_COMPONENTS\] Reciprocal of the relative spacing of a numeric type

### **Synopsis**

```fortran
    result = rrspacing(x)
```

```fortran
     elemental real(kind=KIND) function rrspacing(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** is type _real_ an any kind
- The return value is of the same type and kind as **x**.

### **Description**

**rrspacing**(3) returns the reciprocal of the relative spacing of model
numbers near **x**.

<!--
 5 Result Value. The result has the value |Y* b-e|*bp = ABS (FRACTION (Y)) * RADIX (X) / EPSILON (X),
    where b, e, and p are as defined in 16.4 for Y, the value nearest to X in the model for real values whose kind type
    parameter is that of X; if there are two such values, the value of greater absolute value is taken. If X is an IEEE
    infinity, the result is an IEEE NaN. If X is an IEEE NaN, the result is that NaN.
 6 Example. RRSPACING (-3.0) has the value 0:75x224 for reals whose model is as in 16.4, NOTE 1.
-->

### **Options**

- **x**
  : Shall be of type _real_.

### **Result**

The return value is of the same type and kind as **x**. The value returned
is equal to **abs(fraction(x)) \* float(radix(x))\*\*digits(x)**.

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
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions_
