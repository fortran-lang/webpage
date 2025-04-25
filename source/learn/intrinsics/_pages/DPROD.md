(dprod)=
## dprod

### **Name**

**dprod**(3) - \[NUMERIC\] Double precision real product

### **Synopsis**

```fortran
    result = dprod(x,y)
```

```fortran
     elemental function dprod(x,y)

      real,intent(in) :: x
      real,intent(in) :: y
      doubleprecision :: dprod
```

### **Characteristics**

- **x** is a default real.
- **y** is a default real.
- the result is a _doubleprecision_ real.

The setting of compiler options specifying the size of a default _real_
can affect this function.

### **Description**

**dprod**(3) produces a _doubleprecision_ product of default _real_
values **x** and **y**.

That is, it is expected to convert the arguments to double precision
before multiplying, which a simple expression **x\*y** would not be
required to do. This can be significant in specialized computations
requiring high precision.

The result has a value equal to a processor-dependent approximation
to the product of **x** and **y**. Note it is recommended in the
standard that the processor compute the product in double precision,
rather than in single precision then converted to double precision;
but is only a recommendation.

### **Options**

- **x**
  : the multiplier

- **y**
  : the multiplicand

### **Result**

The returned value of the product should have the same value as
**dble(x)\*dble(y)**.

### **Examples**

Sample program:

```fortran
program demo_dprod
implicit none
integer,parameter :: dp=kind(0.0d0)
real :: x = 5.2
real :: y = 2.3
doubleprecision :: xx
real(kind=dp)   :: dd

   print *,'algebraically 5.2 x 2.3 is exactly 11.96'
   print *,'as floating point values results may differ slightly:'
   ! basic usage
   dd = dprod(x,y)
   print *, 'compare dprod(xy)=',dd, &
   & 'to x*y=',x*y, &
   & 'to dble(x)*dble(y)=',dble(x)*dble(y)

   print *,'test if an expected result is produced'
   xx=-6.0d0
   write(*,*)DPROD(-3.0, 2.0),xx
   write(*,*)merge('PASSED','FAILED',DPROD(-3.0, 2.0) == xx)

   print *,'elemental'
   print *, dprod( [2.3,3.4,4.5], 10.0 )
   print *, dprod( [2.3,3.4,4.5], [9.8,7.6,5.4] )

end program demo_dprod
```

Results:
(this can vary between programming environments):

```text
 >  algebraically 5.2 x 2.3 is exactly 11.96
 >  as floating point values results may differ slightly:
 >  compare dprod(xy)=   11.9599993133545      to x*y=   11.96000
 >  to dble(x)*dble(y)=   11.9599993133545
 >  test if an expected result is produced
 >   -6.00000000000000       -6.00000000000000
 >  PASSED
 >  elemental
 >    22.9999995231628     34.0000009536743     45.0000000000000
 >    22.5399999713898     25.8400004005432     24.3000004291534
```

### **Standard**

FORTRAN 77

### **See Also**

[**dble**(3)](#dble)
[**real**(3)](#real)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
