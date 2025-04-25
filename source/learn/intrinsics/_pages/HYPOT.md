(hypot)=
## hypot

### **Name**

**hypot**(3) - \[MATHEMATICS\] Returns the Euclidean distance - the distance between a point and the origin.

### **Synopsis**

```fortran
    result = hypot(x, y)
```

```fortran
     elemental real(kind=KIND) function hypot(x,y)

      real(kind=KIND),intent(in) :: x
      real(kind=KIND),intent(in) :: y
```

### **Characteristics**

- **x,y** and the result shall all be _real_ and of the same **kind**.

### **Description**

**hypot**(3) is referred to as the Euclidean distance function. It is
equal to

```fortran
sqrt(x**2+y**2)
```

without undue underflow or overflow.

In mathematics, the _Euclidean distance_ between two points in Euclidean
space is the length of a line segment between two points.

**hypot(x,y)** returns the distance between the point **<x,y>** and
the origin.

### **Options**

- **x**
  : The type shall be _real_.

- **y**
  : The type and kind type parameter shall be the same as **x**.

### **Result**

The return value has the same type and kind type parameter as **x**.

The result is the positive magnitude of the distance of the point
**<x,y>** from the origin **<0.0,0.0>** .

### **Examples**

Sample program:

```fortran
program demo_hypot
use, intrinsic :: iso_fortran_env, only : &
 & real_kinds, real32, real64, real128
implicit none
real(kind=real32) :: x, y
real(kind=real32),allocatable :: xs(:), ys(:)
integer :: i
character(len=*),parameter :: f='(a,/,SP,*(3x,g0,1x,g0:,/))'

   x = 1.e0_real32
   y = 0.5e0_real32

   write(*,*)
   write(*,'(*(g0))')'point <',x,',',y,'> is ',hypot(x,y)
   write(*,'(*(g0))')'units away from the origin'
   write(*,*)

   ! elemental
   xs=[  x,  x**2,  x*10.0,  x*15.0, -x**2  ]
   ys=[  y,  y**2, -y*20.0,  y**2,   -y**2  ]

   write(*,f)"the points",(xs(i),ys(i),i=1,size(xs))
   write(*,f)"have distances from the origin of ",hypot(xs,ys)
   write(*,f)"the closest is",minval(hypot(xs,ys))

end program demo_hypot
```

Results:

```text
   point <1.00000000,0.500000000> is 1.11803401
   units away from the origin

   the points
      +1.00000000 +0.500000000
      +1.00000000 +0.250000000
      +10.0000000 -10.0000000
      +15.0000000 +0.250000000
      -1.00000000 -0.250000000
   have distances from the origin of
      +1.11803401 +1.03077638
      +14.1421356 +15.0020828
      +1.03077638
   the closest is
      +1.03077638
```

### **Standard**

Fortran 2008

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
