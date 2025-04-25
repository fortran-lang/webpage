(int)=
## int

### **Name**

**int**(3) - \[TYPE:NUMERIC\] Truncate towards zero and convert to integer

### **Synopsis**

```fortran
    result = int(a [,kind])
```

```fortran
     elemental integer(kind=KIND) function int(a, KIND )

      TYPE(kind=**),intent(in) :: a
      integer,optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **a** shall be of type integer, real, or complex, or a boz-literal-constant.
- **KIND** shall be a scalar integer constant expression.

### **Description**

**int**(3) truncates towards zero and return an _integer_.

### **Options**

- **a**
  : is the value to truncate towards zero

- **kind**
  : indicates the kind parameter of the result.
  If not present the returned type is that of default integer type.

### **Result**

returns an _integer_ variable applying the following rules:

**Case**:

1.  If **a** is of type _integer_, **int**(a) = a

2.  If **a** is of type _real_ and **|a| \< 1, int(a)** equals **0**. If **|a| \>=
    1**, then **int(a)** equals the integer whose magnitude does not exceed
    **a** and whose sign is the same as the sign of **a**.

3.  If **a** is of type _complex_, rule 2 is applied to the _real_ part of **a**.

4.  If _a_ is a boz-literal constant, it is treated as an _integer_
    with the _kind_ specified.

    The interpretation of a bit sequence whose most significant bit is
    **1** is processor dependent.

The result is undefined if it cannot be represented in the specified integer type.

### **Examples**

Sample program:

```fortran
program demo_int
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer :: i = 42
complex :: z = (-3.7, 1.0)
real :: x=-10.5, y=10.5

   print *, int(x), int(y)

   print *, int(i)

   print *, int(z), int(z,8)
   ! elemental
   print *, int([-10.9,-10.5,-10.3,10.3,10.5,10.9])
   ! note int(3) truncates towards zero

   ! CAUTION:
   ! a number bigger than a default integer can represent
   ! produces an incorrect result and is not required to
   ! be detected by the program.
   x=real(huge(0))+1000.0
   print *, int(x),x
   ! using a larger kind
   print *, int(x,kind=int64),x

   print *, int(&
   & B"111111111111111111111111111111111111111111111111111111111111111",&
   & kind=int64)
   print *, int(O"777777777777777777777",kind=int64)
   print *, int(Z"7FFFFFFFFFFFFFFF",kind=int64)

   ! elemental
   print *
   print *,int([ &
   &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
   &  0.0,   &
   &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])

end program demo_int
```

Results:

```text
 >          -10   10
 >           42
 >           -3  -3
 >          -10  -10  -10   10   10  10
 >  -2147483648   2.14748467E+09
 >   2147484672   2.14748467E+09
 >   9223372036854775807
 >   9223372036854775807
 >   9223372036854775807
 >
 >  -2          -2          -2          -2          -1
 >  -1           0           0           0           1
 >   1           2           2           2           2
```

### **Standard**

FORTRAN 77

### **See Also**

[**aint**(3)](#aint),
[**anint**(3)](#anint),
[**nint**(3)](#nint),
[**selected_int_kind**(3)](#selected_int_kind),
[**ceiling**(3)](#ceiling),
[**floor**(3)](#floor)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
