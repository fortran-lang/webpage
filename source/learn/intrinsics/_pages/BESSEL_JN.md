(bessel_jn)=
## bessel_jn

### **Name**

**bessel_jn**(3) - \[MATHEMATICS\] Bessel function of the first kind

### **Synopsis**

```fortran
    result = bessel_jn(n, x)
```

```fortran
     elemental real(kind=KIND) function bessel_jn(n,x)

      integer(kind=**),intent(in) :: n
      real(kind=KIND),intent(in) :: x
```

- KIND may be any valid value for type _real_
- **x** is _real_
- The return value has the same type and kind as **x**.

```fortran
    result = bessel_jn(n1, n2, x)
```

```fortran
     real(kind=KIND) function bessel_jn(n1, n2, ,x)

     integer(kind=**),intent(in) :: n1
     integer(kind=**),intent(in) :: n2
     real(kind=KIND),intent(in) :: x
```

- **n1** is _integer_
- **n2** is _integer_
- **x** is _real_
- The return value has the same type and kind as **x**.

### **Description**

**bessel_jn( n, x )** computes the Bessel function of the first kind of
order **n** of **x**.

**bessel_jn(n1, n2, x)** returns an array with the Bessel
function\|Bessel functions of the first kind of the orders **n1**
to **n2**.

### **Options**

- **n**
  : a non-negative scalar integer..

- **n1**
  : a non-negative scalar _integer_.

- **n2**
  : a non-negative scalar _integer_.

- **x**
  : Shall be a scalar for **bessel_jn(n,x)** or an array
  For **bessel_jn(n1, n2, x)**.

### **Result**

The result value of BESSEL_JN (N, X) is a processor-dependent
approximation to the Bessel function of the first kind and order N
of X.

The result of BESSEL_JN (N1, N2, X) is a rank-one array with extent
MAX (N2-N1+1, 0). Element i of the result value of BESSEL_JN (N1,
N2, X) is a processor-dependent approximation to the Bessel function
of the first kind and order N1+i-1 of X.

### **Examples**

Sample program:

```fortran
program demo_bessel_jn
use, intrinsic :: iso_fortran_env, only : real_kinds, &
   & real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
    x = bessel_jn(5,x)
    write(*,*)x
end program demo_bessel_jn
```

Results:

```text
      2.4975773021123450E-004
```

### **Standard**

Fortran 2008

### **See Also**

[**bessel_j0**(3)](#bessel_j0),
[**bessel_j1**(3)](#bessel_j1),
[**bessel_y0**(3)](#bessel_y0),
[**bessel_y1**(3)](#bessel_y1),
[**bessel_yn**(3)](#bessel_yn)

_fortran-lang intrinsic descriptions_
