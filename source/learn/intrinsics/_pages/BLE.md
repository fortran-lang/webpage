(ble)=
## ble

### **Name**

**ble**(3) - \[BIT:COMPARE\] Bitwise less than or equal to

### **Synopsis**

```fortran
    result = ble(i,j)
```

```fortran
     elemental logical function ble(i, j)

      integer(kind=**),intent(in) :: i
      integer(kind=**),intent(in) :: j
```

### **Characteristics**

- **i** and **j** may be of any supported _integer_ kind, not
  necessarily the same. An exception is that values may be a
  BOZ constant with a value valid for the _integer_ kind available with
  the most bits on the current platform.
- the returned value is a logical scalar of default kind

### **Description**

**ble**(3) determines whether an integer is bitwise less than or
equal to another, assuming any shorter value is padded on the left
with zeros to the length of the longer value.

### **Options**

- **i**
  : the value to compare **j** to

- **j**
  : the value to be tested for being less than or equal to **i**

### **Result**

The return value is _.true._ if any bit in **j** is less than any bit
in **i** starting with the rightmost bit and continuing tests leftward.

### **Examples**

Sample program:

```fortran
program demo_ble
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer            :: i
integer(kind=int8) :: byte
  ! Compare some one-byte values to 64.
   ! Notice that the values are tested as bits not as integers
   ! so sign bits in the integer are treated just like any other
   do i=-128,127,32
      byte=i
      write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,ble(byte,64_int8),byte
      write(*,'(sp,i0.4,*(4x,b0.8))')64_int8,64_int8
   enddo

   ! see the BGE() description for an extended description
   ! of related information

end program demo_ble
```

Results:

```text
   -0128  F 10000000
   +0064    01000000
   -0096  F 10100000
   +0064    01000000
   -0064  F 11000000
   +0064    01000000
   -0032  F 11100000
   +0064    01000000
   +0000  T 00000000
   +0064    01000000
   +0032  T 00100000
   +0064    01000000
   +0064  T 01000000
   +0064    01000000
   +0096  F 01100000
   +0064    01000000
```

### **Standard**

Fortran 2008

### **See Also**

[**bge**(3)](#bge),
[**bgt**(3)](#bgt),
[**blt**(3)](#blt)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
