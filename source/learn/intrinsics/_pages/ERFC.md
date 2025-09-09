(erfc)=
## erfc

### **Name**

**erfc**(3) - \[MATHEMATICS\] Complementary error function

### **Synopsis**

```fortran
    result = erfc(x)
```

```fortran
     elemental real(kind=KIND) function erfc(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** is of type _real_ and any valid kind
- **KIND** is any value valid for type _real_
- the result has the same characteristics as **x**

### **Description**

**erfc**(3) computes the complementary error function of **x**. Simply
put this is equivalent to **1 - erf(x)**, but **erfc** is provided
because of the extreme loss of relative accuracy if **erf(x)** is
called for large **x** and the result is subtracted from **1**.

**erfc(x)** is defined as

<!--
$$
\text{erfc}(x) = 1 - \text{erf}(x) = 1 - \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt.
$$
-->

$$
\text{erfc}(x) = 1 - \text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_x^{\infty} e^{-t^2} dt.
$$

### **Options**

- **x**
  : The type shall be _real_.

### **Result**

The return value is of type _real_ and of the same kind as **x**. It lies in
the range

```fortran
     0 \<= **erfc**(x) \<= 2.
```

and is a processor-dependent approximation to the complementary error
function of **x** ( \*\*1-erf(x) ).

### **Examples**

Sample program:

```fortran
program demo_erfc
use, intrinsic :: iso_fortran_env, only : &
 & real_kinds, real32, real64, real128
implicit none
real(kind=real64) :: x = 0.17_real64
   write(*,'(*(g0))')'X=',x, ' ERFC(X)=',erfc(x)
   write(*,'(*(g0))')'equivalently 1-ERF(X)=',1-erf(x)
end program demo_erfc
```

Results:

```text
 > X=.1700000000000000 ERFC(X)=.8100075387981912
 > equivalently 1-ERF(X)=.8100075387981912
```

### **Standard**

Fortran 2008

### **See also**

[**erf**(3)](#erf)
[**erf_scaled**(3)](#erf_scaled)

### **Resources**

- [Wikipedia:error function](https://en.wikipedia.org/wiki/Error_function)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
