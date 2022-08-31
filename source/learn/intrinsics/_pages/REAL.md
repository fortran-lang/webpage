## real

### **Name**

**real**(3) - \[TYPE:NUMERIC\] Convert to real type

### **Syntax**

```fortran
result = real(x, kind)
```

### **Description**

**real(x, kind)** converts its argument **x** to a real type.

### **Arguments**

- **x**
  : Shall be _integer_, _real_, or _complex_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

These functions return a _real_ variable or array under the following
rules:

1.  **real**(x) is converted to a default _real_ type if **x** is an _integer_
    or _real_ variable.

2.  **real**(x) is converted to a real type with the kind type parameter
    of **x** if **x** is a _complex_ variable.

3.  **real(x, kind)** is converted to a _real_ type with kind type
    parameter **kind** if **x** is a _complex_, _integer_, or _real_ variable.

### **Examples**

Sample program:

```fortran
program demo_real
use,intrinsic :: iso_fortran_env, only : dp=>real64
implicit none
complex              :: zr = (1.0, 2.0)
doubleprecision      :: xd=huge(3.0d0)
complex(kind=dp) :: zd=cmplx(4.0e0_dp,5.0e0_dp,kind=dp)

   print *, real(zr), aimag(zr)
   print *, dble(zd), aimag(zd)

   write(*,*)xd,real(xd,kind=kind(0.0d0)),dble(xd)
end program demo_real
```

Results:

```
 1.00000000       2.00000000
 4.0000000000000000       5.0000000000000000
 1.7976931348623157E+308  1.7976931348623157E+308  1.7976931348623157E+308
```

### **Standard**

FORTRAN 77 and later

### **See Also**

[**dble**(3)](DBLE),
[**float**(3)](FLOAT)

###### fortran-lang intrinsic descriptions
