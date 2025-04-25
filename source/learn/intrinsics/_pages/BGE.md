(bge)=
## bge

### **Name**

**bge**(3) - \[BIT:COMPARE\] Bitwise greater than or equal to

### **Synopsis**

```fortran
    result = bge(i,j)
```

```fortran
      elemental logical function bge(i, j)

       integer(kind=**),intent(in) :: i
       integer(kind=**),intent(in) :: j
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type

- the _integer_ _kind_ of **i** and **j** may not necessarily be
  the same. In addition, values may be a BOZ constant with a value
  valid for the _integer_ kind available with the most bits on the
  current platform.

- The return value is of type default _logical_.

### **Description**

**bge**(3) Determines whether one _integer_ is bitwise greater than
or equal to another.

The bit-level representation of a value is platform dependent. The
endian-ness of a system and whether the system uses a "two's complement"
representation of signs can affect the results, for example.

A BOZ constant (Binary, Octal, Hexadecimal) does not have a _kind_
or _type_ of its own, so be aware it is subject to truncation when
transferred to an _integer_ type. The most bits the constant may
contain is limited by the most bits representable by any _integer_
kind supported by the compilation.

#### Bit Sequence Comparison

When bit sequences of unequal length are compared, the shorter sequence
is padded with zero bits on the left to the same length as the longer
sequence (up to the largest number of bits any available _integer_ kind
supports).

Bit sequences are compared from left to right, one bit at a time,
until unequal bits are found or until all bits have been compared and
found to be equal.

The bits are always evaluated in this order, not necessarily from MSB
to LSB (most significant bit to least significant bit).

If unequal bits are found the sequence with zero in the unequal
position is considered to be less than the sequence with one in the
unequal position.

### **Options**

- **i**
  : The value to test if >= **j** based on the bit representation
  of the values.

- **j**
  : The value to test **i** against.

### **Result**

Returns _.true._ if **i** is bit-wise greater than **j** and _.false._
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

  ! BASIC USAGE
   write(*,*)'bge(-127,127)=',bge( -127, 127 )
   ! on (very common) "two's complement" machines that are
   ! little-endian -127 will be greater than 127

   ! BOZ constants
   ! BOZ constants are subject to truncation, so make sure
   ! your values are valid for the integer kind being compared to
   write(*,*)'bge(b"0001",2)=',bge( b"1", 2)

  ! ELEMENTAL
   ! an array and scalar
   write(*, *)'compare array of values [-128, -0, +0, 127] to 127'
   write(*, *)bge(int([-128, -0, +0, 127], kind=int8), 127_int8)

   ! two arrays
   write(*, *)'compare two arrays'
   arr1=int( [ -127, -0, +0,  127], kind=int8 )
   arr2=int( [  127,  0,  0, -127], kind=int8 )
   write(*,*)'arr1=',arr1
   write(*,*)'arr2=',arr2
   write(*, *)'bge(arr1,arr2)=',bge( arr1, arr2 )

  ! SHOW TESTS AND BITS
   ! actually looking at the bit patterns should clarify what affect
   ! signs have ...
   write(*,*)'Compare some one-byte values to 64.'
   write(*,*)'Notice that the values are tested as bits not as integers'
   write(*,*)'so the results are as if values are unsigned integers.'
   do i=-128,127,32
      byte=i
      write(*,'(sp,i0.4,*(1x,1l,1x,b0.8))')i,bge(byte,64_int8),byte
   enddo

  ! SIGNED ZERO
   ! are +0 and -0 the same on your platform? When comparing at the
   ! bit level this is important
   write(*,'("plus zero=",b0)')  +0
   write(*,'("minus zero=",b0)') -0

end program demo_bge
```

Results:

How an integer value is represented at the bit level can vary. These
are just the values expected on Today's most common platforms ...

```text
    > bge(-127,127)= T
    > bge(b"0001",2)= F
    > compare array of values [-128, -0, +0, 127] to 127
    > T F F T
    > compare two arrays
    > arr1= -127    0    0  127
    > arr2=  127    0    0 -127
    > bge(arr1,arr2)= T T T F
    > Compare some one-byte values to 64.
    > Notice that the values are tested as bits not as integers
    > so the results are as if values are unsigned integers.
    > -0128  T 10000000
    > -0096  T 10100000
    > -0064  T 11000000
    > -0032  T 11100000
    > +0000  F 00000000
    > +0032  F 00100000
    > +0064  T 01000000
    > +0096  T 01100000
    > plus zero=0
    > minus zero=0
```

### **Standard**

Fortran 2008

### **See Also**

[**bgt**(3)](#bgt),
[**ble**(3)](#ble),
[**blt**(3)](#blt)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
