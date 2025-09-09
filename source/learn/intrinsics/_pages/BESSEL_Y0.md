(bessel_y0)=
## bessel_y0

### **Name**

**bessel_y0**(3) - \[MATHEMATICS\] Bessel function of the second kind of order 0

### **Synopsis**

```fortran
    result = bessel_y0(x)
```

```fortran
     elemental real(kind=KIND) function bessel_y0(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- KIND may be any supported _real_ KIND.
- the result characteristics (type, kind) are the same as **x**

### **Description**

**bessel_y0**(3) computes the Bessel function of the second
kind of order 0 of **x**.

### **Options**

- **x**
  : The type shall be _real_.
  Its value shall be greater than zero.

### **Result**

The return value is of type _real_. It has the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_bessel_y0
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
  real(kind=real64) :: x = 0.0_real64
  x = bessel_y0(x)
  write(*,*)x
end program demo_bessel_y0
```

Results:

```text
                    -Infinity
```

### **Standard**

Fortran 2008

### **See Also**

[**bessel_j0**(3)](#bessel_j0),
[**bessel_j1**(3)](#bessel_j1),
[**bessel_jn**(3)](#bessel_jn),
[**bessel_y1**(3)](#bessel_y1),
[**bessel_yn**(3)](#bessel_yn)

_fortran-lang intrinsic descriptions_
