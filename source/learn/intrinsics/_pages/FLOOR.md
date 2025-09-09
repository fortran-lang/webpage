(floor)=
## floor

### **Name**

**floor**(3) - \[NUMERIC\] Function to return largest integral value
not greater than argument

### **Synopsis**

```fortran
    result = floor(a [,kind])
```

```fortran
     elemental integer(kind=KIND) function floor( a ,kind )

      real(kind=**),intent(in) :: a
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **a** is a _real_ of any kind
- _KIND_ is any valid value for type _integer_.
- the result is an _integer_ of the specified or default kind

### **Description**

**floor**(3) returns the greatest integer less than or equal to **a**.

In other words, it picks the whole number at or to the left of the value on
the number line.

This means care has to be taken that the magnitude of the _real_ value **a**
does not exceed the range of the output value, as the range of values supported
by _real_ values is typically larger than the range for _integers_.

### **Options**

- **a**
  : The value to operate on. Valid values are restricted by the size of
  the returned _integer_ kind to the range **-huge(int(a,kind=KIND))-1**
  to **huge(int(a),kind=KIND)**.

- **kind**
  : A scalar _integer_ constant initialization expression
  indicating the kind parameter of the result.

### **Result**

The return value is of type _integer(kind)_ if **kind** is present and of
default-kind _integer_ otherwise.

The result is undefined if it cannot be represented in the specified
integer type.

If in range for the kind of the result the result is the whole number
at or to the left of the input value on the number line.

If **a** is positive the result is the value with the fractional part
removed.

If **a** is negative, it is the whole number at or to the left of the
input value.

### **Examples**

Sample program:

```fortran
program demo_floor
implicit none
real :: x = 63.29
real :: y = -63.59
    print *, x, floor(x)
    print *, y, floor(y)
   ! elemental
   print *,floor([ &
   &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
   &  0.0,   &
   &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])

   ! note even a small deviation from the whole number changes the result
   print *,      [2.0,2.0-epsilon(0.0),2.0-2*epsilon(0.0)]
   print *,floor([2.0,2.0-epsilon(0.0),2.0-2*epsilon(0.0)])

   ! A=Nan, Infinity or  <huge(0_KIND)-1 < A > huge(0_KIND) is undefined
end program demo_floor
```

Results:

```text
 >     63.29000             63
 >    -63.59000            -64
 >            -3         -3         -3         -2         -2         -1
 >            -1          0          0          1          1          2
 >             2          2          2
 >     2.000000      2.000000      2.000000
 >             2          1          1
```

### **Standard**

Fortran 95

### **See Also**

[**ceiling**(3)](#ceiling),
[**nint**(3)](#nint),
[**aint**(3)](#aint),
[**anint**(3)](#anint),
[**int**(3)](#int),
[**selected_int_kind**(3)](#selected_int_kind)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

<!--
real function floor(fval0)
!@(#) return largest integer not greater than x as a real
   fval=fval0
   if(fval.ne.float(int(fval))) then
      if(fval.gt.0.0) fval = int(fval)
      if(fval.lt.0.0) fval = int(fval)-1
   endif
   floor=fval
end function floor
-->
