(bgt)=
## bgt

### **Name**

**bgt**(3) - \[BIT:COMPARE\] Bitwise greater than

### **Synopsis**

```fortran
    result = bgt(i, j)
```

```fortran
      elemental logical function bgt(i, j)

       integer(kind=**),intent(in) :: i
       integer(kind=**),intent(in) :: j
```

### **Characteristics**

- **i** is an _integer_ or a boz-literal-constant.
- **j** is an _integer_ or a boz-literal-constant.
- a kind designated as ** may be any supported kind for the type
  The _integer_ _kind_ of **i** and **j\*\* may not necessarily be the same.
  kind. In addition, values may be a BOZ constant with a value valid
  for the _integer_ kind available with the most bits on the current
  platform.
- The return value is of type _logical_ and of the default kind.

### **Description**

**bgt** determines whether an integer is bitwise greater than another.
Bit-level representations of values are platform-dependent.

### **Options**

- **i**
  : reference value to compare against

- **j**
  : value to compare to **i**

### **Result**

The return value is of type _logical_ and of the default kind. The
result is true if the sequence of bits represented by _i_ is greater
than the sequence of bits represented by _j_, otherwise the result
is false.

Bits are compared from right to left.

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
   write(*,'(a)') 'we will compare other values to 64'
   i=64
   byte=i
   write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,bgt(byte,64_int8),byte

   write(*,'(a)') "comparing at the bit level, not as whole numbers."
   write(*,'(a)') "so pay particular attention to the negative"
   write(*,'(a)') "values on this two's complement platform ..."
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
 > we will compare other values to 64
 > +0064  F 01000000
 > comparing at the bit level, not as whole numbers.
 > so pay particular attention to the negative
 > values on this two's complement platform ...
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

Fortran 2008

### **See Also**

[**bge**(3)](#bge),
[**ble**(3)](#ble),
[**blt**(3)](#blt)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
