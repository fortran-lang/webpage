(scale)=
## scale

### **Name**

**scale**(3) - \[MODEL_COMPONENTS\] Scale a real value by a whole power of the radix

### **Synopsis**

```fortran
    result = scale(x, i)
```

```fortran
     elemental real(kind=KIND) function scale(x, i)

      real(kind=KIND),intent(in)   :: x
      integer(kind=**),intent(in)  :: i
```

### **Characteristics**

- **x** is type _real_ of any kind
- **i** is type an _integer_ of any kind
- the result is _real_ of the same kind as **x**

### **Description**

**scale**(3) returns x \* **radix(x)\*\*i**.

It is almost certain the radix(base) of the platform is two, therefore
**scale**(3) is generally the same as **x\*2\*\*i**

### **Options**

- **x**
  : the value to multiply by **radix(x)\*\*i**. Its type and kind is used
  to determine the radix for values with its characteristics and determines
  the characteristics of the result, so care must be taken the returned
  value is within the range of the characteristics of **x**.

- **i**
  : The power to raise the radix of the machine to

### **Result**

The return value is **x \* radix(x)\*\*i**, assuming that value can be
represented by a value of the type and kind of **x**.

### **Examples**

Sample program:

```fortran
program demo_scale
implicit none
real :: x = 178.1387e-4
integer :: i = 5
   print *, scale(x,i), x*radix(x)**i
end program demo_scale
```

Results:

```
    0.570043862      0.570043862
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
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
