(sin)=
## sin

### **Name**

**sin**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Sine function

### **Synopsis**

```fortran
    result = sin(x)
```

```fortran
     elemental TYPE(kind=KIND) function sin(x)

      TYPE(kind=KIND) :: x
```

### **Characteristics**

- **x** may be any _real_ or _complex_ type
- **KIND** may be any kind supported by the associated type of **x**.
- The returned value will be of the same type and kind as the argument
  **x**.

### **Description**

**sin**(3) computes the sine of an angle given the size of the angle
in radians.

The sine of an angle in a right-angled triangle is the ratio of the
length of the side opposite the given angle divided by the length of
the hypotenuse.

### **Options**

- **x**
  : The angle in radians to compute the sine of.

### **Result**

- **result**
  The return value contains the processor-dependent approximation of
  the sine of **x**

  If X is of type _real_, it is regarded as a value in radians.

  If X is of type _complex_, its real part is regarded as a value
  in radians.

### **Examples**

Sample program:

```fortran
program sample_sin
implicit none
real :: x = 0.0
   x = sin(x)
   write(*,*)'X=',x
end program sample_sin
```

Results:

```text
 >  X=  0.0000000E+00
```

### Extended Example

#### Haversine Formula

From the article on "Haversine formula" in Wikipedia:

```text
    The haversine formula is an equation important in navigation,
    giving great-circle distances between two points on a sphere from
    their longitudes and latitudes.
```

So to show the great-circle distance between the Nashville International
Airport (BNA) in TN, USA, and the Los Angeles International Airport
(LAX) in CA, USA you would start with their latitude and longitude,
commonly given as

```text
  BNA: N 36 degrees 7.2',   W 86 degrees 40.2'
  LAX: N 33 degrees 56.4',  W 118 degrees 24.0'
```

which converted to floating-point values in degrees is:

```text
       Latitude Longitude

     - BNA
       36.12, -86.67

     - LAX
       33.94, -118.40
```

And then use the haversine formula to roughly calculate the distance
along the surface of the Earth between the locations:

Sample program:

```fortran
program demo_sin
implicit none
real :: d
    d = haversine(36.12,-86.67, 33.94,-118.40) ! BNA to LAX
    print '(A,F9.4,A)', 'distance: ',d,' km'
contains
function haversine(latA,lonA,latB,lonB) result (dist)
!
! calculate great circle distance in kilometers
! given latitude and longitude in degrees
!
real,intent(in) :: latA,lonA,latB,lonB
real :: a,c,dist,delta_lat,delta_lon,lat1,lat2
real,parameter :: radius = 6371 ! mean earth radius in kilometers,
! recommended by the International Union of Geodesy and Geophysics

! generate constant pi/180
real, parameter :: deg_to_rad = atan(1.0)/45.0
   delta_lat = deg_to_rad*(latB-latA)
   delta_lon = deg_to_rad*(lonB-lonA)
   lat1 = deg_to_rad*(latA)
   lat2 = deg_to_rad*(latB)
   a = (sin(delta_lat/2))**2 + &
          & cos(lat1)*cos(lat2)*(sin(delta_lon/2))**2
   c = 2*asin(sqrt(a))
   dist = radius*c
end function haversine
end program demo_sin
```

Results:

```text
 > distance: 2886.4446 km
```

### **Standard**

FORTRAN 77

### **See Also**

[**asin**(3)](#asin),
[**cos**(3)](#cos),
[**tan**(3)](#tan),
[**acosh**(3)](#acosh),
[**acos**(3)](#acos),
[**asinh**(3)](#asinh),
[**atan2**(3)](#atan2),
[**atanh**(3)](#atanh),
[**acosh**(3)](#acosh),
[**asinh**(3)](#asinh),
[**atanh**(3)](#atanh)

### **Resources**

- [Wikipedia:sine and cosine](https://en.wikipedia.org/wiki/Sine_and_cosine)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
