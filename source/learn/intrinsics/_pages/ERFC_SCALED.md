## erfc_scaled

### **Name**

**erfc_scaled**(3) - \[MATHEMATICS\] Error function

### **Syntax**

```fortran
result = erfc_scaled(x)
```

### **Description**

**erfc_scaled**(x) computes the exponentially-scaled complementary
error function of **x**:

$$
e^{x^2} \frac{2}{\sqrt{\pi}} \int_{x}^{\infty}
e^{-t^2} dt.
$$

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type _real_ and of the same kind as **x**.

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
     0.83375830214998126
```

### **Standard**

Fortran 2008 and later

_fortran-lang intrinsic descriptions_
