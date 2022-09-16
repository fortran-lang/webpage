## atanh

### **Name**

**atanh**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Inverse hyperbolic tangent function

### **Syntax**

```fortran
result = atanh(x)
```

### **Description**

**atanh(x)** computes the inverse hyperbolic tangent of **x**.

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_.

### **Returns**

The return value has same type and kind as **x**. If **x** is _complex_, the
imaginary part of the result is in radians and lies between

**-PI/2 \<= aimag(atanh(x)) \<= PI/2**

### **Examples**

Sample program:

```fortran
program demo_atanh
implicit none
real, dimension(3) :: x = [ -1.0, 0.0, 1.0 ]

   write (*,*) atanh(x)

end program demo_atanh
```

Results:

```text
   -Infinity   0.00000000             Infinity
```

### **Standard**

Fortran 2008 and later

### **See Also**

- [Wikipedia:hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)

Inverse function: [**tanh**(3)](#tanh)

 _fortran-lang intrinsic descriptions_
