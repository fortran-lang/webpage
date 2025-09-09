(bessel_j0)=
## bessel_j0

### **Name**

**bessel_j0**(3) - \[MATHEMATICS\] Bessel function of the first kind of order 0

### **Synopsis**

```fortran
    result = bessel_j0(x)
```

```fortran
     elemental real(kind=KIND) function bessel_j0(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- KIND may be any KIND supported by the _real_ type.
- The result is the same type and kind as **x**.

### **Description**

**bessel_j0**(3) computes the Bessel function of the first kind
of order **0** of **x**.

### **Options**

- **x**
  : The value to operate on.

### **Result**

the Bessel function of the first kind of order **0** of **x**.
The result lies in the range **-0.4027 \<= bessel(0,x) \<= 1**.

### **Examples**

Sample program:

```fortran
program demo_bessel_j0
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
   implicit none
   real(kind=real64) :: x
   x = 0.0_real64
   x = bessel_j0(x)
   write(*,*)x
end program demo_bessel_j0
```

Results:

```text
      1.0000000000000000
```

### **Standard**

Fortran 2008

### **See Also**

[**bessel_j1**(3)](#bessel_j1),
[**bessel_jn**(3)](#bessel_jn),
[**bessel_y0**(3)](#bessel_y0),
[**bessel_y1**(3)](#bessel_y1),
[**bessel_yn**(3)](#bessel_yn)

_fortran-lang intrinsic descriptions_
