## blt

### **Name**

**blt**(3) - \[BIT:COMPARE\] Bitwise less than
### **Syntax**
```fortran
    elemental function blt(i, j)

     integer(kind=KIND),intent(in) :: i
     integer(kind=KIND),intent(in) :: j
     logical :: blt
```
where the _kind_ of **i** and **j** may be of any supported kind.
An exception is that one value may be a BOZ constant with a
value valid for the _kind_ of the _integer_ value.
### **Description**

Determines whether an integer is bitwise less than another.

### **Arguments**

- **i**
    Shall be of _integer_ type or a BOZ literal constant.

- **j**
  : Shall be of _integer_ type or a BOZ constant.

### **Returns**

The return value is of type _logical_ and of the default kind.
### **Examples**

Sample program:
```fortran
program demo_blt
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer            :: i
integer(kind=int8) :: byte
  ! Compare some one-byte values to 64.
   ! Notice that the values are tested as bits not as integers
   ! so sign bits in the integer are treated just like any other
   do i=-128,127,32
      byte=i
      write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,blt(byte,64_int8),byte
   enddo

   ! see the BGE() description for an extended example

end program demo_blt
```
Results:
```text
   > -0128  F 10000000
   > -0096  F 10100000
   > -0064  F 11000000
   > -0032  F 11100000
   > +0000  T 00000000
   > +0032  T 00100000
   > +0064  F 01000000
   > +0096  F 01100000
```
### **Standard**

Fortran 2008 and later

### **See Also**

[**bge**(3)](#bge),
[**bgt**(3)](#bgt),
[**ble**(3)](#ble)

 _fortran-lang intrinsic descriptions \@urbanjost_
