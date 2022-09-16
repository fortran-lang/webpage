## btest

### **Name**

**btest**(3) - \[BIT:INQUIRY\] Tests a bit of an _integer_ value.

### **Syntax**

```fortran
   result = btest(i, pos)

    integer(kind=KIND) elemental function btest(i,pos)
    integer,intent(in)  :: i
    logical,intent(out) :: pos
```

where **KIND** is any _integer_ kind supported by the programming environment.

### **Description**

**btest(i,pos)** returns logical **.true.** if the bit at **pos** in **i** is set.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **pos**
  : The bit position to query. it must be a valid position for the
  value **i**; ie. **0 <= pos <= bit_size(i)** .

  A value of zero refers to the least significant bit.

### **Returns**

The result is a _logical_ that has the value **.true.** if bit
position **pos** of **i** has the value **1** and the value
**.false.** if bit **pos** of **i** has the value **0**.

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
Looking at the integer: 33856=>11111111111111110111101111000000

00000000000000001000010001000000
11111111111111110111101111000000
1000010001000000
11111111111111110111101111000000
from bit 0 to bit 32==>
FFFFFFTFFFTFFFFTFFFFFFFFFFFFFFFF

so for 33856 with a bit size of 32
00000000000000001000010001000000
________________^____^___^______

and for -33856 with a bit size of 32
11111111111111110111101111000000
^^^^^^^^^^^^^^^^_^^^^_^^^^______

given the array a ...
 1  3
 2  4

the value of btest (a, 2)
 F  F
 F  T

the value of btest (2, a)
 T  F
 F  F
```

### **Standard**

Fortran 95 and later

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
