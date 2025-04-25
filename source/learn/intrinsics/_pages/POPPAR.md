(poppar)=
## poppar

### **Name**

**poppar**(3) - \[BIT:COUNT\] Parity of the number of bits set

### **Synopsis**

```fortran
    result = poppar(i)
```

```fortran
     elemental integer function poppar(i)

      integer(kind=KIND), intent(in) :: i
```

### **Characteristics**

- **i** is an _integer_ of any kind
- the return value is a default kind _integer_

### **Description**

**poppar**(3) returns the parity of an integer's binary representation
(i.e., the parity of the number of bits set).

The parity is expressed as

- **0** (zero) if **i** has an even number of bits set to **1**.
- **1** (one) if the number of bits set to one **1** is odd,

### **Options**

- **i**
  : The value to query for its bit parity

### **Result**

The return value is equal to **0** if **i** has an even number of bits
set and **1** if an odd number of bits are set.

### **Examples**

Sample program:

```fortran
program demo_poppar
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
   & int8, int16, int32, int64
implicit none
character(len=*),parameter :: pretty='(b64,1x,i0)'
   ! basic usage
   print pretty, 127,     poppar(127)
   print pretty, 128,     poppar(128)
   print pretty, int(b"01010"), poppar(int(b"01010"))

   ! any kind of an integer can be used
   print pretty, huge(0_int8),  poppar(huge(0_int8))
   print pretty, huge(0_int16), poppar(huge(0_int16))
   print pretty, huge(0_int32), poppar(huge(0_int32))
   print pretty, huge(0_int64), poppar(huge(0_int64))
end program demo_poppar
```

Results:

```text
 >                                                          1111111 1
 >                                                         10000000 1
 >                                                             1010 0
 >                                  1111111111111111111111111111111 1
 >                                                          1111111 1
 >                                                  111111111111111 1
 >                                  1111111111111111111111111111111 1
 >  111111111111111111111111111111111111111111111111111111111111111 1
```

### **Standard**

Fortran 2008

### **See Also**

There are many procedures that operator or query values at the bit level:

[**popcnt**(3)](#popcnt),
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
