(log)=
## log

### **Name**

**log**(3) - \[MATHEMATICS\] Natural logarithm

### **Synopsis**

```fortran
  result = log(x)
```

```fortran
   elemental TYPE(kind=KIND) function log(x)

    TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** may be any _real_ or _complex_ kind.
- the result is the same type and characteristics as **x**.

### **Description**

**log**(3) computes the natural logarithm of **x**, i.e. the logarithm to
the base "e".

### **Options**

- **x**
  : The value to compute the natural log of.
  If **x** is _real_, its value shall be greater than zero.
  If **x** is _complex_, its value shall not be zero.

### **Result**

The natural logarithm of **x**.
If **x** is the _complex_ value **(r,i)** , the imaginary part "i" is in the range

```fortran
    -PI < i <= PI
```

If the real part of **x** is less than zero and the imaginary part of
**x** is zero, then the imaginary part of the result is approximately
**PI** if the imaginary part of **PI** is positive real zero or the
processor does not distinguish between positive and negative real zero,
and approximately **-PI** if the imaginary part of **x** is negative
real zero.

### **Examples**

Sample program:

```fortran
program demo_log
implicit none
  real(kind(0.0d0)) :: x = 2.71828182845904518d0
  complex :: z = (1.0, 2.0)
  write(*,*)x, log(x)    ! will yield (approximately) 1
  write(*,*)z, log(z)
end program demo_log
```

Results:

```text
      2.7182818284590451        1.0000000000000000
   (1.00000000,2.00000000) (0.804718971,1.10714877)
```

### **Standard**

FORTRAN 77

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
