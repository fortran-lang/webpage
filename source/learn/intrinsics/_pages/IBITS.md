(ibits)=
## ibits

### **Name**

**ibits**(3) - \[BIT:COPY\] Extraction of a subset of bits

### **Synopsis**

```fortran
    result = ibits(i, pos, len)
```

```fortran
     elemental integer(kind=KIND) function ibits(i,pos,len)

      integer(kind=KIND),intent(in) :: i
      integer(kind=**),intent(in) :: pos
      integer(kind=**),intent(in) :: len
```

### **Characteristics**

- a kind designated as \*\* may be any supported _integer_ kind
- **i** may be any supported _integer_ kind as well
- the return value will be the same kind as **i**

### **Description**

**ibits**(3) extracts a field of bits from **i**, starting
from bit position **pos** and extending left for a total of **len** bits.

The result is then right-justified and the remaining left-most bits in the
result are zeroed.

The position **pos** is calculated assuming the right-most bit is zero and
the positions increment to the left.

### **Options**

- **i**
  : The value to extract bits from

- **pos**
  : The position of the bit to start copying at. **pos** is
  non-negative.

- **len**
  : the number of bits to copy from **i**. It must be non-negative.

**pos + len** shall be less than or equal to **bit_size(i)**.

### **Result**

The return value is composed of the selected bits right-justified,
left-padded with zeros.

### **Examples**

Sample program:

```fortran
program demo_ibits
use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
implicit none
integer(kind=int16) :: i,j
  ! basic usage
   print *,ibits (14, 1, 3) ! should be seven
   print *,ibits(-1,10,3)   ! and so is this
   ! it is easier to see using binary representation
   i=int(b'0101010101011101',kind=int16)
   write(*,'(b16.16,1x,i0)') ibits(i,3,3), ibits(i,3,3)

  ! we can illustrate this as
   !        #-- position 15
   !        |              #-- position 0
   !        |   <-- +len   |
   !        V              V
   !        5432109876543210
   i =int(b'1111111111111111',kind=int16)
   !          ^^^^
   j=ibits(i,10,4) ! start at 10th from left and proceed
                   ! left for a total of 4 characters
   write(*,'(a,b16.16)')'j=',j
  ! lets do something less ambiguous
   i =int(b'0010011000000000',kind=int16)
   j=ibits(i,9,5)
   write(*,'(a,b16.16)')'j=',j
end program demo_ibits
```

Results:

```text
 > 7
 > 7
 > 0000000000000011 3
 > j=0000000000001111
 > j=0000000000010011
```

### **Standard**

Fortran 95

### **See Also**

[**ieor**(3)](#ieor),
[**ibclr**(3)](#ibclr),
[**not**(3)](#not),
[**btest**(3)](#btest),
[**ibclr**(3)](#ibclr),
[**ibset**(3)](#ibset),
[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
