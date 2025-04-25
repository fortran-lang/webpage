(ibclr)=
## ibclr

### **Name**

**ibclr**(3) - \[BIT:SET\] Clear a bit

### **Synopsis**

```fortran
    result = ibclr(i, pos)
```

```fortran
     elemental integer(kind=KIND) function ibclr(i,pos)

      integer(kind=KIND),intent(in) :: i
      integer(kind=**),intent(in) :: pos
```

### **Characteristics**

- **i** shall be type _integer_.
- **pos** shall be type _integer_.
- The return value is of the same kind as **i**.

- a kind designated as \*\* may be any supported kind for the type

### **Description**

**ibclr**(3) returns the value of **i** with the bit at position **pos**
set to zero.

### **Options**

- **i**
  : The initial value to be modified

- **pos**
  : The position of the bit to change in the input value. A value
  of zero refers to the right-most bit. The value of **pos** must be
  nonnegative and less than **(bit_size(i)**).

### **Result**

The returned value has the same bit sequence as **i** except the
designated bit is unconditionally set to **0**

### **Examples**

Sample program:

```fortran
program demo_ibclr
use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
implicit none
integer(kind=int16) :: i
  ! basic usage
   print *,ibclr (16, 1), ' ==> ibclr(16,1) has the value 15'

   ! it is easier to see using binary representation
   i=int(b'0000000000111111',kind=int16)
   write(*,'(b16.16,1x,i0)') ibclr(i,3), ibclr(i,3)

  ! elemental
   print *,'an array of initial values may be given as well'
   print *,ibclr(i=[7,4096,9], pos=2)
   print *
   print *,'a list of positions results in multiple returned values'
   print *,'not multiple bits set in one value, as the routine is  '
   print *,'a scalar function; calling it elementally essentially  '
   print *,'calls it multiple times.                               '
   write(*,'(b16.16)') ibclr(i=-1_int16, pos=[1,2,3,4])

   ! both may be arrays if of the same size

end program demo_ibclr
```

Results:

```text
 >           16  ==> ibclr(16,1) has the value 15
 > 0000000000110111 55
 >  an array of initial values may be given as well
 >            3        4096           9
 >
 >  a list of positions results in multiple returned values
 >  not multiple bits set in one value, as the routine is
 >  a scalar function; calling it elementally essentially
 >  calls it multiple times.
 > 1111111111111101
 > 1111111111111011
 > 1111111111110111
 > 1111111111101111
```

### **Standard**

Fortran 95

### **See Also**

[**ieor**(3)](#ieor),
[**not**(3)](#not),
[**btest**(3)](#btest),
[**ibset**(3)](#ibclr),
[**ibits**(3)](#ibits),
[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
