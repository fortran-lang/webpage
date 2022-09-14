## bessel_yn

### **Name**

**bessel_yn**(3) - \[MATHEMATICS\] Bessel function of the second kind

### **Syntax**

```fortran
  result = bessel_yn(n, x)

  result = bessel_yn(n1, n2, x)
```

### **Description**

**bessel_yn(n, x)** computes the Bessel function of the second
kind of order **n** of **x**. If **n** and **x** are arrays, their ranks and shapes
shall conform.

**bessel_yn(n1, n2, x)** returns an array with the Bessel
function\|Bessel functions of the first kind of the orders **n1** to **n2**.

### **Arguments**

- **n**
  : Shall be a scalar or an array of type _integer_.

- **n1**
  : Shall be a non-negative scalar of type _integer_.

- **n2**
  : Shall be a non-negative scalar of type _integer_.

- **x**
  : Shall be a scalar or an array of type _real_; for
  **bessel_yn(n1, n2, x)** it shall be scalar.

### **Returns**

The return value is _real_. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besyn
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
  write(*,*) x,bessel_yn(5,x)
end program demo_besyn
```

Results:

```text
      1.0000000000000000       -260.40586662581222
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j0**(3)](BESSEL_J0),
[**bessel_j1**(3)](BESSEL_J1),
[**bessel_jn**(3)](BESSEL_JN),
[**bessel_y0**(3)](BESSEL_Y0),
[**bessel_y1**(3)](BESSEL_Y1)

_fortran-lang intrinsic descriptions_
