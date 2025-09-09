(acosh)=
## acosh

### **Name**

**acosh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Inverse hyperbolic cosine function

### **Synopsis**

```fortran
    result = acosh(x)
```

```fortran
     elemental TYPE(kind=KIND) function acosh(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **TYPE** may be _real_ or _complex_
- **KIND** may be any kind supported by the associated type.
- The returned value will be of the same type and kind as the argument.

### **Description**

**acosh**(3) computes the inverse hyperbolic cosine of **x** in radians.

### **Options**

- **x**
  : The value to compute the hyperbolic cosine of

### **Result**

The result has a value equal to a processor-dependent approximation to
the inverse hyperbolic cosine function of X.

If **x** is _complex_, the imaginary part of the result is in radians
and lies between

```fortran
 0 <= aimag(acosh(x)) <= PI
```

### **Examples**

Sample program:

```fortran
program demo_acosh
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=dp), dimension(3) :: x = [ 1.0d0, 2.0d0, 3.0d0 ]
   write (*,*) acosh(x)
end program demo_acosh
```

Results:

```text
 0.000000000000000E+000   1.31695789692482        1.76274717403909
```

### **Standard**

Fortran 2008

### **See Also**

Inverse function: [**cosh**(3)](#cosh)

### **Resources**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
