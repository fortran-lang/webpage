(acos)=
## acos

### **Name**

**acos**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Arccosine (inverse cosine) function

### **Synopsis**

```fortran
    result = acos(x)
```

```fortran
     elemental TYPE(kind=KIND) function acos(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **TYPE** may be _real_ or _complex_
- **KIND** may be any kind supported by the associated type.
- The returned value will be of the same type and kind as the argument.

### **Description**

**acos**(3) computes the arccosine of **x** (inverse of **cos(x)**).

### **Options**

- **x**
  : The value to compute the arctangent of.
  : If the type is _real_, the value must satisfy |**x**| <= 1.

### **Result**

The return value is of the same type and kind as **x**. The _real_ part of
the result is in radians and lies in the range **0 \<= acos(x%re) \<= PI** .

### **Examples**

Sample program:

```fortran
program demo_acos
use, intrinsic :: iso_fortran_env, only : real_kinds,real32,real64,real128
implicit none
character(len=*),parameter :: all='(*(g0,1x))'
real(kind=real64) :: x , d2r

   ! basics
    x = 0.866_real64
    print all,'acos(',x,') is ', acos(x)

   ! acos(-1) should be PI
    print all,'for reference &
    &PI ~= 3.14159265358979323846264338327950288419716939937510'
    write(*,*) acos(-1.0_real64)
    d2r=acos(-1.0_real64)/180.0_real64
    print all,'90 degrees is ', d2r*90.0_real64, ' radians'
   ! elemental
    print all,'elemental',acos([-1.0,-0.5,0.0,0.50,1.0])
   ! complex
    print *,'complex',acos( (-1.0,  0.0) )
    print *,'complex',acos( (-1.0, -1.0) )
    print *,'complex',acos( ( 0.0, -0.0) )
    print *,'complex',acos( ( 1.0,  0.0) )

end program demo_acos
```

Results:

```text
 acos( 0.86599999999999999 ) is  0.52364958093182890
 for reference PI ~= 3.14159265358979323846264338327950288419716939937510
    3.1415926535897931
 90 degrees is  1.5707963267948966  radians
 elemental 3.14159274 2.09439516 1.57079637 1.04719758 0.00000000
  complex            (3.14159274,-0.00000000)
  complex             (2.23703575,1.06127501)
  complex             (1.57079637,0.00000000)
  complex            (0.00000000,-0.00000000)
```

### **Standard**

FORTRAN 77 ; for a _complex_ argument - Fortran 2008

### **See Also**

Inverse function: [**cos**(3)](cos)

### **Resources**

- [wikipedia: inverse trigonometric functions](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
