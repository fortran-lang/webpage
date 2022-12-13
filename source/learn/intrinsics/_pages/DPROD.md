## dprod

### **Name**

**dprod**(3) - \[NUMERIC\] Double precision real product

### **Syntax**

```fortran
   elemental function dprod(x,y)

    real,intent(in) :: x
    real,intent(in) :: y
    doubleprecision :: dprod
```
### **Description**

**dprod(x,y)** produces a _doubleprecision_ product of default _real_
values **x** and **y**.

The result has a value equal to a processor-dependent approximation to
the product of **x** and **y**. It is recommended that the processor
compute the product in double precision, rather than in single precision
then converted to double precision.

### **Arguments**

- **x**
  : the multiplier, a _real_ value of default kind

- **y**
  : the multiplicand, a _real_ value of default kind.
  **y** Must have the same type and kind parameters as **x**

The setting of compiler options specifying the size of a default _real_
can affect this function.

### **Returns**

The return value is doubleprecision (ie. _real(kind=kind(0.0d0))_).
It should have the same value as **dble(x)\*dble(y)**.

### **Examples**

Sample program:

```fortran
program demo_dprod
use, intrinsic :: iso_fortran_env, only : real_kinds, &
& real32, real64, real128
implicit none
integer,parameter :: dp=kind(0.0d0)
real :: x = 5.2
real :: y = 2.3
real(kind=dp) :: dd

   ! basic usage
   dd = dprod(x,y)
   print *, 'compare dprod(xy)=',dd, &
   & 'to x*y=',x*y, &
   & 'to dble(x)*dble(y)=',dble(x)*dble(y)

   ! elemental
   print *, dprod( [2.3,3.4,4.5], 10.0 )
   print *, dprod( [2.3,3.4,4.5], [9.8,7.6,5.4] )

   ! other interesting comparisons
   print *, 'integer multiplication of digits=',52*23
   print *, 52*23/100.0
   print *, 52*23/100.0d0

   !! A common extension is to take doubleprecision arguments
   !! and return higher precision when available
   bigger: block
   doubleprecision :: xx = 5.2_dp
   doubleprecision :: yy = 2.3_dp
   print *, 'dprop==>',dprod(xx,yy)
   print *, 'multipy==>',xx*yy
   print *, 'using dble==>',dble(xx)*dble(yy)
   print *, 'kind of arguments is',kind(xx)
   print *, 'kind of result is',kind(dprod(xx,yy))
   endblock bigger

end program demo_dprod
```
  Results:
  (this can vary between programming environments):
```text
    compare dprod(xy)= 11.9599993133545 to x*y= 11.96000
    to dble(x)*dble(y)= 11.9599993133545
      22.9999995231628  34.0000009536743  45.0000000000000
      22.5399999713898  25.8400004005432  24.3000004291534
    integer multiplication of digits=        1196
      11.96000
      11.9600000000000
    dprop==>   11.9599999999999994848565165739273
    multipy==>   11.9600000000000
    using dble==>   11.9600000000000
    kind of arguments is           8
    kind of result is          16
```
### **Standard**

FORTRAN 77 and later

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
