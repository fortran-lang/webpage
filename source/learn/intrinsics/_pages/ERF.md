(erf)=
## erf

### **Name**

**erf**(3) - \[MATHEMATICS\] Error function

### **Synopsis**

```fortran
    result = erf(x)
```

```fortran
     elemental real(kind=KIND) function erf(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** is of type _real_
- The result is of the same _type_ and _kind_ as **x**.

### **Description**

**erf**(3) computes the error function of **x**, defined as

$$
\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt.
$$

### **Options**

- **x**
  : The type shall be _real_.

### **Result**

The return value is of type _real_, of the same kind as **x** and lies in the
range **-1** \<= **erf**(x) \<= 1 .

### **Examples**

Sample program:

```fortran
program demo_erf
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x = 0.17_real64
    write(*,*)x, erf(x)
end program demo_erf
```

Results:

```text
     0.17000000000000001       0.18999246120180879
```

### **Standard**

Fortran 2008

### **See also**

[**erfc**(3)](#erfc),
[**erf_scaled**(3)](#erfc_scaled)

### **Resources**

- [Wikipedia:error function](https://en.wikipedia.org/wiki/Error_function)

_fortran-lang intrinsic descriptions_
