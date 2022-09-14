## tan

### **Name**

**tan**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Tangent function

### **Syntax**

```fortran
result = tan(x)
```

### **Description**

**tan(x)** computes the tangent of **x**.

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_.

### **Returns**

The return value has the same type and kind as **x**.

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

FORTRAN 77 and later. For a complex argument, Fortran 2008 or later.

### **See Also**

[**atan**(3)](ATAN),
[**cos**(3)](COS),
[**sin**(3)](SIN)

_fortran-lang intrinsic descriptions_
