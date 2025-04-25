(cosh)=
## cosh

### **Name**

**cosh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Hyperbolic cosine function

### **Synopsis**

```fortran
    result = cosh(x)
```

```fortran
     elemental TYPE(kind=KIND) function cosh(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **TYPE** may be _real_ or _complex_ of any kind.
- The returned value will be of the same type and kind as the argument.

### **Description**

**cosh**(3) computes the hyperbolic cosine of **x**.

If **x** is of type complex its imaginary part is regarded as a value
in radians.

### **Options**

- **x**
  : the value to compute the hyperbolic cosine of

### **Result**

If **x** is _complex_, the imaginary part of the result is in radians.

If **x** is _real_, the return value has a lower bound of one,
**cosh(x) \>= 1**.

### **Examples**

Sample program:

```fortran
program demo_cosh
use, intrinsic :: iso_fortran_env, only : &
 & real_kinds, real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
    write(*,*)'X=',x,'COSH(X=)',cosh(x)
end program demo_cosh
```

Results:

```text
 >  X=   1.00000000000000      COSH(X=)   1.54308063481524
```

### **Standard**

FORTRAN 77 , for a complex argument - Fortran 2008

### **See Also**

Inverse function: [**acosh**(3)](#acosh)

### **Resources**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

_fortran-lang intrinsic descriptions_
