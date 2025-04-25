(cmplx)=
## cmplx

### **Name**

**cmplx**(3) - \[TYPE:NUMERIC\] Conversion to a complex type

### **Synopsis**

```fortran
    result = cmplx(x [,kind]) | cmplx(x [,y] [,kind])
```

```fortran
     elemental complex(kind=KIND) function cmplx( x, y, kind )

      type(TYPE(kind=**)),intent(in)          :: x
      type(TYPE(kind=**)),intent(in),optional :: y
      integer(kind=**),intent(in),optional    :: KIND
```

### **Characteristics**

- **x** may be _integer_, _real_, or _complex_.
- **y** may be _integer_ or _real_.
  **y** is allowed only if **x** is not _complex_.
- **KIND** is a constant _integer_ initialization expression indicating the kind
  parameter of the result.

The type of the arguments does not affect the kind of the result except
for a _complex_ **x** value.

- if **kind** is not present and **x** is _complex_ the result is of the kind
  of **x**.

- if **kind** is not present and **x** is not _complex_ the result if of default
  _complex_ kind.

NOTE: a kind designated as \*\* may be any supported kind for the type

### **Description**

The **cmplx**(3) function converts numeric values to a _complex_ value.

Even though constants can be used to define a complex variable using syntax like

```fortran
      z = (1.23456789, 9.87654321)
```

this will not work for variables. So you cannot enter

```fortran
      z = (a, b)  ! NO ! (unless a and b are constants, not variables)
```

so to construct a _complex_ value using non-complex values you must use
the **cmplx**(3) function:

```fortran
      z = cmplx(a, b)
```

or assign values separately to the imaginary and real components using
the **%IM** and **%RE** designators:

```fortran
      z%re = a
      z%im = b
```

If **x** is complex **y** is not allowed and **cmplx** essentially
returns the input value except for an optional change of kind, which can be
useful when passing a value to a procedure that requires the arguments
to have a different kind (and does not return an altered value):

```fortran
      call something(cmplx(z,kind=real64))
```

would pass a copy of a value with kind=real64 even if z had a different kind

but otherwise is equivalent to a simple assign. So if z1 and z2 were _complex_:

```fortran
      z2 = z1        ! equivalent statements
      z2 = cmplx(z1)
```

If **x** is not _complex_ **x** is only used to define the real component
of the result but **y** is still optional -- the imaginary part of the
result will just be assigned a value of zero.

If **y** is present it is converted to the imaginary component.

#### **cmplx(3) and double precision**

Primarily in order to maintain upward compatibility you need to be careful
when working with complex values of higher precision that the default.

It was necessary for Fortran to continue to specify that **cmplx**(3)
always return a result of the default kind if the **kind** option
is absent, since that is the behavior mandated by FORTRAN 77.

It might have been preferable to use the highest precision of the
arguments for determining the return kind, but that is not the case. So
with arguments with greater precision than default values you are
required to use the **kind** argument or the greater precision values
will be reduced to default precision.

This means **cmplx(d1,d2)**, where **d1** and **d2** are
_doubleprecision_, is treated as:

```fortran
      cmplx(sngl(d1), sngl(d2))
```

which looses precision.

So Fortran 90 extends the **cmplx**(3) intrinsic by adding an extra
argument used to specify the desired kind of the complex result.

```fortran
      integer,parameter :: dp=kind(0.0d0)
      complex(kind=dp) :: z8
     ! wrong ways to specify constant values
      ! note this was stored with default real precision !
      z8 = cmplx(1.2345678901234567d0, 1.2345678901234567d0)
      print *, 'NO, Z8=',z8,real(z8),aimag(z8)

      z8 = cmplx(1.2345678901234567e0_dp, 1.2345678901234567e0_dp)
      ! again, note output components are just real
      print *, 'NO, Z8=',z8,real(z8),aimag(z8)
      !
      ! YES
      !
      ! kind= makes it work
      z8 = cmplx(1.2345678901234567d0, 1.2345678901234567d0,kind=dp)
      print *, 'YES, Z8=',z8,real(z8),aimag(z8)
```

A more recent alternative to using **cmplx**(3) is "F2018 component
syntax" where real and imaginary parts of a complex entity can be
accessed independently:

```fortran
value%RE     ! %RE specifies the real part
or
value%IM     ! %IM specifies the imaginary part

```

Where the designator value is of course of complex type.

The type of a complex-part-designator is _real_, and its kind and shape
are those of the designator. That is, you retain the precision of the
complex value by default, unlike with **cmplx**.

The following are examples of complex part designators:

```fortran
       impedance%re           !-- Same value as real(impedance)
       fft%im                 !-- Same value as AIMAG(fft)
       x%im = 0.0             !-- Sets the imaginary part of x to zero
       x(1:2)%re=[10,20]      !-- even if x is an array
```

#### NOTE for I/O

Note that if format statements are specified a complex value is
treated as two real values.

For list-directed I/O (ie. using an asterisk for a format) and NAMELIST
output the values are expected to be delimited by "(" and ")" and of
the form "(real*part,imaginary_part)". For NAMELIST input parenthesized
values or lists of multiple \_real* values are acceptable.

### **Options**

- **x**
  : The value assigned to the _real_ component of the result when **x** is
  not complex.

  If **x** is complex, the result is the same as if the real part of the
  input was passed as **x** and the imaginary part as **y**.

```fortran
     result = CMPLX (REAL (X), AIMAG (X), KIND).
```

That is, a complex **x** value is copied to the result value with a
possible change of kind.

- **y**
  : **y** is only allowed if **x** is not _complex_. Its value
  is assigned to the imaginary component of the result and defaults
  to a value of zero if absent.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Result**

The return value is of _complex_ type, with magnitudes determined by the
values **x** and **y**.

The common case when **x** is not complex is that the real
component of the result is assigned the value of **x** and the imaginary
part is zero or the value of **y** if **y** is present.

When **x** is complex **y** is not allowed and the result is the same
value as **x** with a possible change of kind. That is, the real part
is **real(x, kind)** and the imaginary part is **real(y, kind)**.

### **Examples**

Sample program:

```fortran
program demo_aimag
implicit none
integer,parameter :: dp=kind(0.0d0)
real(kind=dp)     :: precise
complex(kind=dp)  :: z8
complex           :: z4, zthree(3)
   precise=1.2345678901234567d0

  ! basic
   z4 = cmplx(-3)
   print *, 'Z4=',z4
   z4 = cmplx(1.23456789, 1.23456789)
   print *, 'Z4=',z4
   ! with a format treat a complex as two real values
   print '(1x,g0,1x,g0,1x,g0)','Z4=',z4

  ! working with higher precision values
   ! using kind=dp makes it keep DOUBLEPRECISION precision
   ! otherwise the result would be of default kind
   z8 = cmplx(precise, -precise )
   print *, 'lost precision Z8=',z8
   z8 = cmplx(precise, -precise ,kind=dp)
   print *, 'kept precision Z8=',z8

  ! assignment of constant values does not require cmplx(3)00
   ! The following is intuitive and works without calling cmplx(3)
   ! but does not work for variables just constants
   z8 = (1.1111111111111111d0, 2.2222222222222222d0 )
   print *, 'Z8 defined with constants=',z8

  ! what happens when you assign a complex to a real?
   precise=z8
   print *, 'LHS=',precise,'RHS=',z8

  ! elemental
   zthree=cmplx([10,20,30],-1)
   print *, 'zthree=',zthree

  ! descriptors are an alternative
   zthree(1:2)%re=[100,200]
   print *, 'zthree=',zthree

end program demo_aimag
```

Results:

```text
    Z4= (-3.000000,0.0000000E+00)
    Z4= (1.234568,1.234568)
    Z4= 1.234568 1.234568
    lost precision Z8= (1.23456788063049,-1.23456788063049)
    kept precision Z8= (1.23456789012346,-1.23456789012346)
    Z8 defined with constants= (1.11111111111111,2.22222222222222)
    LHS=   1.11111111111111      RHS= (1.11111111111111,2.22222222222222)
    zthree= (10.00000,-1.000000) (20.00000,-1.000000) (30.00000,-1.000000)
    zthree= (100.0000,-1.000000) (200.0000,-1.000000) (30.00000,-1.000000)
```

### **Standard**

FORTRAN 77, KIND added in Fortran 90.

### **See Also**

- [**aimag**(3)](#aimag) - Imaginary part of complex number
- [**conjg**(3)](#conjg) - Complex conjugate function
- [**real**(3)](#real) - Convert to real type

Fortran has strong support for _complex_ values, including many intrinsics
that take or produce _complex_ values in addition to algebraic and
logical expressions:

[**abs**(3)](#abs),
[**acosh**(3)](#acosh),
[**acos**(3)](#acos),
[**asinh**(3)](#asinh),
[**asin**(3)](#asin),
[**atan2**(3)](#atan2),
[**atanh**(3)](#atanh),
[**atan**(3)](#atan),
[**cosh**(3)](#cosh),
[**cos**(3)](#cos),
[**co_sum**(3)](#co_sum),
[**dble**(3)](#dble),
[**dot_product**(3)](#dot_product),
[**exp**(3)](#exp),
[**int**(3)](#int),
[**is_contiguous**(3)](#is_contiguous),
[**kind**(3)](#kind),
[**log**(3)](#log),
[**matmul**(3)](#matmul),
[**precision**(3)](#precision),
[**product**(3)](#product),
[**range**(3)](#range),
[**rank**(3)](#rank),
[**sinh**(3)](#sinh),
[**sin**(3)](#sin),
[**sqrt**(3)](#sqrt),
[**storage_size**(3)](#storage_size),
[**sum**(3)](#sum),
[**tanh**(3)](#tanh),
[**tan**(3)](#tan),
[**unpack**(3)](#unpack),

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
