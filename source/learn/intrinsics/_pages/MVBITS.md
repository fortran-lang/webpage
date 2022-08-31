## mvbits

### **Name**

**mvbits**(3) - \[BIT:COPY\] reproduce bit patterns found in one integer in another

### **Syntax**

```fortran
call mvbits(from, frompos, len, to, topos)
```

### **Description**

**mvbits(3f)** copies a bit pattern found in a range of adjacent bits in
the _integer_ **from** to a specified position in another integer **to**
(which is of the same kind as **from**). It otherwise leaves the bits
in **to** as-is.

The bit positions copied must exist within the value of **from**.
That is, the values of **frompos+len-1** and **topos+len-1** must be
nonnegative and less than **bit_size**(from).

The bits are numbered **0** to **bit_size(i)-1**, from right to left.

### **Arguments**

- **from**
  : An _integer_ to read bits from.
- **frompos**
  : **frompos** is the position of the first bit to copy. It is a
  nonnegative _integer_ value < **bit_size(from)**.
- **len**
  : A nonnegative _integer_ value that indicates how many bits to
  copy from **from**. It must not specify copying bits past the end
  of **from**. That is, **frompos + len** must be less than or equal
  to **bit_size(from)**.
- **to**
  : The _integer_ variable to place the copied bits into. It must
  be of the same kind as **from** and may even be the same variable
  as **from**.

  **to**
  : is set by copying the sequence of bits of length **len**,
  starting at position **frompos** of **from** to position **topos** of
  **to**. No other bits of **to** are altered. On return, the **len**
  bits of **to** starting at **topos** are equal to the value that
  the **len** bits of **from** starting at **frompos** had on entry.

- **topos**
  : A nonnegative _integer_ value indicating the starting location in
  **to** to place the specified copy of bits from **from**.
  **topos + len** must be less than or equal to **bit_size(to)**.

### **Example**

Sample program that populates a new 32-bit integer with its bytes in
reverse order (ie. changes the Endian of the integer).

      program demo_mvbits
      use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
      implicit none
      integer(kind=int32) :: intfrom, intto, abcd_int
      character(len=*),parameter :: bits= '(g0,t30,b32.32)'
      character(len=*),parameter :: fmt= '(g0,t30,a,t40,b32.32)'

         intfrom=huge(0)  ! all bits are 1 accept the sign bit
     intto=0          ! all bits are 0

         !! CHANGE BIT 0
         ! show the value and bit pattern
         write(*,bits)intfrom,intfrom
         write(*,bits)intto,intto

         ! copy bit 0 from intfrom to intto to show the rightmost bit changes
         !          (from,    frompos, len,    to, topos)
         call mvbits(intfrom,       0,   1, intto,     0) ! change bit 0
         write(*,bits)intto,intto

         !! COPY PART OF A VALUE TO ITSELF
     call mvbits(intfrom,0,1,intfrom,31) ! can copy bit from a value to itself
         write(*,bits)intfrom,intfrom

         !! MOVING BYTES AT A TIME
         ! make native integer value with bit patterns
         ! that happen to be the same as the beginning of the alphabet
     ! to make it easy to see the bytes are reversed
         abcd_int=transfer('abcd',0)
         ! show the value and bit pattern
         write(*,*)'native'
         write(*,fmt)abcd_int,abcd_int,abcd_int

         ! change endian of the value
         abcd_int=int_swap32(abcd_int)
         ! show the values and their bit pattern
         write(*,*)'non-native'
         write(*,fmt)abcd_int,abcd_int,abcd_int

      contains

      pure elemental function int_swap32(intin) result(intout)
      ! Convert a 32 bit integer from big Endian to little Endian,
      ! or conversely from little Endian to big Endian.
      !
      integer(kind=int32), intent(in)  :: intin
      integer(kind=int32) :: intout
         ! copy bytes from input value to new position in output value
         !          (from,  frompos, len,     to, topos)
         call mvbits(intin,       0,   8, intout,    24) ! byte1 to byte4
         call mvbits(intin,       8,   8, intout,    16) ! byte2 to byte3
         call mvbits(intin,      16,   8, intout,     8) ! byte3 to byte2
         call mvbits(intin,      24,   8, intout,     0) ! byte4 to byte1
      end function int_swap32

      end program demo_mvbits

````
  Results:
```text

   2147483647                   01111111111111111111111111111111
   0                            00000000000000000000000000000000
   1                            00000000000000000000000000000001
   -1                           11111111111111111111111111111111
    native
   1684234849                   abcd      01100100011000110110001001100001
    non-native
   1633837924                   dcba      01100001011000100110001101100100
================================================================================
````

### **Standard**

Fortran 95 and later

### **See Also**

[**ieor**(3)](IEOR),
[**ibclr**(3)](IBCLR),
[**not**(3)](NOT),
[**btest**(3)](BTEST),
[**ibclr**(3)](IBCLR),
[**ibits**(3)](IBITS),
[**ibset**(3)](IBSET),
[**iand**(3)](IAND),
[**ior**(3)](IOR),
[**ieor**(3)](IEOR)

###### fortran-lang intrinsic descriptions (license MIT) @urbanjost
