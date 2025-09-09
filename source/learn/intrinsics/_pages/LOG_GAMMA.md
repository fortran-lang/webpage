(log_gamma)=
## log_gamma

### **Name**

**log_gamma**(3) - \[MATHEMATICS\] Logarithm of the absolute value of
the Gamma function

### **Synopsis**

```fortran
    result = log_gamma(x)
```

```fortran
     elemental real(kind=KIND) function log_gamma(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** may be any _real_ type
- the return value is of same type and kind as **x**.

### **Description**

**log_gamma**(3) computes the natural logarithm of the absolute value
of the Gamma function.

### **Options**

- **x**
  : neither negative nor zero value to render the result for.

### **Result**

The result has a value equal to a processor-dependent approximation
to the natural logarithm of the absolute value of the gamma function
of **x**.

### **Examples**

Sample program:

```fortran
program demo_log_gamma
implicit none
real :: x = 1.0
   write(*,*)x,log_gamma(x) ! returns 0.0
   write(*,*)x,log_gamma(3.0) ! returns 0.693 (approximately)
end program demo_log_gamma
```

Results:

```text
 >    1.000000      0.0000000E+00
 >    1.000000      0.6931472
```

### **Standard**

Fortran 2008

### **See Also**

Gamma function: [**gamma**(3)](#gamma)

_fortran-lang intrinsic descriptions_
