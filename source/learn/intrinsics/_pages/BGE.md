## bge

### **Name**

**bge**(3) - \[BIT:COMPARE\] Bitwise greater than or equal to

### **Syntax**
```fortran
    elemental function bge(i, j)

     integer(kind=KIND),intent(in) :: i,j
     logical :: bge
```
where the _kind_ of **i** and **j** must be the same.

### **Description**

  Determines whether an integer is bitwise greater than or equal to
  another.

### **Arguments**

- **i**
  : The value to test if >= **j**

- **j**
  : The value to test **i** against.

### **Returns**

  The return value is of type _logical_ and of the default kind.
  It is _.true._ if **i** is bit-wise greater than **j** and _.false._
  otherwise.

### **Examples**

Sample program:
```fortran
program demo_bge
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer            :: i
integer(kind=int8) :: byte
integer(kind=int8),allocatable :: arr1(:), arr2(:)
  ! basic usage
   write(*,*)'bge(-127,127)=',bge( -127_int8, 127_int8 )
   ! surprised -127 is great than 127 (on most machines, at least)?
   ! if the values are not represented as "two's complement" or if
   ! the endian changes the representation of a sign can vary!

   write(*,*)'compare some values to 01000000 (64)'
   write(*,*)'Notice that the values are tested as bits, so essentially'
   write(*,*)'the values are tested as if unsigned integers.'
   do i=-128,127,32
      byte=i
      write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,bge(byte,64_int8),byte
   enddo
  ! elemental

   ! an array and scalar
   write(*, *)'compare array of values [-128, -0, +0, 127] to 127'
   write(*, *)bge(int([-128, -0, +0, 127], kind=int8), 127_int8)
   ! are +0 and -9 the same?

   ! two arrays
   write(*, *)'compare two arrays'
   arr1=int( [ -127, -0, +0,  127], kind=int8 )
   arr2=int( [  127,  0,  0, -127], kind=int8 ) 
   write(*,*)'arr1=',arr1
   write(*,*)'arr2=',arr2
   write(*, *)'bge(arr1,arr2)=',bge( arr1, arr2 )

end program demo_bge
```
Results:

  Note that how an integer value is represented at the bit level
  can vary. These are just the values expected on the most common
  platforms ...

```text
   >  bge(-127,127)= T
   >  compare some values to 01000000 (64)
   >  Notice that the values are tested as bits, so essentially
   >  the values are tested as if unsigned integers.
   > -0128  T 10000000
   > -0096  T 10100000
   > -0064  T 11000000
   > -0032  T 11100000
   > +0000  F 00000000
   > +0032  F 00100000
   > +0064  T 01000000
   > +0096  T 01100000
   >  compare array of values [-128, -0, +0, 127] to 127
   >  T F F T
   >  compare two arrays
   >  arr1= -127    0    0  127
   >  arr2=  127    0    0 -127
   >  bge(arr1,arr2)= T T T F
```
### **Standard**

Fortran 2008 and later

### **See Also**

[**bgt**(3)](#bgt),
[**ble**(3)](#ble),
[**blt**(3)](#bit)

 _fortran-lang intrinsic descriptions \@urbanjost_
