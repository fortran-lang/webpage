(epsilon)=
## epsilon

### **Name**

**epsilon**(3) - \[NUMERIC MODEL\] Epsilon function

### **Synopsis**

```fortran
    result = epsilon(x)
```

```fortran
     real(kind=kind(x)) function epsilon(x)

      real(kind=kind(x),intent(in)   :: x(..)
```

### **Characteristics**

- **x** shall be of type _real_. It may be a scalar or an array.
- the result is a scalar of the same type and kind type parameter as **x**.

### **Description**

**epsilon**(3) returns the floating point relative accuracy.
It is the nearly negligible number relative to **1**
such that **1+ little_number** is not equal to **1**; or more
precisely

```fortran
   real( 1.0, kind(x)) + epsilon(x) /=  real( 1.0, kind(x))
```

It may be thought of as the distance from 1.0 to the next largest
floating point number.

One use of **epsilon**(3) is to select a _delta_ value for algorithms that
search until the calculation is within _delta_ of an estimate.

If _delta_ is too small the algorithm might never halt, as a computation
summing values smaller than the decimal resolution of the data type does
not change.

### **Options**

- **x**
  : The type shall be _real_.

### **Result**

The return value is of the same type as the argument.

### **Examples**

Sample program:

```fortran
program demo_epsilon
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp) :: x = 3.143
real(kind=dp) :: y = 2.33d0

   ! so if x is of type real32, epsilon(x) has the value 2**-23
   print *, epsilon(x)
   ! note just the type and kind of x matter, not the value
   print *, epsilon(huge(x))
   print *, epsilon(tiny(x))

   ! the value changes with the kind of the real value though
   print *, epsilon(y)

   ! adding and subtracting epsilon(x) changes x
   write(*,*)x == x + epsilon(x)
   write(*,*)x == x - epsilon(x)

   ! these next two comparisons will be .true. !
   write(*,*)x == x + epsilon(x) * 0.999999
   write(*,*)x == x - epsilon(x) * 0.999999

   ! you can calculate epsilon(1.0d0)
   write(*,*)my_dp_eps()

contains

   function my_dp_eps()
   ! calculate the epsilon value of a machine the hard way
   real(kind=dp) :: t
   real(kind=dp) :: my_dp_eps

      ! starting with a value of 1, keep dividing the value
      ! by 2 until no change is detected. Note that with
      ! infinite precision this would be an infinite loop,
      ! but floating point values in Fortran have a defined
      ! and limited precision.
      my_dp_eps = 1.0d0
      SET_ST: do
         my_dp_eps = my_dp_eps/2.0d0
         t = 1.0d0 + my_dp_eps
         if (t <= 1.0d0) exit
      enddo SET_ST
      my_dp_eps = 2.0d0*my_dp_eps

   end function my_dp_eps
end program demo_epsilon
```

Results:

```text
  1.1920929E-07
  1.1920929E-07
  1.1920929E-07
  2.220446049250313E-016
 F
 F
 T
 T
  2.220446049250313E-016
```

### **Standard**

Fortran 95

### **See Also**

[**digits**(3)](#digits),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
