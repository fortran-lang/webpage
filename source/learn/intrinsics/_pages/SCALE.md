## scale

### **Name**

**scale**(3) - \[MODEL_COMPONENTS\] Scale a real value by a whole power of the radix

### **Syntax**

```fortran
result = scale(x, i)

   real(kind=KIND),intent(in) :: x
   integer,intent(in)         :: i
```

### **Description**

**scale(x,i)** returns x \* **radix(x)\*\*i**.

### **Arguments**

- **x**
  : The type of the argument shall be a _real_.

- **i**
  : The type of the argument shall be a _integer_.

### **Returns**

The return value is of the same type and kind as **x**. Its value is
**x \* radix(x)\*\*i**.

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
[**set_exponent**(3)](SET_EXPONENT),
[**spacing**(3)](SPACING),
[**tiny**(3)](TINY)

###### fortran-lang intrinsic descriptions
