## bessel_jn

### **Name**

**bessel_jn**(3) - \[MATHEMATICS\] Bessel function of the first kind

### **Syntax**

```fortran
  result = bessel_jn(n, x)

  result = bessel_jn(n1, n2, x)
```

### **Description**

**bessel_jn(n, x)** computes the Bessel function of the first
kind of order **n** of **x**. If **n** and **x** are arrays, their ranks and shapes
shall conform.

**bessel_jn(n1, n2, x)** returns an array with the Bessel function\|Bessel functions
of the first kind of the orders **n1** to **n2**.

### **Arguments**

- **n**
  : Shall be a scalar or an array of type _integer_.

- **n1**
  : Shall be a non-negative scalar of type _integer_.

- **n2**
  : Shall be a non-negative scalar of type _integer_.

- **x**
  : Shall be a scalar or an array of type _real_. For
  **bessel_jn(n1, n2, x)** it shall be scalar.

### **Returns**

The return value is a scalar of type _real_. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besjn
use, intrinsic :: iso_fortran_env, only : real_kinds, &
   & real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
    x = bessel_jn(5,x)
    write(*,*)x
end program demo_besjn
```

Results:

```text
      2.4975773021123450E-004
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j0**(3)](BESSEL_J0),
[**bessel_j1**(3)](BESSEL_J1),
[**bessel_y0**(3)](BESSEL_Y0),
[**bessel_y1**(3)](BESSEL_Y1),
[**bessel_yn**(3)](BESSEL_YN)

_fortran-lang intrinsic descriptions_
