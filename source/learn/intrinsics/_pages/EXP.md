## exp

### **Name**

**exp**(3) - \[MATHEMATICS\] Exponential function

### **Syntax**

```fortran
result = exp(x)
```

### **Description**

**exp**(x) computes the base "_e_" exponential of **x** where "_e_" is
_Euler's constant_.

If **x** is of type _complex_, its imaginary part is regarded as a value
in radians such that (see _Euler's formula_):

if
**cx=(re,im)**
then
**exp(cx)=exp(re)\*cmplx(cos(im),sin(im),kind=kind(cx))**

Since **exp**(3) is the inverse function of **log**(3) the maximum valid magnitude
of the _real_ component of **x** is **log(huge(x))**.

### **Arguments**

- **x**
  : The type shall be _real_ or _complex_.

### **Returns**

The value of the result is **e\*\*x** where **e** is Euler's constant.

The return value has the same type and kind as **x**.

### **Examples**

Sample program:

```fortran
program demo_exp
implicit none
real :: x, re, im
complex :: cx

   x = 1.0
   write(*,*)"Euler's constant is approximately",exp(x)

   !! complex values
   ! given
   re=3.0
   im=4.0
   cx=cmplx(re,im)

   ! complex results from complex arguments are Related to Euler's formula
   write(*,*)'given the complex value ',cx
   write(*,*)'exp(x) is',exp(cx)
   write(*,*)'is the same as',exp(re)*cmplx(cos(im),sin(im),kind=kind(cx))

   ! exp(3) is the inverse function of log(3) so
   ! the real component of the input must be less than or equal to
   write(*,*)'maximum real component',log(huge(0.0))
   ! or for double precision
   write(*,*)'maximum doubleprecision component',log(huge(0.0d0))

   ! but since the imaginary component is passed to the cos(3) and sin(3)
   ! functions the imaginary component can be any real value

end program demo_exp
```

Results:

```text
 Euler's constant is approximately   2.718282
 given the complex value  (3.000000,4.000000)
 exp(x) is (-13.12878,-15.20078)
 is the same as (-13.12878,-15.20078)
 maximum real component   88.72284
 maximum doubleprecision component   709.782712893384
```

### **Standard**

FORTRAN 77 and later

### **See Also**

- [**log**(3)](#log)

- Wikipedia:[Exponential function](https://en.wikipedia.org/wiki/Exponential_function)

- Wikipedia:[Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
