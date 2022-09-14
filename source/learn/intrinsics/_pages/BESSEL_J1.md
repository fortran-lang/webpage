## bessel_j1

### **Name**

**bessel_j1**(3) - \[MATHEMATICS\] Bessel function of the first kind of order 1

### **Syntax**

```fortran
    result = bessel_j1(x)
```

### **Description**

**bessel_j1(x)** computes the Bessel function of the first kind
of order **1** of **x**.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type _real_ and lies in the range
**-0.5818 \<= bessel(0,x) \<= 0.5818** . It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besj1
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
   x = bessel_j1(x)
   write(*,*)x
end program demo_besj1
```

Results:

```text
     0.44005058574493350
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j0**(3)](BESSEL_J0),
[**bessel_jn**(3)](BESSEL_JN),
[**bessel_y0**(3)](BESSEL_Y0),
[**bessel_y1**(3)](BESSEL_Y1),
[**bessel_yn**(3)](BESSEL_YN)

_fortran-lang intrinsic descriptions_
