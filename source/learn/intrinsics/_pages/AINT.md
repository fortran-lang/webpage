## aint

### **Name**

**aint**(3) - \[NUMERIC\] Truncate to a whole number

### **Syntax**

```fortran
result = aint(x)

   real(kind=kind(x)),elemental  :: aint

   real(kind=kind(x)),intent(in) :: x
```

or

```fortran
result = aint(x, KIND)

   real(kind=KIND),elemental     :: aint

   integer,intent(in),optional   :: KIND
   real(kind=kind(x)),intent(in) :: x
```

### **Description**

**aint(x, kind)** truncates its argument to a whole number.

### **Arguments**

- **x**
  : the type of the argument shall be _real_.

- **kind**
  : (optional) an _integer_ initialization expression indicating the
  kind parameter of the result.

### **Returns**

The return value is of type _real_ with the kind type parameter of
the argument if the optional **kind** is absent; otherwise, the kind
type parameter will be given by **kind**. If the magnitude of **x**
is less than one, **aint(x)** returns zero. If the magnitude is equal
to or greater than one then it returns the largest whole number that
does not exceed its magnitude. The sign is the same as the sign of **x**.

### **Examples**

Sample program:

```fortran
program demo_aint
use, intrinsic :: iso_fortran_env, only : real32, real64
implicit none
real(kind=real32) :: x4
real(kind=real64) :: x8

   x4 = 4.3210_real32
   x8 = 4.3210_real64
   print *, aint(x4), aint(x8)
   print *
   ! elemental
   print *,aint([ &
    &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
    &  0.0,   &
    &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])

end program demo_aint
```

Results:

```text
     4.00000000       4.0000000000000000

    -2.00000000      -2.00000000      -2.00000000      -2.00000000
    -1.00000000      -1.00000000      -0.00000000       0.00000000
     0.00000000       1.00000000       1.00000000       2.00000000
     2.00000000       2.00000000       2.00000000
```

### **Standard**

FORTRAN 77 and later

### **See Also**

[**anint**(3)](ANINT),
[**int**(3)](INT),
[**nint**(3)](NINT),
[**selected_int_kind**(3)](SELECTED_INT_KIND),
[**ceiling**(3)](CEILING),
[**floor**(3)](FLOOR)

_fortran-lang intrinsic descriptions_
