(set_exponent)=
## set_exponent

### **Name**

**set_exponent**(3) - \[MODEL_COMPONENTS\] real value with specified exponent

### **Synopsis**

```fortran
    result = set_exponent(x, i)
```

```fortran
     elemental real(kind=KIND) function set_exponent(x,i)

      real(kind=KIND),intent(in) :: x
      integer(kind=**),intent(in) :: i
```

### **Characteristics**

- **x** is type _real_
- **i** is type _integer_
- a kind designated as \*\* may be any supported kind for the type

- The return value is of the same type and kind as **x**.

### **Description**

**set_exponent**(3) returns the real number whose fractional part is
that of **x** and whose exponent part is **i**.

### **Options**

- **x**
  : Shall be of type _real_.

- **i**
  : Shall be of type _integer_.

### **Result**

The return value is of the same type and kind as **x**. The real number
whose fractional part is that of **x** and whose exponent part
if **i** is returned; it is **fraction(x) \* radix(x)\*\*i**.

If **x** has the value zero, the result has the same value as **x**.

If **x** is an IEEE infinity, the result is an IEEE NaN.

If **x** is an IEEE NaN, the result is the same NaN.

### **Examples**

Sample program:

```fortran
program demo_setexp
implicit none
real :: x = 178.1387e-4
integer :: i = 17
   print *, set_exponent(x, i), fraction(x) * radix(x)**i
end program demo_setexp
```

Results:

```text
      74716.7891       74716.7891
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
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions_
