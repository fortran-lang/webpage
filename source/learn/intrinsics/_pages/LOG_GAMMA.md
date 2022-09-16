## log_gamma

### **Name**

**log_gamma**(3) - \[MATHEMATICS\] Logarithm of the Gamma function

### **Syntax**

```fortran
x = log_gamma(x)
```

### **Description**

**log_gamma(x)** computes the natural logarithm of the absolute value of the Gamma function.

### **Arguments**

- **x**
  : Shall be of type _real_ and neither zero nor a negative integer.

### **Returns**

The return value is of type _real_ of the same kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_log_gamma
implicit none
real :: x = 1.0
   write(*,*)x,log_gamma(x) ! returns 0.0
end program demo_log_gamma
```

Results:

```text
      1.00000000       0.00000000
```

### **Standard**

Fortran 2008 and later

### **See Also**

Gamma function: [**gamma**(3)](#gamma)

 _fortran-lang intrinsic descriptions_
