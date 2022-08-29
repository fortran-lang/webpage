## acosh

### **Name**

**acosh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Inverse hyperbolic cosine function

### **Syntax**

```fortran
  result = acosh(x)

   TYPE(kind=KIND),elemental :: acosh

   TYPE(kind=KIND,intent(in) :: x
```

where TYPE may be _real_ or _complex_ and KIND may be any KIND supported
by the associated type.

### **Description**

**acosh(x)** computes the inverse hyperbolic cosine of **x** in radians.

### **Arguments**

- **x**
  : the type shall be _real_ or _complex_.

### **Returns**

The return value has the same type and kind as **x**.

If **x** is _complex_, the imaginary part of the result is in radians and
lies between

> **0 \<= aimag(acosh(x)) \<= PI**

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

Fortran 2008 and later

### **See Also**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

Inverse function: [**cosh**(3)](COSH)

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
