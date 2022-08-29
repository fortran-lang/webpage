## bessel_y1

### **Name**

**bessel_y1**(3) - \[MATHEMATICS\] Bessel function of the second kind of order 1

### **Syntax**

```fortran
    result = bessel_y1(x)
```

### **Description**

**bessel_y1(x)** computes the Bessel function of the second
kind of order 1 of **x**.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is _real_. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besy1
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
  real(kind=real64) :: x = 1.0_real64
  write(*,*)x, bessel_y1(x)
end program demo_besy1
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j0**(3)](BESSEL_J0),
[**bessel_j1**(3)](BESSEL_J1),
[**bessel_jn**(3)](BESSEL_JN),
[**bessel_y0**(3)](BESSEL_Y0),
[**bessel_yn**(3)](BESSEL_YN)

###### fortran-lang intrinsic descriptions
