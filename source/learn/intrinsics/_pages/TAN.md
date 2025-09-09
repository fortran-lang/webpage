(tan)=
## tan

### **Name**

**tan**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Tangent function

### **Synopsis**

```fortran
result = tan(x)
```

```fortran
 elemental TYPE(kind=KIND) function tan(x)

  TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- the **TYPE** of **x** may be _real_ or _complex_ of any supported kind
- The returned value will be of the same type and kind as the argument
  **x**.

### **Description**

**tan**(3) computes the tangent of **x**.

### **Options**

- **x**
  : The angle in radians to compute the tangent of for _real_ input.
  If **x** is of type _complex_, its real part is regarded as a value
  in radians.

### **Result**

The return value is the tangent of the value **x**.

### **Examples**

Sample program:

```fortran
program demo_tan
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
real(kind=real64) :: x = 0.165_real64
     write(*,*)x, tan(x)
end program demo_tan
```

Results:

```text
     0.16500000000000001       0.16651386310913616
```

### **Standard**

FORTRAN 77 . For a complex argument, Fortran 2008 .

### **See Also**

[**atan**(3)](#atan),
[**atan2**(3)](#atan2),
[**cos**(3)](#cos),
[**sin**(3)](#sin)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
