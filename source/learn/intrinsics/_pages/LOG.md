## log

### **Name**

**log**(3) - \[MATHEMATICS\] Logarithm function

### **Syntax**

```fortran
result = log(x)
```

### **Description**

**log(x)** computes the natural logarithm of **x**, i.e. the logarithm to
the base "e".

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_.

### **Returns**

The return value is of type _real_ or _complex_. The kind type parameter is
the same as **x**. If **x** is _complex_, the imaginary part OMEGA is in the range

**-PI** \< OMEGA \<= PI.

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

FORTRAN 77 and later

 _fortran-lang intrinsic descriptions_
