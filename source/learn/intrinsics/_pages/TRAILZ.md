(trailz)=
## trailz

### **Name**

**trailz**(3) - \[BIT:COUNT\] Number of trailing zero bits of an integer

### **Synopsis**

```fortran
 result = trailz(i)
```

```fortran
  elemental integer function trailz(i)

   integer(kind=**),intent(in) :: i
```

### **Characteristics**

- **i** is an _integer_ of any kind.
- the result is an _integer_ of default kind

### **Description**

**trailz**(3) returns the number of trailing zero bits of an _integer_
value.

### **Options**

- **i**
  : the value to count trailing zero bits in

### **Result**

The number of trailing rightmost zero bits in an _integer_ value after
the last non-zero bit.

```text
       >      right-most non-zero bit
       >                 V
       >  |0|0|0|1|1|1|0|1|0|0|0|0|0|0|
       >  ^               |___________| trailing zero bits
       >   bit_size(i)
```

If all the bits of **i** are zero, the result is the size of the input
value in bits, ie. **bit_size(i)**.

The result may also be seen as the position of the rightmost 1 bit
in **i**, starting with the rightmost bit being zero and counting to
the left.

### **Examples**

Sample program:

```fortran
program demo_trailz

! some common integer kinds
use, intrinsic :: iso_fortran_env, only : &
 & integer_kinds, int8, int16, int32, int64

implicit none

! a handy format
character(len=*),parameter :: &
 & show = '(1x,"value=",i4,", value(bits)=",b32.32,1x,", trailz=",i3)'

integer(kind=int64) :: bigi
  ! basics
   write(*,*)'Note default integer is',bit_size(0),'bits'
   print  show,  -1, -1,  trailz(-1)
   print  show,   0,  0,  trailz(0)
   print  show,   1,  1,  trailz(1)
   print  show,  96, 96,  trailz(96)
  ! elemental
   print *, 'elemental and any integer kind:'
   bigi=2**5
   write(*,*) trailz( [ bigi, bigi*256, bigi/2 ] )
   write(*,'(1x,b64.64)')[ bigi, bigi*256, bigi/2 ]

end program demo_trailz
```

Results:

```text
    Note default integer is          32 bits
    value=  -1, value(bits)=11111111111111111111111111111111 , trailz=  0
    value=   0, value(bits)=00000000000000000000000000000000 , trailz= 32
    value=   1, value(bits)=00000000000000000000000000000001 , trailz=  0
    value=  96, value(bits)=00000000000000000000000001100000 , trailz=  5
    elemental and any integer kind:
              5          13           4
    0000000000000000000000000000000000000000000000000000000000100000
    0000000000000000000000000000000000000000000000000010000000000000
    0000000000000000000000000000000000000000000000000000000000010000
```

### **Standard**

Fortran 2008

### **See Also**

[**bit_size**(3)](#bit_size),
[**popcnt**(3)](#popcnt),
[**poppar**(3)](#poppar),
[**leadz**(3)](#leadz)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
