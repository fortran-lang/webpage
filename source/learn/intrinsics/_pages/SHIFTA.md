(shifta)=
## shifta

### **Name**

**shifta**(3) - \[BIT:SHIFT\] Right shift with fill

### **Synopsis**

```fortran
    result = shifta(i, shift )
```

```fortran
     elemental integer(kind=KIND) function shifta(i, shift)

      integer(kind=KIND),intent(in) :: i
      integer(kind=**),intent(in) :: shift
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **i** is an _integer_ of any kind
- **shift** is an _integer_ of any kind
- the result will automatically be of the same type, kind and rank as **i**.

### **Description**

**shifta**(3) returns a value corresponding to **i** with all of the
bits shifted right by **shift** places and the vacated bits on the
left filled with the value of the original left-most bit.

### **Options**

- **i**
  : The initial value to shift and fill

- **shift**
  : how many bits to shift right.
  It shall be nonnegative and less than or equal to **bit_size(i)**.
  or the value is undefined. If **shift** is zero the result is **i**.

### **Result**

The result has the value obtained by shifting the bits of **i** to
the right **shift** bits and replicating the leftmost bit of **i**
in the left **shift** bits (Note the leftmost bit in "two's complement"
representation is the sign bit).

Bits shifted out from the right end are lost.

If **shift** is zero the result is **i**.

### **Examples**

Sample program:

```fortran
program demo_shifta
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer(kind=int32) :: ival
integer             :: shift
integer(kind=int32) :: oval
integer(kind=int32),allocatable :: ivals(:)
integer             :: i
integer(kind=int8)  :: arr(2,2)=reshape([2,4,8,16],[2,2])

  ! basic usage
  write(*,*)shifta(100,3)

  ! loop through some interesting values
   shift=5

   ivals=[ -1, -0, +0, +1, &
   & int(b"01010101010101010101010101010101"), &
   & int(b"10101010101010101010101010101010"), &
   & int(b"00000000000000000000000000011111") ]

   ! does your platform distinguish between +0 and -0?
   ! note the original leftmost bit is used to fill in the vacated bits

   write(*,'(/,"SHIFT =  ",i0)') shift
   do i=1,size(ivals)
      ival=ivals(i)
      write(*,'(  "I =      ",b32.32," == ",i0)') ival,ival
      oval=shifta(ival,shift)
      write(*,'(  "RESULT = ",b32.32," == ",i0)') oval,oval
   enddo
   ! elemental
   write(*,*)"characteristics of the result are the same as input"
   write(*,'(*(g0,1x))') &
     & "kind=",kind(shifta(arr,3)), "shape=",shape(shifta(arr,3)), &
     & "size=",size(shifta(arr,3)) !, "rank=",rank(shifta(arr,3))

end program demo_shifta
```

Results:

```text
 >           12
 >
 > SHIFT =  5
 > I =      11111111111111111111111111111111 == -1
 > RESULT = 11111111111111111111111111111111 == -1
 > I =      00000000000000000000000000000000 == 0
 > RESULT = 00000000000000000000000000000000 == 0
 > I =      00000000000000000000000000000000 == 0
 > RESULT = 00000000000000000000000000000000 == 0
 > I =      00000000000000000000000000000001 == 1
 > RESULT = 00000000000000000000000000000000 == 0
 > I =      01010101010101010101010101010101 == 1431655765
 > RESULT = 00000010101010101010101010101010 == 44739242
 > I =      10101010101010101010101010101010 == -1431655766
 > RESULT = 11111101010101010101010101010101 == -44739243
 > I =      00000000000000000000000000011111 == 31
 > RESULT = 00000000000000000000000000000000 == 0
 >  characteristics of the result are the same as input
 > kind= 1 shape= 2 2 size= 4
```

### **Standard**

Fortran 2008

### **See Also**

[**shiftl**(3)](#shiftl),
[**shiftr**(3)](#shiftr),
[**ishft**(3)](#ishft),
[**ishftc**(3)](#ishftc)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
