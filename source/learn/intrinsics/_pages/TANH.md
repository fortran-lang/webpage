(tanh)=
## tanh

### **Name**

**tanh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Hyperbolic tangent function

### **Synopsis**

```fortran
    result = tanh(x)
```

```fortran
     elemental TYPE(kind=KIND) function tanh(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** may be _real_ or _complex_ and any associated kind supported by
  the processor.
- The returned value will be of the same type and kind as the argument.

### **Description**

**tanh**(3) computes the hyperbolic tangent of **x**.

### **Options**

- **x**
  : The value to compute the Hyperbolic tangent of.

### **Result**

Returns the hyperbolic tangent of **x**.

If **x** is _complex_, the imaginary part of the result is regarded as
a radian value.

If **x** is _real_, the return value lies in the range

```
      -1 <= tanh(x) <= 1.
```

### **Examples**

Sample program:

```fortran
program demo_tanh
use, intrinsic :: iso_fortran_env, only : &
& real_kinds, real32, real64, real128
implicit none
real(kind=real64) :: x = 2.1_real64
   write(*,*)x, tanh(x)
end program demo_tanh
```

Results:

```text
      2.1000000000000001       0.97045193661345386
```

### **Standard**

FORTRAN 77 , for a complex argument Fortran 2008

### **See Also**

[**atanh**(3)](#atanh)

### **Resources**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

_fortran-lang intrinsic descriptions_
