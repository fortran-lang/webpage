## atan2

### **Name**
**atan2**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arctangent (inverse tangent)
function

### **Syntax**
```fortran
  elemental function atan2(y, x)

    type(real,kind=KIND) :: atan2
    type(real,kind=KIND),intent(in) :: y, x
```
The return value has the same type and kind as **y**
and **x**.

### **Description**

**atan2(y, x)** computes in radians a processor-dependent approximation of
the arctangent of the complex number ( **x**, **y** ) or equivalently the
principal value of the arctangent of the value **y/x** (which determines
a unique angle).

### **Arguments**

- **y**
  : The imaginary component of the complex value **(x,y)** or the **y**
  component of the point **\<x,y\>**.

- **x**
  : The real component of the complex value **(x,y)** or the **x**
  component of the point **\<x,y\>**.

  If must be of the same kind as **y**. 

### **Returns**

The value returned is by definition the principal value of the complex
number **(x, y)**.

The principal value is simply what we get when we adjust a radian value
to lie between **-PI** and **PI** inclusive,

The type and kind of the result are the same as the elements of **x**.
and **y**.

The classic definition of the arctangent is the angle that is formed
in Cartesian coordinates of the line from the origin point **\<0,0\>**
to the point **\<x,y\>** . 

Pictured as such a vector it is easy to see that if **x** and **y**
are both zero the angle is indeterminent because it sits directly over
the origin, so **atan(0.0,0.0)** will produce an error.

Range of returned values by quadrant:
```text
>                   +PI/2
>                     |
>                     |
>        PI/2<Z<PI    |   0>Z<PI/2
>                     |
>   +-PI -------------+---------------- +-0
>                     |
>         PI/2<-Z<PI  |    0<-Z<PI/2
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
real :: x, y, z
complex :: c

 ! basic usage
  ! ATAN2 (1.5574077, 1.0) has the value 1.0 (approximately).
  z=atan2(1.5574077, 1.0)
  write(*,*) 'radians=',z,'degrees=',r2d(z)

 ! elemental arrays
  write(*,*)'elemental',atan2( [10.0, 20.0], [30.0,40.0] )
 ! elemental arrays and scalars
  write(*,*)'elemental',atan2( [10.0, 20.0], 50.0 )

 ! break into real and imaginary components to use with complex values
 ! note TAN2() can take a complex value
  c=(0.0,1.0)
  write(*,*)'complex',c,atan2( x=c%re, y=c%im )
  COMPLEX_VALS: block
  real                :: ang, radius
  complex,allocatable :: vals(:)

  vals=[ &
    ( 0.0, 1.0 ), &
    ( 1.0, 1.0 ), &
    ( 1.0, 0.0 ), &
    ( 0.0,-1.0 ), &
    (-1.0, 1.0 ), &
    (-1.0, 0.0 ), &
    (-1.0,-1.0 )]
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

contains

elemental real function r2d(radians)
! input radians to convert to degrees
doubleprecision,parameter :: DEGREE=0.017453292519943d0 ! radians
real,intent(in)           :: radians
   r2d=radians / DEGREE ! do the conversion
end function r2d

subroutine cartesian_to_polar(x,y,radius,inclination)
implicit none
real,intent(in)  :: x,y
real,intent(out) :: radius,inclination
   radius=sqrt(x**2+y**2)
   if(radius.eq.0)then
      inclination=0.0
   else
      inclination=atan2(y,x)
   endif
end subroutine cartesian_to_polar

end program demo_atan2
```
  Results:
```text
> radians=   1.00000000     degrees=   57.2957802    
> elemental  0.321750551      0.463647604    
> elemental  0.197395563      0.380506366    
>X=  0.00 Y=  1.00 ANGLE= 1.57079637  DEGREES= 90.00  DISTANCE=1.00000000
>X=  1.00 Y=  1.00 ANGLE= 0.785398185 DEGREES= 45.00  DISTANCE=1.41421354
>X=  1.00 Y=  0.00 ANGLE= 0.00000000  DEGREES= 0.000  DISTANCE=1.00000000
>X=  0.00 Y= -1.00 ANGLE= -1.57079637 DEGREES= -90.00 DISTANCE=1.00000000
>X= -1.00 Y=  1.00 ANGLE= 2.35619450  DEGREES= 135.0  DISTANCE=1.41421354
>X= -1.00 Y=  0.00 ANGLE= 3.14159274  DEGREES= 180.0  DISTANCE=1.00000000
>X= -1.00 Y= -1.00 ANGLE= -2.35619450 DEGREES= -135.0 DISTANCE=1.41421354
```
### **See Also**

- [**atan**(3)](ATAN)
- [arctan:wikipedia](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

### **Standard**

FORTRAN 77 and later

_fortran-lang intrinsic descriptions (license: MIT) @urbanjost_
