(blt)=
## blt

### **Name**

**blt**(3) - \[BIT:COMPARE\] Bitwise less than

### **Synopsis**

```fortran
    result = blt(i,j)
```

```fortran
     elemental logical function blt(i, j)

      integer(kind=**),intent(in) :: i
      integer(kind=**),intent(in) :: j
```

### **Characteristics**

- **i** is an _integer_ of any kind or a BOZ-literal-constant
- **j** is an _integer_ of any kind or a BOZ-literal-constant, not
  necessarily the same as **i**.
- the result is of default logical kind

BOZ constants must have a value valid for the _integer_ kind available
with the most bits on the current platform.

### **Description**

**blt**(3) determines whether an _integer_ is bitwise less than another.

### **Options**

- **i**
  : Shall be of _integer_ type or a BOZ literal constant.

- **j**
  : Shall be of _integer_ type or a BOZ constant.

### **Result**

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
  ! BOZ literals
   write(*,*)blt(z'1000', z'101011010')
   ! see the BGE() description for an extended description
   ! of related information

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
   > T
```

### **Standard**

Fortran 2008

### **See Also**

[**bge**(3)](#bge),
[**bgt**(3)](#bgt),
[**ble**(3)](#ble)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
