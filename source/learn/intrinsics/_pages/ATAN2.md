(atan2)=
## atan2

### **Name**

**atan2**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arctangent (inverse tangent)
function

### **Synopsis**

```fortran
    result = atan2(y, x)
```

```fortran
     elemental real(kind=KIND) function atan2(y, x)

      real,kind=KIND) :: atan2
      real,kind=KIND),intent(in) :: y, x
```

### **Characteristics**

- **x** and **y** must be reals of the same kind.
- The return value has the same type and kind as **y** and **x**.

### **Description**

**atan2**(3) computes in radians a processor-dependent approximation of
the arctangent of the complex number ( **x**, **y** ) or equivalently the
principal value of the arctangent of the value **y/x** (which determines
a unique angle).

If **y** has the value zero, **x** shall not have the value zero.

The resulting phase lies in the range -PI <= ATAN2 (Y,X) <= PI and is equal to a
processor-dependent approximation to a value of arctan(Y/X).

### **Options**

- **y**
  : The imaginary component of the complex value **(x,y)** or the **y**
  component of the point **\<x,y\>**.

- **x**
  : The real component of the complex value **(x,y)** or the **x**
  component of the point **\<x,y\>**.

### **Result**

The value returned is by definition the principal value of the complex
number **(x, y)**, or in other terms, the phase of the phasor x+i\*y.

The principal value is simply what we get when we adjust a radian value
to lie between **-PI** and **PI** inclusive,

The classic definition of the arctangent is the angle that is formed
in Cartesian coordinates of the line from the origin point **\<0,0\>**
to the point **\<x,y\>** .

Pictured as a vector it is easy to see that if **x** and **y** are both
zero the angle is indeterminate because it sits directly over the origin,
so **atan(0.0,0.0)** will produce an error.

Range of returned values by quadrant:

```text
>                   +PI/2
>                     |
>                     |
>     PI/2 < z < PI   |   0 > z < PI/2
>                     |
>   +-PI -------------+---------------- +-0
>                     |
>     PI/2 < -z < PI  |   0 < -z < PI/2
>                     |
>                     |
>                   -PI/2
>
     NOTES:

     If the processor distinguishes -0 and +0 then the sign of the
     returned value is that of Y when Y is zero, else when Y is zero
     the returned value is always positive.
```

### **Examples**

Sample program:

```fortran
program demo_atan2
real :: z
complex :: c
 !
 ! basic usage
  ! ATAN2 (1.5574077, 1.0) has the value 1.0 (approximately).
  z=atan2(1.5574077, 1.0)
  write(*,*) 'radians=',z,'degrees=',r2d(z)
 !
 ! elemental arrays
  write(*,*)'elemental',atan2( [10.0, 20.0], [30.0,40.0] )
 !
 ! elemental arrays and scalars
  write(*,*)'elemental',atan2( [10.0, 20.0], 50.0 )
 !
 ! break complex values into real and imaginary components
 ! (note TAN2() can take a complex type value )
  c=(0.0,1.0)
  write(*,*)'complex',c,atan2( x=c%re, y=c%im )
 !
 ! extended sample converting cartesian coordinates to polar
  COMPLEX_VALS: block
  real                :: ang, radius
  complex,allocatable :: vals(:)
 !
  vals=[ &
    ( 1.0, 0.0 ), & ! 0
    ( 1.0, 1.0 ), & ! 45
    ( 0.0, 1.0 ), & ! 90
    (-1.0, 1.0 ), & ! 135
    (-1.0, 0.0 ), & ! 180
    (-1.0,-1.0 ), & ! 225
    ( 0.0,-1.0 )]   ! 270
  do i=1,size(vals)
     call cartesian_to_polar(vals(i)%re, vals(i)%im, radius,ang)
     write(*,101)vals(i),ang,r2d(ang),radius
  enddo
  101 format(             &
  & 'X= ',f5.2,           &
  & ' Y= ',f5.2,          &
  & ' ANGLE= ',g0,        &
  & T38,'DEGREES= ',g0.4, &
  & T54,'DISTANCE=',g0)
 endblock COMPLEX_VALS
!
contains
!
elemental real function r2d(radians)
! input radians to convert to degrees
doubleprecision,parameter :: DEGREE=0.017453292519943d0 ! radians
real,intent(in)           :: radians
   r2d=radians / DEGREE ! do the conversion
end function r2d
!
subroutine cartesian_to_polar(x,y,radius,inclination)
! return angle in radians in range 0 to 2*PI
implicit none
real,intent(in)  :: x,y
real,intent(out) :: radius,inclination
   radius=sqrt(x**2+y**2)
   if(radius.eq.0)then
      inclination=0.0
   else
      inclination=atan2(y,x)
      if(inclination < 0.0)inclination=inclination+2*atan2(0.0d0,-1.0d0)
   endif
end subroutine cartesian_to_polar
!
end program demo_atan2
```

Results:

```text
 >  radians=   1.000000     degrees=   57.29578
 >  elemental  0.3217506      0.4636476
 >  elemental  0.1973956      0.3805064
 >  complex (0.0000000E+00,1.000000)   1.570796
 > X=  1.00 Y=  0.00 ANGLE= .000000     DEGREES= .000   DISTANCE=1.000000
 > X=  1.00 Y=  1.00 ANGLE= .7853982    DEGREES= 45.00  DISTANCE=1.414214
 > X=  0.00 Y=  1.00 ANGLE= 1.570796    DEGREES= 90.00  DISTANCE=1.000000
 > X= -1.00 Y=  1.00 ANGLE= 2.356194    DEGREES= 135.0  DISTANCE=1.414214
 > X= -1.00 Y=  0.00 ANGLE= 3.141593    DEGREES= 180.0  DISTANCE=1.000000
 > X= -1.00 Y= -1.00 ANGLE= 3.926991    DEGREES= 225.0  DISTANCE=1.414214
 > X=  0.00 Y= -1.00 ANGLE= 4.712389    DEGREES= 270.0  DISTANCE=1.000000
```

### **Standard**

FORTRAN 77

### **See Also**

- [**atan**(3)](#atan)

### **Resources**

- [arctan:wikipedia](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)
  _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
