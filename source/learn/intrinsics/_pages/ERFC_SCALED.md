(erfc_scaled)=
## erfc_scaled

### **Name**

**erfc_scaled**(3) - \[MATHEMATICS\] Scaled complementary error function

### **Synopsis**

```fortran
    result = erfc_scaled(x)
```

```fortran
     elemental real(kind=KIND) function erfc_scaled(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** is of type _real_ of any valid kind
- **KIND** is any kind valid for a _real_ type
- the result has the same characteristics as **x**

### **Description**

**erfc_scaled**(3) computes the exponentially-scaled complementary
error function of **x**:

$$
e^{x^2} \frac{2}{\sqrt{\pi}} \int_{x}^{\infty}
e^{-t^2} dt.
$$

erfc_scaled(x)=exp(x\*x)erfc(x)

#### NOTE1

The complementary error function is asymptotic to
exp(-X2)/(X/PI). As such it underflows at approximately X >= 9 when
using ISO/IEC/IEEE 60559:2011 single precision arithmetic. The
exponentially-scaled complementary error function is asymptotic to
1/(X PI). As such it does not underflow until X > HUGE (X)/PI.

### **Options**

- **x**
  the value to apply the **erfc** function to

### **Result**

The approximation to the exponentially-scaled complementary error function
of **x**

### **Examples**

Sample program:

```fortran
program demo_erfc_scaled
implicit none
real(kind(0.0d0)) :: x = 0.17d0
   x = erfc_scaled(x)
   print *, x
end program demo_erfc_scaled
```

Results:

```text
 >   0.833758302149981
```

### **Standard**

Fortran 2008

### **See also**

[**erf**(3)](#erf),
[**exp**(3)](#exp),
[**erfc**(3)](#erfc)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
