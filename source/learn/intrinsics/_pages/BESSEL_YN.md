(bessel_yn)=
## bessel_yn

### **Name**

**bessel_yn**(3) - \[MATHEMATICS\] Bessel function of the second kind

### **Synopsis**

```fortran
    result = bessel_yn(n, x)
```

```fortran
     elemental real(kind=KIND) function bessel_yn(n,x)

      integer(kind=**),intent(in) :: n
      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **n** is _integer_
- **x** is _real_
- The return value has the same type and kind as **x**.

```fortran
    result = bessel_yn(n1, n2, x)
```

```fortran
     real(kind=KIND) function bessel_yn(n1, n2, ,x)

      integer(kind=**),intent(in) :: n1
      integer(kind=**),intent(in) :: n2
      real(kind=KIND),intent(in) :: x
```

- **n1** is _integer_
- **n2** is _integer_
- **x** is _real_
- The return value has the same type and kind as **x**.

### **Description**

**bessel_yn(n, x)** computes the Bessel function of the second kind
of order **n** of **x**.

**bessel_yn(n1, n2, x)** returns an array with the Bessel
function\|Bessel functions of the first kind of the orders **n1**
to **n2**.

### **Options**

- **n**
  : Shall be a scalar or an array of type _integer_ and non-negative.

- **n1**
  : Shall be a non-negative scalar of type _integer_ and non-negative.

- **n2**
  : Shall be a non-negative scalar of type _integer_ and non-negative.

- **x**
  : A _real_ non-negative value. Note **bessel_yn(n1, n2, x)** is not
  elemental, in which case it must be a scalar.

### **Result**

The result value of BESSEL_YN (N, X) is a processor-dependent
approximation to the Bessel function of the second kind and order N
of X.

The result of **BESSEL_YN (N1, N2, X)** is a rank-one array with extent
**MAX (N2-N1+1, 0)**. Element i of the result value of BESSEL_YN
(N1, N2, X) is a processor-dependent approximation to the Bessel
function of the second kind and order N1+i-1 of X.

### **Examples**

Sample program:

```fortran
program demo_bessel_yn
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
real(kind=real64) :: x = 1.0_real64
  write(*,*) x,bessel_yn(5,x)
end program demo_bessel_yn
```

Results:

```text
      1.0000000000000000       -260.40586662581222
```

### **Standard**

Fortran 2008

### **See Also**

[**bessel_j0**(3)](#bessel_j0),
[**bessel_j1**(3)](#bessel_j1),
[**bessel_jn**(3)](#bessel_jn),
[**bessel_y0**(3)](#bessel_y0),
[**bessel_y1**(3)](#bessel_y1)

_fortran-lang intrinsic descriptions_
