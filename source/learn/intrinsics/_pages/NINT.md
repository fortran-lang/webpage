(nint)=
## nint

### **Name**

**nint**(3) - \[TYPE:NUMERIC\] Nearest whole number

### **Synopsis**

```fortran
    result = nint( a [,kind] )
```

```fortran
     elemental integer(kind=KIND) function nint(a, kind )

      real(kind=**),intent(in) :: a
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **a** is type real of any kind
- **KIND** is a scalar integer constant expression
- The result is default _integer_ kind or the value of **kind**
  if **kind** is present.

### **Description**

**nint**(3) rounds its argument to the nearest whole number with its
sign preserved.

The user must ensure the value is a valid value for the range of the
**kind** returned. If the processor cannot represent the result in the kind
specified, the result is undefined.

If **a** is greater than zero, **nint(a)** has the value **int(a+0.5)**.

If **a** is less than or equal to zero, **nint(a)** has the value
**int(a-0.5)**.

### **Options**

- **a**
  : The value to round to the nearest whole number

- **kind**
  : can specify the kind of the output value. If not present, the
  output is the default type of _integer_.

### **Result**

The result is the integer nearest **a**, or if there are two integers
equally near **a**, the result is whichever such _integer_ has the greater
magnitude.

The result is undefined if it cannot be represented in the specified
integer type.

### **Examples**

Sample program:

```fortran
program demo_nint
implicit none
integer,parameter   :: dp=kind(0.0d0)
real,allocatable    :: in(:)
integer,allocatable :: out(:)
integer             :: i
real                :: x4
real(kind=dp)       :: x8

  ! basic use
   x4 = 1.234E0
   x8 = 4.721_dp
   print *, nint(x4), nint(-x4)
   print *, nint(x8), nint(-x8)

  ! elemental
   in = [ -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, -0.4, &
        &  0.0,   &
        & +0.04, +0.5, +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ]
   out = nint(in)
   do i=1,size(in)
      write(*,*)in(i),out(i)
   enddo

  ! dusty corners
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
 >               1          -1
 >               5          -5
 >      -2.700000              -3
 >      -2.500000              -3
 >      -2.200000              -2
 >      -2.000000              -2
 >      -1.500000              -2
 >      -1.000000              -1
 >     -0.5000000              -1
 >     -0.4000000               0
 >      0.0000000E+00           0
 >      3.9999999E-02           0
 >      0.5000000               1
 >       1.000000               1
 >       1.500000               2
 >       2.000000               2
 >       2.200000               2
 >       2.500000               3
 >       2.700000               3
 >     Range limits for typical KINDS:
 >     1 127
 >     2 32767
 >     4 2147483647
 >     8 9223372036854775807
 >     Any KIND big enough? ICHECK=          -1
 >     These are all wrong answers for   1.234566949990144E+019
 >        0
 >          0
 >     -2147483648
 >      -9223372036854775808
```

### **Standard**

FORTRAN 77 , with KIND argument - Fortran 90

### **See Also**

[**aint**(3)](#aint),
[**anint**(3)](#anint),
[**int**(3)](#int),
[**selected_int_kind**(3)](#selected_int_kind),
[**ceiling**(3)](#ceiling),
[**floor**(3)](#floor)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
