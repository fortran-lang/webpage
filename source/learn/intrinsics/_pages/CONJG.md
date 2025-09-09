(conjg)=
## conjg

### **Name**

**conjg**(3) - \[NUMERIC\] Complex conjugate of a complex value

### **Synopsis**

```fortran
    result = conjg(z)
```

```fortran
     elemental complex(kind=KIND) function conjg(z)

      complex(kind=**),intent(in) :: z
```

### **Characteristics**

- **z** is a _complex_ value of any valid kind.
- The returned value has the same _complex_ type as the input.

### **Description**

**conjg**(3) returns the complex conjugate of the _complex_ value **z**.

That is, If **z** is the _complex_ value **(x, y)** then the result is
**(x, -y)**.

In mathematics, the complex conjugate of a complex number is a value
whose real and imaginary part are equal parts are equal in magnitude to
each other but the **y** value has opposite sign.

For matrices of complex numbers, **conjg(array)** represents the
element-by-element conjugation of **array**; not the conjugate transpose
of the **array** .

### **Options**

- **z**
  : The value to create the conjugate of.

### **Result**

Returns a value equal to the input value except the sign of
the imaginary component is the opposite of the input value.

That is, if **z** has the value **(x,y)**, the result has the value
**(x, -y)**.

### **Examples**

Sample program:

```fortran
program demo_conjg
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
complex :: z = (2.0, 3.0)
complex(kind=real64) :: dz = (   &
   &  1.2345678901234567_real64, -1.2345678901234567_real64)
complex :: arr(3,3)
integer :: i
   ! basics
    ! notice the sine of the imaginary component changes
    print *, z, conjg(z)

    ! any complex kind is supported. z is of default kind but
    ! dz is kind=real64.
    print *, dz
    dz = conjg(dz)
    print *, dz
    print *

    ! the function is elemental so it can take arrays
    arr(1,:)=[(-1.0, 2.0),( 3.0, 4.0),( 5.0,-6.0)]
    arr(2,:)=[( 7.0,-8.0),( 8.0, 9.0),( 9.0, 9.0)]
    arr(3,:)=[( 1.0, 9.0),( 2.0, 0.0),(-3.0,-7.0)]

    write(*,*)'original'
    write(*,'(3("(",g8.2,",",g8.2,")",1x))')(arr(i,:),i=1,3)
    arr = conjg(arr)
    write(*,*)'conjugate'
    write(*,'(3("(",g8.2,",",g8.2,")",1x))')(arr(i,:),i=1,3)

end program demo_conjg
```

Results:

```fortran
 >  (2.000000,3.000000) (2.000000,-3.000000)
 >
 >  (1.23456789012346,-1.23456789012346)
 >  (1.23456789012346,1.23456789012346)
 >
 >  original
 > (-1.0    , 2.0    ) ( 3.0    , 4.0    ) ( 5.0    ,-6.0    )
 > ( 7.0    ,-8.0    ) ( 8.0    , 9.0    ) ( 9.0    , 9.0    )
 > ( 1.0    , 9.0    ) ( 2.0    , 0.0    ) (-3.0    ,-7.0    )
 >
 >  conjugate
 > (-1.0    ,-2.0    ) ( 3.0    ,-4.0    ) ( 5.0    , 6.0    )
 > ( 7.0    , 8.0    ) ( 8.0    ,-9.0    ) ( 9.0    ,-9.0    )
 > ( 1.0    ,-9.0    ) ( 2.0    , 0.0    ) (-3.0    , 7.0    )
```

### **Standard**

FORTRAN 77

### **See Also**

- [**aimag**(3)](#aimag) - Imaginary part of complex number
- [**cmplx**(3)](#cmplx) - Complex conversion function
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
