(popcnt)=
## popcnt

### **Name**

**popcnt**(3) - \[BIT:COUNT\] Number of bits set

### **Synopsis**

```fortran
    result = popcnt(i)
```

```fortran
     elemental integer function popcnt(i)

      integer(kind=KIND), intent(in) :: i
```

### **Characteristics**

- **i** may be an _integer_ of any kind.
- The return value is an _integer_ of the default integer kind.

### **Description**

**popcnt**(3) returns the number of bits set to one in the binary
representation of an _integer_.

### **Options**

- **i**
  : value to count set bits in

### **Result**

The number of bits set to one in **i**.

### **Examples**

Sample program:

```fortran
program demo_popcnt
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
   & int8, int16, int32, int64
implicit none
character(len=*),parameter :: pretty='(b64,1x,i0)'
  ! basic usage
   print pretty, 127,     popcnt(127)
   print pretty, int(b"01010"), popcnt(int(b"01010"))

  ! any kind of an integer can be used
   print pretty, huge(0_int8),  popcnt(huge(0_int8))
   print pretty, huge(0_int16), popcnt(huge(0_int16))
   print pretty, huge(0_int32), popcnt(huge(0_int32))
   print pretty, huge(0_int64), popcnt(huge(0_int64))
end program demo_popcnt
```

Results:

Note that on most machines the first bit is the sign bit, and a zero is
used for positive values; but that this is system-dependent. These are
typical values, where the huge(3f) function has set all but the first
bit to 1.

```text
 >                                                         1111111 7
 >                                                            1010 2
 >                                                         1111111 7
 >                                                 111111111111111 15
 >                                 1111111111111111111111111111111 31
 > 111111111111111111111111111111111111111111111111111111111111111 63
```

### **Standard**

Fortran 2008

### **See Also**

There are many procedures that operator or query values at the bit level:

[**poppar**(3)](#poppar),
[**leadz**(3)](#leadz),
[**trailz**(3)](#trailz)
[**atomic_and**(3)](#atomic_and),
[**atomic_fetch_and**(3)](#atomic_fetch_and),
[**atomic_fetch_or**(3)](#atomic_fetch_or),
[**atomic_fetch_xor**(3)](#atomic_fetch_xor),
[**atomic_or**(3)](#atomic_or),
[**atomic_xor**(3)](#atomic_xor),
[**bge**(3)](#bge),
[**bgt**(3)](#bgt),
[**bit_size**(3)](#bit_size),
[**ble**(3)](#ble),
[**blt**(3)](#blt),
[**btest**(3)](#btest),
[**dshiftl**(3)](#dshiftl),
[**dshiftr**(3)](#dshiftr),
[**iall**(3)](#iall),
[**iand**(3)](#iand),
[**iany**(3)](#iany),
[**ibclr**(3)](#ibclr),
[**ibits**(3)](#ibits),
[**ibset**(3)](#ibset),
[**ieor**(3)](#ieor),
[**ior**(3)](#ior),
[**iparity**(3)](#iparity),
[**ishftc**(3)](#ishftc),
[**ishft**(3)](#ishft),
[**maskl**(3)](#maskl),
[**maskr**(3)](#maskr),
[**merge_bits**(3)](#merge_bits),
[**mvbits**(3)](#mvbits),
[**not**(3)](#not),
[**shifta**(3)](#shifta),
[**shiftl**(3)](#shiftl),
[**shiftr**(3)](#shiftr),
[**storage_size**(3)](#storage_size)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
