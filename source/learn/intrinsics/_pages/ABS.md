(abs)=
## abs

### **Name**

**abs**(3) - \[NUMERIC\] Absolute value

### **Synopsis**

```fortran
    result = abs(a)
```

```fortran
     elemental TYPE(kind=KIND) function abs(a)

      TYPE(kind=KIND),intent(in) :: a
```

### **Characteristics**

- **a** may be any _real_, _integer_, or _complex_ value.

- If **a** is _complex_ the returned value will be a _real_ with the
  same kind as **a**.

  Otherwise the returned type and kind is the same as for **a**.

### **Description**

**abs**(3) computes the absolute value of numeric argument **a**.

In mathematics, the absolute value or modulus of a real number **x**,
denoted **|x|**, is the magnitude of **x** without regard to its sign.

The absolute value of a number may be thought of as its distance from
zero. So for a complex value the absolute value is a real number
with magnitude **sqrt(x%re\*\*2,x%im\*\*2)**, as if the real component
is the x value and the imaginary value is the y value for the point
\<x,y\>.

### **Options**

- **a**
  : The value to compute the absolute value of.

### **Result**

If **a** is of type _integer_ or _real_, the value of the result
is the absolute value **|a|** and of the same type and kind as the
input argument.

If **a** is _complex_ with value **(x, y)**, the result is a _real_
equal to a processor-dependent approximation to

```fortran
        sqrt(x**2 + y**2)
```

computed without undue overflow or underflow (that means the
computation of the result can overflow the allowed magnitude of the
real value returned, and that very small values can produce underflows
if they are squared while calculating the returned value, for example).

That is, if you think of non-complex values as being complex values
on the x-axis and complex values as being x-y points <x%re,x%im>
the result of **abs**(3) is the (positive) magnitude of the distance
of the value from the origin.

### **Examples**

Sample program:

```fortran
program demo_abs
implicit none
integer,parameter :: dp=kind(0.0d0)

integer           :: i = -1
real              :: x = -1.0
complex           :: z = (-3.0,-4.0)
doubleprecision   :: rr = -45.78_dp

character(len=*),parameter :: &
   ! some formats
   frmt  =  '(1x,a15,1x," In: ",g0,            T51," Out: ",g0)', &
   frmtc = '(1x,a15,1x," In: (",g0,",",g0,")",T51," Out: ",g0)',  &
   g     = '(*(g0,1x))'

  ! basic usage
    ! any integer, real, or complex type
    write(*, frmt)  'integer         ',  i, abs(i)
    write(*, frmt)  'real            ',  x, abs(x)
    write(*, frmt)  'doubleprecision ', rr, abs(rr)
    write(*, frmtc) 'complex         ',  z, abs(z)

  ! You can take the absolute value of any value whose positive value
  ! is representable with the same type and kind.
    write(*, *) 'abs range test : ', abs(huge(0)), abs(-huge(0))
    write(*, *) 'abs range test : ', abs(huge(0.0)), abs(-huge(0.0))
    write(*, *) 'abs range test : ', abs(tiny(0.0)), abs(-tiny(0.0))
    ! A dusty corner is that abs(-huge(0)-1) of an integer would be
    ! a representable negative value on most machines but result in a
    ! positive value out of range.

  ! elemental
    write(*, g) ' abs is elemental:', abs([20,  0,  -1,  -3,  100])

  ! COMPLEX input produces REAL output
    write(*, g)' complex input produces real output', &
    & abs(cmplx(30.0_dp,40.0_dp,kind=dp))
    ! dusty corner: "kind=dp" is required or the value returned by
    ! CMPLX() is a default real instead of double precision

  ! the returned value for complex input can be thought of as the
  ! distance from the origin <0,0>
    write(*, g) ' distance of (', z, ') from zero is', abs( z )
    write(*, g) ' so beware of overflow with complex values'
    !write(*, g) abs(cmplx( huge(0.0), huge(0.0) ))
    write(*, g) ' because the biggest default real is',huge(0.0)

end program demo_abs
```

Results:

```text
    integer          In: -1                     Out: 1
    real             In: -1.000000              Out: 1.000000
    doubleprecision  In: -45.78000000000000     Out: 45.78000000000000
    complex          In: (-3.000000,-4.000000)  Out: 5.000000
    abs range test :   2147483647  2147483647
    abs range test :   3.4028235E+38  3.4028235E+38
    abs range test :   1.1754944E-38  1.1754944E-38
    abs is elemental: 20 0 1 3 100
    complex input produces real output 50.00000000000000
    distance of ( -3.000000 -4.000000 ) from zero is 5.000000
    so beware of overflow with complex values
    Inf
    because the biggest default real is .3402823E+39
```

### **Standard**

FORTRAN 77

### **See Also**

[**sign**(3)](#sign)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
