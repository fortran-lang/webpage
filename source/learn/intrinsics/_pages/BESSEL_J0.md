## bessel_j0

### **Name**

**bessel_j0**(3) - \[MATHEMATICS\] Bessel function of the first kind of order 0

### **Syntax**

```fortran
    result = bessel_j0(x)
```

### **Description**

**bessel_j0(x)** computes the Bessel function of the first kind
of order **0** of **x**.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type _real_ and lies in the range
**-0.4027 \<= bessel(0,x) \<= 1**. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_besj0
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
   implicit none
   real(kind=real64) :: x = 0.0_real64
   x = bessel_j0(x)
   write(*,*)x
end program demo_besj0
```

Results:

```text
      1.0000000000000000
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**bessel_j1**(3)](#bessel_j1),
[**bessel_jn**(3)](#bessel_jn),
[**bessel_y0**(3)](#bessel_y0),
[**bessel_y1**(3)](#bessel_y1),
[**bessel_yn**(3)](#bessel_yn)

 _fortran-lang intrinsic descriptions_
