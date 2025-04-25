(asin)=
## asin

### **Name**

**asin**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arcsine function

### **Synopsis**

```fortran
    result = asin(x)
```

```fortran
     elemental TYPE(kind=KIND) function asin(x)

      TYPE(kind=KIND) :: x
```

### **Characteristics**

- **TYPE** may be _real_ or _complex_
- **KIND** may be any kind supported by the associated type.
- The returned value will be of the same type and kind as the argument.

### **Description**

**asin**(3) computes the arcsine of its argument **x**.

The arcsine is the inverse function of the sine function. It is commonly
used in trigonometry when trying to find the angle when the lengths of
the hypotenuse and the opposite side of a right triangle are known.

### **Options**

- **x**
  : The value to compute the arcsine of
  : The type shall be either _real_ and a magnitude that is less than or
  equal to one; or be _complex_.

### **Result**

- **result**
  The result has a value equal to a processor-dependent approximation
  to arcsin(x).

  If **x** is real the result is _real_ and it is expressed in radians
  and lies in the range

```fortran
        PI/2 <= ASIN (X) <= PI/2.
```

If the argument (and therefore the result) is imaginary the real part
of the result is in radians and lies in the range

```fortran
    -PI/2 <= real(asin(x)) <= PI/2
```

### **Examples**

The arcsine will allow you to find the measure of a right angle when you
know the ratio of the side opposite the angle to the hypotenuse.

So if you knew that a train track rose 1.25 vertical miles on a track
that was 50 miles long, you could determine the average angle of incline
of the track using the arcsine. Given

     sin(theta) = 1.25 miles/50 miles (opposite/hypotenuse)

Sample program:

```fortran
program demo_asin
use, intrinsic :: iso_fortran_env, only : dp=>real64
implicit none
! value to convert degrees to radians
real(kind=dp),parameter :: D2R=acos(-1.0_dp)/180.0_dp
real(kind=dp)           :: angle, rise, run
character(len=*),parameter :: all='(*(g0,1x))'
  ! given sine(theta) = 1.25 miles/50 miles (opposite/hypotenuse)
  ! then taking the arcsine of both sides of the equality yields
  ! theta = arcsine(1.25 miles/50 miles) ie. arcsine(opposite/hypotenuse)
  rise=1.250_dp
  run=50.00_dp
  angle = asin(rise/run)
  print all, 'angle of incline(radians) = ', angle
  angle = angle/D2R
  print all, 'angle of incline(degrees) = ', angle

  print all, 'percent grade=',rise/run*100.0_dp
end program demo_asin
```

Results:

```
    angle of incline(radians) =    2.5002604899361139E-002
    angle of incline(degrees) =    1.4325437375665075
    percent grade=   2.5000000000000000
```

The percentage grade is the slope, written as a percent. To calculate
the slope you divide the rise by the run. In the example the rise is
1.25 mile over a run of 50 miles so the slope is 1.25/50 = 0.025.
Written as a percent this is 2.5 %.

For the US, two and 1/2 percent is generally thought of as the upper
limit. This means a rise of 2.5 feet when going 100 feet forward. In
the US this was the maximum grade on the first major US railroad, the
Baltimore and Ohio. Note curves increase the frictional drag on a
train reducing the allowable grade.

### **Standard**

FORTRAN 77 , for a _complex_ argument Fortran 2008

### **See Also**

Inverse function: [**sin**(3)](#sin)

### **Resources**

- [wikipedia: inverse trigonometric functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
