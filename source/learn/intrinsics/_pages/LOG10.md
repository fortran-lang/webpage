(log10)=
## log10

### **Name**

**log10**(3) - \[MATHEMATICS\] Base 10 or common logarithm

### **Synopsis**

```fortran
    result = log10(x)
```

```fortran
     elemental real(kind=KIND) function log10(x)

      real(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** may be any kind of _real_ value
- the result is the same type and characteristics as **x**.

### **Description**

**log10**(3) computes the base 10 logarithm of **x**. This is generally
called the "common logarithm".

### **Options**

- **x**
  : A _real_ value > 0 to take the log of.

### **Result**

The logarithm to base 10 of **x**

### **Examples**

Sample program:

```fortran
program demo_log10
use, intrinsic :: iso_fortran_env, only : real_kinds, &
 & real32, real64, real128
implicit none
real(kind=real64) :: x = 10.0_real64

   x = log10(x)
   write(*,'(*(g0))')'log10(',x,') is ',log10(x)

   ! elemental
   write(*, *)log10([1.0, 10.0, 100.0, 1000.0, 10000.0, &
                     & 100000.0, 1000000.0, 10000000.0])

end program demo_log10
```

Results:

```text
 > log10(1.000000000000000) is .000000000000000
 >   0.0000000E+00   1.000000       2.000000       3.000000       4.000000
 >    5.000000       6.000000       7.000000
```

### **Standard**

FORTRAN 77

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions_
