(ishftc)=
## ishftc

### **Name**

**ishftc**(3) - \[BIT:SHIFT\] Shift rightmost bits circularly, AKA. a logical shift

### **Synopsis**

```fortran
    result = ishftc( i, shift [,size] )
```

```fortran
     elemental integer(kind=KIND) function ishftc(i, shift, size)

      integer(kind=KIND),intent(in)        :: i
      integer(kind=**),intent(in)          :: shift
      integer(kind=**),intent(in),optional :: size
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **i** may be an _integer_ of any kind
- **shift** and **size** may be _integers_ of any kind
- the kind for **i** dictates the kind of the returned value.

### **Description**

**ishftc**(3) circularly shifts just the specified rightmost bits of
an integer.

**ishftc**(3) returns a value corresponding to **i** with the rightmost
**size** bits shifted circularly **shift** places; that is, bits
shifted out one end of the section are shifted into the opposite end
of the section.

A value of **shift** greater than zero corresponds to a left shift,
a value of zero corresponds to no shift, and a value less than zero
corresponds to a right shift.

### **Options**

- **i**
  : The value specifying the pattern of bits to shift

- **shift**
  : If **shift** is positive, the shift is to the left; if **shift**
  is negative, the shift is to the right; and if **shift** is zero,
  no shift is performed.

  The absolute value of **shift** must be less than **size** (simply
  put, the number of positions to shift must be less than or equal to
  the number of bits specified to be shifted).

- **size**
  : The value must be greater than zero and less than or equal to
  **bit_size**(i).

  The default if **bit_size(i)** is absent is to circularly shift the
  entire value **i**.

### **Result**

The result characteristics (kind, shape, size, rank, ...) are the
same as **i**.

The result has the value obtained by shifting the **size** rightmost
bits of **i** circularly by **shift** positions.

No bits are lost.

The unshifted bits are unaltered.

### **Examples**

Sample program:

```fortran
program demo_ishftc
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer             :: i
character(len=*),parameter :: g='(b32.32,1x,i0)'
  ! basics
   write(*,*) ishftc(3, 1),' <== typically should have the value 6'

   print *, 'lets start with this:'
   write(*,'(b32.32)')huge(0)
   print *, 'shift the value by various amounts, negative and positive'
   do i= -bit_size(0), bit_size(0), 8
      write(*,g) ishftc(huge(0),i), i
   enddo
  print *,'elemental'
  i=huge(0)
  write(*,*)ishftc(i,[2,3,4,5])
  write(*,*)ishftc([2**1,2**3,-2**7],3)
  print *,'note the arrays have to conform when elemental'
  write(*,*)ishftc([2**1,2**3,-2**7],[5,20,0])

end program demo_ishftc
```

Results:

```text
 >            6  <== typically should have the value 6
 >  lets start with this:
 > 01111111111111111111111111111111
 >  shift the value by various amounts, negative and positive
 > 01111111111111111111111111111111 -32
 > 11111111111111111111111101111111 -24
 > 11111111111111110111111111111111 -16
 > 11111111011111111111111111111111 -8
 > 01111111111111111111111111111111 0
 > 11111111111111111111111101111111 8
 > 11111111111111110111111111111111 16
 > 11111111011111111111111111111111 24
 > 01111111111111111111111111111111 32
 >  elemental
 >           -3          -5          -9         -17
 >           16          64       -1017
 >  note the arrays have to conform when elemental
 >           64     8388608        -128
```

### **Standard**

Fortran 95

### **See Also**

- [**ishft**(3)](#ishft) - Logical shift of bits in an integer
- [**shifta**(3)](#shifta) - Right shift with fill
- [**shiftl**(3)](#shiftl) - Shift bits left
- [**shiftr**(3)](#shiftr) - Combined right shift of the bits of two int...
- [**dshiftl**(3)](#dshiftl) - Combined left shift of the bits of two inte...
- [**dshiftr**(3)](#dshiftr) - Combined right shift of the bits of two int...
- [**cshift**(3)](#cshift) - Circular shift elements of an array
- [**eoshift**(3)](#eoshift) - End-off shift elements of an array

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
