## nint

### **Name**

**nint**(3) - \[TYPE:NUMERIC\] Nearest whole number

### **Syntax**

```fortran
    elemental function nint(x [, kind=NN]) result(ANSWER)
     real(kind=??),intent(in) :: x
     integer(kind=NN) :: ANSWER
```

### **Description**

**nint(x)** rounds its argument to the nearest whole number with its
sign preserved.

The user must ensure the value is a valid value for the range of the
**kind** returned. If the processor cannot represent the result in the kind
specified, the result is undefined.

If **x** is greater than zero, **nint(x)** has the value **int(x+0.5)**.

If **x** is less than or equal to zero, **nint(x)** has the value
**int(a-0.5)**.

### **Arguments**

- **x**
  : The type of the argument shall be _real_.

- **kind**
  : (Optional) A constant _integer_ expression indicating the kind
  parameter of the result. Otherwise, the kind type parameter is that
  of default _integer_ type.

### **Returns**

- **answer**
  : The result is the integer nearest **x**, or if there are two integers
  equally near **x**, the result is whichever such _integer_ has the greater
  magnitude.

  The result is undefined if it cannot be represented in the specified
  integer type.

### **Examples**

Sample program:

```fortran
program demo_nint
implicit none
integer,parameter :: dp=kind(0.0d0)
real              :: x4 = 1.234E0
real(kind=dp)     :: x8 = 4.721_dp

! basic use
   print *, nint(x4), nint(x8),nint(-x8)
   ! elemental
   print *,nint([ &
   &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
   &  0.0,   &
   &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])

! issues
ISSUES: block
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
integer :: icheck
   ! make sure input is in range for the type returned
   write(*,*)'Range limits for typical KINDS:'
   write(*,'(1x,g0,1x,g0)')  &
   & int8,huge(0_int8),   &
   & int16,huge(0_int16), &
   & int32,huge(0_int32), &
   & int64,huge(0_int64)

   ! the standard does not require this to be an error ...
   x8=12345.67e15 ! too big of a number
   icheck=selected_int_kind(ceiling(log10(x8)))
   write(*,*)'Any KIND big enough? ICHECK=',icheck
   print *, 'These are all wrong answers for ',x8
   print *, nint(x8,kind=int8)
   print *, nint(x8,kind=int16)
   print *, nint(x8,kind=int32)
   print *, nint(x8,kind=int64)
endblock ISSUES

end program demo_nint
```

Results:

```text
     1    5   -5
    -3   -3   -2   -2   -2
    -1   -1    0    1    1
     2    2    2    3    3
    Range limits for typical KINDS:
    1 127
    2 32767
    4 2147483647
    8 9223372036854775807
    Any KIND big enough? ICHECK=          16
    These are all wrong answers for    1.2345669499901444E+019
       0
         0
              0
    -9223372036854775808
```

### **Standard**

FORTRAN 77 and later, with KIND argument - Fortran 90 and later

### **See Also**

[**aint**(3)](AINT),
[**anint**(3)](ANINT),
[**int**(3)](INT),
[**selected_int_kind**(3)](SELECTED_INT_KIND),
[**ceiling**(3)](CEILING),
[**floor**(3)](FLOOR)

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
