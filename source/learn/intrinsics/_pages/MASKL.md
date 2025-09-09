(maskl)=
## maskl

### **Name**

**maskl**(3) - \[BIT:SET\] Generates a left justified mask

### **Synopsis**

```fortran
    result = maskl( i [,kind] )
```

```fortran
     elemental integer(kind=KIND) function maskl(i,KIND)

      integer(kind=**),intent(in) :: i
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **i** is an integer
- **kind** Shall be a scalar constant expression of type _integer_
  whose value is a supported _integer_ kind.
- The result is an _integer_ of the same _kind_ as **i** unless **kind** is
  present, which is then used to specify the kind of the result.

### **Description**

**maskl**(3) has its leftmost **i** bits set to **1**, and the remaining
bits set to **0**.

### **Options**

- **i**
  : the number of left-most bits to set in the _integer_ result. It
  must be from 0 to the number of bits for the kind of the result.
  The default kind of the result is the same as **i** unless the result
  size is specified by **kind**. That is, these Fortran statements must
  be _.true._ :

```fortran
   i >= 0 .and. i < bitsize(i) ! if KIND is not specified
   i >= 0 .and. i < bitsize(0_KIND) ! if KIND is specified
```

- **kind**
  : designates the kind of the _integer_ result.

### **Result**

The leftmost **i** bits of the output _integer_ are set to 1 and the
other bits are set to 0.

### **Examples**

Sample program:

```fortran
program demo_maskl
implicit none
integer :: i
  ! basics
   i=3
   write(*,'(i0,1x,b0)') i, maskl(i)

  ! elemental
   write(*,'(*(i11,1x,b0.32,1x,/))') maskl([(i,i,i=0,bit_size(0),4)])
end program demo_maskl
```

Results:

```text
 > 3 11100000000000000000000000000000
 >           0 00000000000000000000000000000000
 >  -268435456 11110000000000000000000000000000
 >   -16777216 11111111000000000000000000000000
 >    -1048576 11111111111100000000000000000000
 >      -65536 11111111111111110000000000000000
 >       -4096 11111111111111111111000000000000
 >        -256 11111111111111111111111100000000
 >         -16 11111111111111111111111111110000
 >          -1 11111111111111111111111111111111

```

### **Standard**

Fortran 2008

### **See Also**

[**maskr**(3)](#maskr)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
