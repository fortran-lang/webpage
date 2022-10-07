## atan2

### **Name**

**atan2**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arctangent function

### **Syntax**

```fortran
result = atan2(y, x)
```

### **Description**

**atan2(y, x)** computes the arctangent of the complex number
( **x** + i **y** ) .

This function can be used to transform from Cartesian into polar
coordinates and allows to determine the angle in the correct quadrant.
To convert from Cartesian Coordinates **(x,y)** to polar coordinates

(r,theta): $$ \begin{aligned} r &= \sqrt{x**2 + y**2} \\ \theta
&= \tan\*\*{**-1**}(y / x) \end{aligned} $$

### **Arguments**

- **y**
  : The type shall be _real_.

- **x**
  : The type and kind type parameter shall be the same as **y**. If **y** is
  zero, then **x** must be nonzero.

### **Returns**

The return value has the same type and kind type parameter as **y**. It is
the principal value of the complex number **(x + i, y)**. If x is nonzero,
then it lies in the range **-PI \<= atan(x) \<= PI**. The sign is
positive if **y** is positive. If **y** is zero, then the return value is zero
if **x** is strictly positive, **PI** if **x** is negative and **y** is positive zero
(or the processor does not handle signed zeros), and **-PI** if **x** is
negative and **Y** is negative zero. Finally, if **x** is zero, then the
magnitude of the result is **PI/2**.

### **Examples**

Sample program:

```fortran
program demo_atan2
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp) :: x = 1.e0_sp, y = 0.5e0_sp, z
   z = atan2(y,x)
   write(*,*)x,y,z
end program demo_atan2
```

Results:

```text
      1.00000000      0.500000000      0.463647604
```

### **Standard**

FORTRAN 77 and later

###### fortran-lang intrinsic descriptions
