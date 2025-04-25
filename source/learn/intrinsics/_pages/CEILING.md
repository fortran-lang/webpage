(ceiling)=
## ceiling

### **Name**

**ceiling**(3) - \[NUMERIC\] Integer ceiling function

### **Synopsis**

```fortran
    result = ceiling(a [,kind])
```

```fortran
     elemental integer(KIND) function ceiling(a,KIND)

      real(kind=**),intent(in)  :: a
      integer,intent(in),optional :: KIND
```

### **Characteristics**

- \*\* a is of type _real_
- **KIND** shall be a scalar integer constant expression.
  It specifies the kind of the result if present.
- the result is _integer_. It is default kind if **KIND** is not
  specified

### **Description**

**ceiling**(3) returns the least integer greater than or equal to **a**.

On the number line -n <-- 0 -> +n the value returned is always at or
to the right of the input value.

### **Options**

- **a**
  : A _real_ value to produce a ceiling for.

- **kind**
  : indicates the kind parameter of the result.

### **Result**

The result will be the _integer_ value equal to **a** or the least
integer greater than **a** if the input value is not equal to a
whole number.

If **a** is equal to a whole number, the returned value is **int(a)**.

The result is undefined if it cannot be represented in the specified
_integer_ type.

### **Examples**

Sample program:

```fortran
program demo_ceiling
implicit none
! just a convenient format for a list of integers
character(len=*),parameter :: ints='(*("   > ",5(i0:,",",1x),/))'
real :: x
real :: y
  ! basic usage
   x = 63.29
   y = -63.59
   print ints, ceiling(x)
   print ints, ceiling(y)
   ! note the result was the next integer larger to the right

  ! real values equal to whole numbers
   x = 63.0
   y = -63.0
   print ints, ceiling(x)
   print ints, ceiling(y)

  ! elemental (so an array argument is allowed)
   print ints , &
   & ceiling([ &
   &  -2.7,  -2.5, -2.2, -2.0, -1.5, &
   &  -1.0,  -0.5,  0.0, +0.5, +1.0, &
   &  +1.5,  +2.0, +2.2, +2.5, +2.7  ])

end program demo_ceiling
```

Results:

```text
   > 64
   > -63
   > 63
   > -63
   > -2, -2, -2, -2, -1,
   > -1, 0, 0, 1, 1,
   > 2, 2, 3, 3, 3
```

### **Standard**

Fortran 95

### **See Also**

[**floor**(3)](#floor),
[**nint**(3)](#nint)

[**aint**(3)](#aint),
[**anint**(3)](#anint),
[**int**(3)](#int),
[**selected_int_kind**(3)](#selected_int_kind)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
