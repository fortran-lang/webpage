(btest)=
## btest

### **Name**

**btest**(3) - \[BIT:INQUIRY\] Tests a bit of an _integer_ value.

### **Synopsis**

```fortran
    result = btest(i,pos)
```

```fortran
     elemental logical function btest(i,pos)

      integer(kind=**),intent(in)  :: i
      integer(kind=**),intent(in)  :: pos
```

### **Characteristics**

- **i** is an _integer_ of any kind
- **pos** is a _integer_ of any kind
- the result is a default logical

### **Description**

**btest**(3) returns logical _.true._ if the bit at **pos** in **i** is
set to 1. Position zero is the right-most bit. Bit position increases
from right to left up to **bitsize(i)-1**.

### **Options**

- **i**
  : The _integer_ containing the bit to be tested

- **pos**
  : The position of the bit to query. it must be a valid position for the
  value **i**; ie. **0 <= pos <= bit_size(i)**.

### **Result**

The result is a _logical_ that has the value _.true._ if bit position
**pos** of **i** has the value **1** and the value _.false._ if bit
**pos** of **i** has the value **0**.

Positions of bits in the sequence are numbered from right to left,
with the position of the rightmost bit being zero.

### **Examples**

Sample program:

```fortran
program demo_btest
implicit none
integer :: i, j, pos, a(2,2)
logical :: bool
character(len=*),parameter :: g='(*(g0))'

     i = 32768 + 1024 + 64
    write(*,'(a,i0,"=>",b32.32,/)')'Looking at the integer: ',i

    ! looking one bit at a time from LOW BIT TO HIGH BIT
    write(*,g)'from bit 0 to bit ',bit_size(i),'==>'
    do pos=0,bit_size(i)-1
        bool = btest(i, pos)
        write(*,'(l1)',advance='no')bool
    enddo
    write(*,*)

    ! a binary format the hard way.
    ! Note going from bit_size(i) to zero.
    write(*,*)
    write(*,g)'so for ',i,' with a bit size of ',bit_size(i)
    write(*,'(b32.32)')i
    write(*,g)merge('^','_',[(btest(i,j),j=bit_size(i)-1,0,-1)])
    write(*,*)
    write(*,g)'and for ',-i,' with a bit size of ',bit_size(i)
    write(*,'(b32.32)')-i
    write(*,g)merge('^','_',[(btest(-i,j),j=bit_size(i)-1,0,-1)])

    ! elemental:
    !
    a(1,:)=[ 1, 2 ]
    a(2,:)=[ 3, 4 ]
    write(*,*)
    write(*,'(a,/,*(i2,1x,i2,/))')'given the array a ...',a
    ! the second bit of all the values in a
    write(*,'(a,/,*(l2,1x,l2,/))')'the value of btest (a, 2)',btest(a,2)
    ! bits 1,2,3,4 of the value 2
    write(*,'(a,/,*(l2,1x,l2,/))')'the value of btest (2, a)',btest(2,a)
end program demo_btest
```

Results:

```text
  > Looking at the integer: 33856=>11111111111111110111101111000000
  >
  > 00000000000000001000010001000000
  > 11111111111111110111101111000000
  > 1000010001000000
  > 11111111111111110111101111000000
  > from bit 0 to bit 32==>
  > FFFFFFTFFFTFFFFTFFFFFFFFFFFFFFFF
  >
  > so for 33856 with a bit size of 32
  > 00000000000000001000010001000000
  > ________________^____^___^______
  >
  > and for -33856 with a bit size of 32
  > 11111111111111110111101111000000
  > ^^^^^^^^^^^^^^^^_^^^^_^^^^______
  >
  > given the array a ...
  >  1  3
  >  2  4
  >
  > the value of btest (a, 2)
  >  F  F
  >  F  T
  >
  > the value of btest (2, a)
  >  T  F
  >  F  F
```

### **Standard**

Fortran 95

### **See Also**

[**ieor**(3)](#ieor),
[**ibclr**(3)](#ibclr),
[**not**(3)](#not),
[**ibclr**(3)](#ibclr),
[**ibits**(3)](#ibits),
[**ibset**(3)](#ibset),
[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
