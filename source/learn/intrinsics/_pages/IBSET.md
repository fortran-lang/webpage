(ibset)=
## ibset

### **Name**

**ibset**(3) - \[BIT:SET\] Set a bit to one in an integer value

### **Synopsis**

```fortran
    result = ibset(i, pos)
```

```fortran
     elemental integer(kind=KIND) function ibset(i,pos)

      integer(kind=KIND),intent(in) :: i
      integer(kind=**),intent(in) :: pos
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- The return value is of the same kind as **i**. Otherwise,
  any _integer_ kinds are allowed.

### **Description**

**ibset**(3) returns the value of **i** with the bit at position **pos** set to one.

### **Options**

- **i**
  : The initial value to be modified

- **pos**
  : The position of the bit to change in the input value. A value
  of zero refers to the right-most bit. The value of **pos** must be
  nonnegative and less than **(bit_size(i)**).

### **Result**

The returned value has the same bit sequence as **i** except the
designated bit is unconditionally set to **1**.

### **Examples**

Sample program:

```fortran
program demo_ibset
use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
implicit none
integer(kind=int16) :: i
  ! basic usage
   print *,ibset (12, 1), 'ibset(12,1) has the value 14'

   ! it is easier to see using binary representation
   i=int(b'0000000000000110',kind=int16)
   write(*,'(b16.16,1x,i0,1x,i0)') ibset(i,12), ibset(i,12), i

  ! elemental
   print *,'an array of initial values may be given as well'
   print *,ibset(i=[0,4096], pos=2)
   print *
   print *,'a list of positions results in multiple returned values'
   print *,'not multiple bits set in one value, as the routine is  '
   print *,'a scalar function; calling it elementally essentially  '
   print *,'calls it multiple times.                               '
   write(*,'(b16.16)') ibset(i=0, pos=[1,2,3,4])

   ! both may be arrays if of the same size

end program demo_ibset
```

Results:

```text
 >           14 ibset(12,1) has the value 14
 > 0001000000000110 4102 6
 >  an array of initial values may be given as well
 >            4        4100
 >
 >  a list of positions results in multiple returned values
 >  not multiple bits set in one value, as the routine is
 >  a scalar function; calling it elementally essentially
 >  calls it multiple times.
 > 0000000000000010
 > 0000000000000100
 > 0000000000001000
 > 0000000000010000
```

### **Standard**

Fortran 95

### **See Also**

[**ibclr**(3)](#ibclr)

[**ieor**(3)](#ieor),
[**not**(3)](#not),
[**btest**(3)](#btest),
[**ibits**(3)](#ibits),
[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
