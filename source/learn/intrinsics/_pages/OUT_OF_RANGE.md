(out_of_range)=
## out_of_range

### **Name**

**out_of_range**(3) - \[TYPE:NUMERIC\] Whether a value cannot be converted safely.

### **Synopsis**

```fortran
    result = out_of_range (x, mold [, round])
```

```fortran
     elemental logical function(x, mold, round)

      TYPE,kind=KIND),intent(in) :: x
      TYPE,kind=KIND),intent(in) :: mold
      logical,intent(in),optional     :: round
```

### **Characteristics**

- **x** is of type _integer_ or _real_.
- **mold** is an _integer_ or _real_ scalar.
- **round** is a _logical_ scalar.
- the result is a default _logical_.

### **Description**

**out_of_range**(3) determines whether a value **x** can be converted
safely to a _real_ or _integer_ variable the same type and kind
as **mold**.

For example, if **int8** is the kind value for an 8-bit binary integer
type, **out_of_range(-128.5, 0_int8)** will have the value false and
**out_of_range(-128.5, 0_int8, .true.)** will have the value _.true._
because the value will be truncated when converted to an _integer_
and -128 is a representable value on a two's complement machine in
eight bits even though +128 is not.

### **Options**

- **x**
  : a scalar to be tested for whether
  it can be stored in a variable of the type and kind of **mold**

- **mold**
  and kind are queried to determine the characteristics of what
  needs to be fit into.

- **round**
  : flag whether to round the value of **xx** before validating it as
  an integer value like **mold**.

  **round** can only be present if **x** is of type
  _real_ and **mold** is of type _integer_.

### **Result**

From the standard:

Case (i): If **mold** is of type integer, and **round** is absent or
present with the value false, the result is true
if and only if the value of X is an IEEE infinity or
NaN, or if the integer with largest magnitude that lies
between zero and X inclusive is not representable by
objects with the type and kind of **mold**.

Case (ii): If **mold** is of type integer, and **round** is present with
the value true, the result is true if and only
if the value of X is an IEEE infinity or NaN, or
if the integer nearest X, or the integer of greater
magnitude if two integers are equally near to X, is not
representable by objects with the type and kind of **mold**.

Case (iii): Otherwise, the result is true if and only if the value
of X is an IEEE infinity or NaN that is not
supported by objects of the type and kind of **mold**,
or if X is a finite number and the result of rounding
the value of X (according to the IEEE rounding mode if
appropriate) to the extended model for the kind of **mold**
has magnitude larger than that of the largest finite
number with the same sign as X that is representable
by objects with the type and kind of **mold**.

NOTE

**mold** is required to be a scalar because the only information
taken from it is its type and kind. Allowing an array **mold** would
require that it be conformable with **x**. **round** is scalar because
allowing an array rounding mode would have severe performance
difficulties on many processors.

### **Examples**

Sample program:

```fortran
program demo_out_of_range
use, intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
use, intrinsic :: iso_fortran_env, only : real32, real64, real128
implicit none
integer            :: i
integer(kind=int8) :: i8, j8

    ! compilers are not required to produce an error on out of range.
    ! here storing the default integers into 1-byte integers
    ! incorrectly can have unexpected results
    do i=127,130
       i8=i
       j8=-i
       ! OUT_OF_RANGE(3f) can let you check if the value will fit
       write(*,*)i8,j8,' might have expected',i,-i, &
        & out_of_range( i,i8), &
        & out_of_range(-i,i8)
    enddo
    write(*,*) 'RANGE IS ',-1-huge(0_int8),'TO',huge(0_int8)
    ! the real -128.5 is truncated to -128 and is in range
    write(*,*) out_of_range (  -128.5, 0_int8)         ! false

    ! the real -128.5 is rounded to -129 and is not in range
    write(*,*) out_of_range (  -128.5, 0_int8, .true.) ! true

end program demo_out_of_range
```

Results:

```text
  >  127 -127  might have expected         127        -127 F F
  > -128 -128  might have expected         128        -128 T F
  > -127  127  might have expected         129        -129 T T
  > -126  126  might have expected         130        -130 T T
  > RANGE IS         -128 TO  127
  > F
  > T
```

### **Standard**

FORTRAN 2018

### **See also**

- [**aimag**(3)](#aimag) - Imaginary part of complex number
- [**cmplx**(3)](#cmplx) - Convert values to a complex type
- [**dble**(3)](#dble) - Double conversion function
- [**int**(3)](#int) - Truncate towards zero and convert to integer
- [**nint**(3)](#nint) - Nearest whole number
- [**real**(3)](#real) - Convert to real type

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
