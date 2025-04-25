(cos)=
## cos

### **Name**

**cos**(3) - \[MATHEMATICS:TRIGONOMETRIC\] Cosine function

### **Synopsis**

```fortran
    result = cos(x)
```

```fortran
     elemental TYPE(kind=KIND) function cos(x)

      TYPE(kind=KIND),intent(in) :: x
```

### **Characteristics**

- **x** is of type _real_ or _complex_ of any valid kind.
- **KIND** may be any kind supported by the associated type of **x**.
- The returned value will be of the same type and kind as the argument
  **x**.

### **Description**

**cos**(3) computes the cosine of an angle **x** given the size of
the angle in radians.

The cosine of a _real_ value is the ratio of the adjacent side to the
hypotenuse of a right-angled triangle.

### **Options**

- **x**
  : The angle in radians to compute the cosine of.

### **Result**

The return value is the tangent of **x**.

If **x** is of the type _real_, the return value is in radians and lies in
the range **-1 \<= cos(x) \<= 1** .

If **x** is of type complex, its real part is regarded as a value in
radians, often called the phase.

### **Examples**

Sample program:

```fortran
program demo_cos
implicit none
character(len=*),parameter :: g2='(a,t20,g0)'
doubleprecision,parameter :: PI=atan(1.0d0)*4.0d0
   write(*,g2)'COS(0.0)=',cos(0.0)
   write(*,g2)'COS(PI)=',cos(PI)
   write(*,g2)'COS(PI/2.0d0)=',cos(PI/2.0d0),'EPSILON=',epsilon(PI)
   write(*,g2)'COS(2*PI)=',cos(2*PI)
   write(*,g2)'COS(-2*PI)=',cos(-2*PI)
   write(*,g2)'COS(-2000*PI)=',cos(-2000*PI)
   write(*,g2)'COS(3000*PI)=',cos(3000*PI)
end program demo_cos
```

Results:

```text
 > COS(0.0)=          1.000000
 > COS(PI)=           -1.000000000000000
 > COS(PI/2.0d0)=     .6123233995736766E-16
 > EPSILON=           .2220446049250313E-15
 > COS(2*PI)=         1.000000000000000
 > COS(-2*PI)=        1.000000000000000
 > COS(-2000*PI)=     1.000000000000000
 > COS(3000*PI)=      1.000000000000000
```

### **Standard**

FORTRAN 77

### **See Also**

[**acos**(3)](#acos),
[**sin**(3)](#sin),
[**tan**(3)](#tan)

### **Resources**

- [Wikipedia:sine and cosine](https://en.wikipedia.org/wiki/Sine_and_cosine)

_fortran-lang intrinsic descriptions_
