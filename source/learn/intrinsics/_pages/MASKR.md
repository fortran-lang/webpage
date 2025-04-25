(maskr)=
## maskr

### **Name**

**maskr**(3) - \[BIT:SET\] Generates a right-justified mask

### **Synopsis**

```fortran
    result = maskr( i [,kind] )
```

```fortran
     elemental integer(kind=KIND) function maskr(i,KIND)

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

**maskr**(3) generates an _integer_ with its rightmost **i**
bits set to 1, and the remaining bits set to 0.

### **Options**

- **i**
  : the number of right-most bits to set in the _integer_ result. It
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

The rightmost **i** bits of the output _integer_ are set to 1 and the
other bits are set to 0.

### **Examples**

Sample program:

```fortran
program demo_maskr
implicit none
integer :: i

  ! basics
   print *,'basics'
   write(*,'(i0,t5,b32.32)') 1, maskr(1)
   write(*,'(i0,t5,b32.32)') 5,  maskr(5)
   write(*,'(i0,t5,b32.32)') 11, maskr(11)
   print *,"should be equivalent on two's-complement processors"
   write(*,'(i0,t5,b32.32)') 1,  shiftr(-1,bit_size(0)-1)
   write(*,'(i0,t5,b32.32)') 5,  shiftr(-1,bit_size(0)-5)
   write(*,'(i0,t5,b32.32)') 11, shiftr(-1,bit_size(0)-11)

  ! elemental
   print *,'elemental '
   print *,'(array argument accepted like called with each element)'
   write(*,'(*(i11,1x,b0.32,1x,/))') maskr([(i,i,i=0,bit_size(0),4)])

end program demo_maskr
```

Results:

```text
 >   basics
 >  1   00000000000000000000000000000001
 >  5   00000000000000000000000000011111
 >  11  00000000000000000000011111111111
 >   should be equivalent on two's-complement processors
 >  1   00000000000000000000000000000001
 >  5   00000000000000000000000000011111
 >  11  00000000000000000000011111111111
 >   elemental
 >   (array argument accepted like called with each element)
 >            0 00000000000000000000000000000000
 >           15 00000000000000000000000000001111
 >          255 00000000000000000000000011111111
 >         4095 00000000000000000000111111111111
 >        65535 00000000000000001111111111111111
 >      1048575 00000000000011111111111111111111
 >     16777215 00000000111111111111111111111111
 >    268435455 00001111111111111111111111111111
 >           -1 11111111111111111111111111111111
```

### **Standard**

Fortran 2008

### **See Also**

[**maskl**(3)](#maskl)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
