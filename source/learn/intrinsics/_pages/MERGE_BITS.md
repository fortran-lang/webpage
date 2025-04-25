(merge_bits)=
## merge_bits

### **Name**

**merge_bits**(3) - \[BIT:COPY\] Merge bits using a mask

### **Synopsis**

```fortran
    result = merge_bits(i, j, mask)
```

```fortran
     elemental integer(kind=KIND) function merge_bits(i,j,mask)

      integer(kind=KIND), intent(in) :: i, j, mask
```

### **Characteristics**

- the result and all input values have the same _integer_ type and
  KIND with the exception that the mask and either **i** or **j** may be
  a BOZ constant.

### **Description**

A common graphics operation in Ternary Raster Operations is to combine
bits from two different sources, generally referred to as bit-blending.
**merge_bits**(3) performs a masked bit-blend of **i** and **j** using
the bits of the **mask** value to determine which of the input values
to copy bits from.

Specifically, The k-th bit of the result is equal to the k-th bit of
**i** if the k-th bit of **mask** is **1**; it is equal to the k-th bit
of **j** otherwise (so all three input values must have the same number
of bits).

The resulting value is the same as would result from

```fortran
    ior (iand (i, mask),iand (j, not (mask)))
```

An exception to all values being of the same _integer_ type is that **i**
or **j** and/or the mask may be a BOZ constant (A BOZ constant means it is
either a Binary, Octal, or Hexadecimal literal constant). The BOZ values
are converted to the _integer_ type of the non-BOZ value(s) as if called
by the intrinsic function **int()** with the kind of the non-BOZ value(s),
so the BOZ values must be in the range of the type of the result.

### **Options**

- **i**
  : value to select bits from when the associated bit in the mask is **1**.

- **j**
  : value to select bits from when the associated bit in the mask is **0**.

- **mask**
  : a value whose bits are used as a mask to select bits from **i** and **j**

### **Result**

The bits blended from **i** and **j** using the mask **mask**.

### **Examples**

Sample program:

```fortran
program demo_merge_bits
use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
implicit none
integer(kind=int16) :: if_one,if_zero,msk
character(len=*),parameter :: fmt='(*(g0, 1X))'

   ! basic usage
   print *,'MERGE_BITS( 5,10,41) should be 3.=>',merge_bits(5,10,41)
   print *,'MERGE_BITS(13,18,22) should be 4.=>',merge_bits(13,18,22)

   ! use some values in base2 illustratively:
   if_one =int(b'1010101010101010',kind=int16)
   if_zero=int(b'0101010101010101',kind=int16)

   msk=int(b'0101010101010101',kind=int16)
   print '("should get all zero bits =>",b16.16)', &
   & merge_bits(if_one,if_zero,msk)

   msk=int(b'1010101010101010',kind=int16)
   print '("should get all ones bits =>",b16.16)', &
   & merge_bits(if_one,if_zero,msk)

   ! using BOZ values
   print fmt, &
   & merge_bits(32767_int16,    o'12345',         32767_int16), &
   & merge_bits(o'12345', 32767_int16, b'0000000000010101'), &
   & merge_bits(32767_int16,    o'12345',             z'1234')

   ! a do-it-yourself equivalent for comparison and validation
   print fmt, &
   & ior(iand(32767_int16, 32767_int16),                   &
   &   iand(o'12345', not(32767_int16))),                  &

   & ior(iand(o'12345', int(o'12345', kind=int16)),        &
   &   iand(32767_int16, not(int(o'12345', kind=int16)))), &

   & ior(iand(32767_int16, z'1234'),                       &
   &   iand(o'12345', not(int( z'1234', kind=int16))))

end program demo_merge_bits
```

Results:

```text
    MERGE_BITS( 5,10,41) should be 3.=>           3
    MERGE_BITS(13,18,22) should be 4.=>           4
   should get all zero bits =>0000000000000000
   should get all ones bits =>1111111111111111
   32767 32751 5877
   32767 32767 5877
```

### **Standard**

Fortran 2008

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
