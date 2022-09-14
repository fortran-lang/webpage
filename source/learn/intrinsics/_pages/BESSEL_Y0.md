## bessel_y0

### **Name**

**bessel_y0**(3) - \[MATHEMATICS\] Bessel function of the second kind of order 0

### **Syntax**

```fortran
    result = bessel_y0(x)
```

### **Description**

**bessel_y0(x)** computes the Bessel function of the second
kind of order 0 of **x**.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type _real_. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besy0
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
  real(kind=real64) :: x = 0.0_real64
  x = bessel_y0(x)
  write(*,*)x
end program demo_besy0
```

Results:

```text
                    -Infinity
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j0**(3)](BESSEL_J0),
[**bessel_j1**(3)](BESSEL_J1),
[**bessel_jn**(3)](BESSEL_JN),
[**bessel_y1**(3)](BESSEL_Y1),
[**bessel_yn**(3)](BESSEL_YN)

_fortran-lang intrinsic descriptions_
