(bessel_j1)=
## bessel_j1

### **Name**

**bessel_j1**(3) - \[MATHEMATICS\] Bessel function of the first kind of order 1

### **Synopsis**

```fortran
    result = bessel_j1(x)
```

```fortran
     elemental real(kind=KIND) function bessel_j1(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- KIND may be any supported _real_ KIND.
- the result is of the same type and kind as **x**

### **Description**

**bessel_j1**(3) computes the Bessel function of the first kind
of order **1** of **x**.

### **Options**

- **x**
  : The type shall be _real_.

### **Result**

The return value is of type _real_ and lies in the range
**-0.5818 \<= bessel(0,x) \<= 0.5818** . It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_bessel_j1
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
   x = bessel_j1(x)
   write(*,*)x
end program demo_bessel_j1
```

Results:

```text
     0.44005058574493350
```

### **Standard**

Fortran 2008

### **See Also**

[**bessel_j0**(3)](#bessel_j0),
[**bessel_jn**(3)](#bessel_jn),
[**bessel_y0**(3)](#bessel_y0),
[**bessel_y1**(3)](#bessel_y1),
[**bessel_yn**(3)](#bessel_yn)

_fortran-lang intrinsic descriptions_
