## bgt

### **Name**

**bgt**(3) - \[BIT:COMPARE\] Bitwise greater than

### **Syntax**
```fortran
    elemental function bgt(i, j)

     integer(kind=KIND),intent(in) :: i
     integer(kind=KIND),intent(in) :: j
     logical :: bgt
```
  where the _kind_ of **i** and **j** may be of any supported _integer_
  kind, not necessarily the same.  An exception is that values may be a
  BOZ constant with a value valid for the _integer_ kind available with
  the most bits on the current platform.

### **Description**

  Determines whether an integer is bitwise greater than another.
  Bit-level representations of values are platform-dependent.

### **Arguments**

- **i**
  : Shall be of _integer_ type or a BOZ literal constant.

- **j**
  : Shall be of _integer_ type or a BOZ literal constant.

### **Returns**

  The return value is of type _logical_ and of the default kind. The
  result is true if the sequence of bits represented by _i_ is greater
  than the sequence of bits represented by _j_, otherwise the result
  is false.

### **Examples**

Sample program:
```fortran
program demo_bgt
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer            :: i
integer(kind=int8) :: byte
  ! Compare some one-byte values to 64.
   ! Notice that the values are tested as bits not as integers
   ! so sign bits in the integer are treated just like any other
   do i=-128,127,32
      byte=i
      write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,bgt(byte,64_int8),byte
   enddo

   ! see the BGE() description for an extended description 
   ! of related information

end program demo_bgt
```
Results:
```text
   > -0128  T 10000000
   > -0096  T 10100000
   > -0064  T 11000000
   > -0032  T 11100000
   > +0000  F 00000000
   > +0032  F 00100000
   > +0064  F 01000000
   > +0096  T 01100000
```
### **Standard**

Fortran 2008 and later

### **See Also**

[**bge**(3)](#bge),
[**ble**(3)](#ble),
[**blt**(3)](#blt)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
