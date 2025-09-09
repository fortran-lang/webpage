(leadz)=
## leadz

### **Name**

**leadz**(3) - \[BIT:COUNT\] Number of leading zero bits of an integer

### **Synopsis**

```fortran
    result = leadz(i)
```

```fortran
     elemental integer function leadz(i)

      integer(kind=**),intent(in) :: i
```

### **Characteristics**

- **i** may be an _integer_ of any kind.
- the return value is a default integer type.

### **Description**

**leadz**(3) returns the number of leading zero bits of an integer.

### **Options**

- **i**
  : _integer_ to count the leading zero bits of.

### **Result**

The number of leading zero bits, taking into account the kind of the
input value. If all the bits of **i** are zero, the result value is
**bit_size(i)**.

The result may also be thought of as **bit_size(i)-1-k** where **k**
is the position of the leftmost 1 bit in the input **i**. Positions
are from 0 to bit-size(), with 0 at the right-most bit.

### **Examples**

Sample program:

```fortran
program demo_leadz
implicit none
integer :: value, i
character(len=80) :: f

  ! make a format statement for writing a value as a bit string
  write(f,'("(b",i0,".",i0,")")')bit_size(value),bit_size(value)

  ! show output for various integer values
  value=0
  do i=-150, 150, 50
     value=i
     write (*,'("LEADING ZERO BITS=",i3)',advance='no') leadz(value)
     write (*,'(" OF VALUE ")',advance='no')
     write(*,f,advance='no') value
     write(*,'(*(1x,g0))') "AKA",value
  enddo
  ! Notes:
  ! for two's-complements programming environments a negative non-zero
  ! integer value will always start with a 1 and a positive value with 0
  ! as the first bit is the sign bit. Such platforms are very common.
end program demo_leadz
```

Results:

```text
  LEADING ZERO BITS=  0 OF VALUE 11111111111111111111111101101010 AKA -150
  LEADING ZERO BITS=  0 OF VALUE 11111111111111111111111110011100 AKA -100
  LEADING ZERO BITS=  0 OF VALUE 11111111111111111111111111001110 AKA -50
  LEADING ZERO BITS= 32 OF VALUE 00000000000000000000000000000000 AKA 0
  LEADING ZERO BITS= 26 OF VALUE 00000000000000000000000000110010 AKA 50
  LEADING ZERO BITS= 25 OF VALUE 00000000000000000000000001100100 AKA 100
  LEADING ZERO BITS= 24 OF VALUE 00000000000000000000000010010110 AKA 150
```

### **Standard**

Fortran 2008

### **See Also**

[**bit_size**(3)](#bit_size),
[**popcnt**(3)](#popcnt),
[**poppar**(3)](#poppar),
[**trailz**(3)](#trailz)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
