(shiftr)=
## shiftr

### **Name**

**shiftr**(3) - \[BIT:SHIFT\] Shift bits right

### **Synopsis**

```fortran
    result = shiftr( i, shift )
```

```fortran
     elemental integer(kind=KIND) function shiftr(i, shift)

      integer(kind=KIND),intent(in) :: i
      integer(kind=**),intent(in) :: shift
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **i** is an _integer_ of any kind
- **shift** is an _integer_ of any kind
- the result will automatically be of the same type, kind and rank as **i**.

### **Description**

**shiftr**(3) returns a value corresponding to **i** with all of the
bits shifted right by **shift** places.

If the absolute value of **shift** is greater than **bit_size(i)**,
the value is undefined.

Bits shifted out from the right end are lost, and bits shifted in from
the left end are set to 0.

For example, for a 16-bit integer right-shifted five ...

```text
    >  |a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p| <- original 16-bit example
    >            |a|b|c|d|e|f|g|h|i|j|k| <- right-shifted five
    >  |0|0|0|0|0|f|g|h|i|j|k|l|m|n|o|p| <- left-padded with zeros
```

Note the value of the result is the same as **ishft (i, -shift)**.

### **Options**

- **i**
  : The value to shift

- **shift**
  : How many bits to shift right.
  It shall be nonnegative and less than or equal to **bit_size(i)**.

### **Result**

The remaining bits shifted right **shift** positions.
Vacated positions on the left are filled with zeros.

### **Examples**

Sample program:

```fortran
program demo_shiftr
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer             :: shift
integer(kind=int32) :: oval
integer(kind=int32) :: ival
integer(kind=int32),allocatable :: ivals(:)
integer             :: i

  print *,' basic usage'
  ival=100
  write(*,*)ival, shiftr(100,3)

  ! elemental (input values may be conformant arrays)
  print *,' elemental'
   shift=9
   ivals=[ &
   & int(b"01010101010101010101010101010101"), &
   & int(b"10101010101010101010101010101010"), &
   & int(b"11111111111111111111111111111111") ]

   write(*,'(/,"SHIFT =  ",i0)') shift
   do i=1,size(ivals)
      ! print initial value as binary and decimal
      write(*,'(  "I =      ",b32.32," == ",i0)') ivals(i),ivals(i)
      ! print shifted value as binary and decimal
      oval=shiftr(ivals(i),shift)
      write(*,'(  "RESULT = ",b32.32," == ",i0,/)') oval,oval
   enddo

   ! more on elemental
   ELEM : block
   integer(kind=int8)  :: arr(2,2)=reshape([2,4,8,16],[2,2])
   write(*,*)"characteristics of the result are the same as input"
   write(*,'(*(g0,1x))') &
     & "kind=",kind(shiftr(arr,3)), "shape=",shape(shiftr(arr,3)), &
     & "size=",size(shiftr(arr,3)) !, "rank=",rank(shiftr(arr,3))
   endblock ELEM

end program demo_shiftr
```

Results:

```text
  >    basic usage
  >           100          12
  >    elemental
  >
  >  SHIFT =  9
  >  I =      01010101010101010101010101010101 == 1431655765
  >  RESULT = 00000000001010101010101010101010 == 2796202
  >
  >  I =      10101010101010101010101010101010 == -1431655766
  >  RESULT = 00000000010101010101010101010101 == 5592405
  >
  >  I =      11111111111111111111111111111111 == -1
  >  RESULT = 00000000011111111111111111111111 == 8388607
  >
  >   characteristics of the result are the same as input
  >  kind= 1 shape= 2 2 size= 4
```

### **Standard**

Fortran 2008

### **See Also**

[**shifta**(3)](#shifta),
[**shiftl**(3)](#shiftl),
[**ishft**(3)](#ishft),
[**ishftc**(3)](#ishftc)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
