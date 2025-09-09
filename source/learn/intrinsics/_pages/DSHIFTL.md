(dshiftl)=
## dshiftl

### **Name**

**dshiftl**(3) - \[BIT:COPY\] Combined left shift of the bits of two integers

### **Synopsis**

```fortran
    result = dshiftl(i, j, shift)
```

```fortran
     elemental integer(kind=KIND) function dshiftl(i, j, shift)

      integer(kind=KIND),intent(in) :: i
      integer(kind=KIND),intent(in) :: j
      integer(kind=**),intent(in) :: shift
```

### **Characteristics**

- the kind of **i**, **j**, and the return value are the same. An
  exception is that one of **i** and **j** may be a BOZ literal constant
  (A BOZ literal constant is a binary, octal or hex constant).

- If either I or J is a BOZ-literal-constant (but not both), it is
  first converted as if by the intrinsic function **int**(3) to type
  _integer_ with the kind type parameter of the other.

- a kind designated as \*\* may be any supported kind for the type

### **Description**

**dshiftl**(3) combines bits of **i** and **j**. The rightmost **shift**
bits of the result are the leftmost **shift** bits of **j**, and the
remaining bits are the rightmost **bitsize(i)-shift** of **i**.

Hence **dshiftl** is designated as a "combined left shift", because
it is like we appended **i** and **j** together, shifted it **shift**
bits to the left, and then kept the same number of bits as **i** or
**j** had.

For example, for two 16-bit values if **shift=6**

```text
      SHIFT=6
      I =             1111111111111111
      J =             0000000000000000
      COMBINED        11111111111111110000000000000000
      DROP LEFT BITS  11111111110000000000000000
      KEEP LEFT 16    1111111111000000
```

#### NOTE

This is equivalent to

```fortran
     ior( shiftl(i, shift), shiftr(j, bit_size(j) - shift) )
```

Also note that using this last representation of the operation is can
be derived that when both **i** and **j** have the same value as in

```fortran
      dshiftl(i, i, shift)
```

the result has the same value as a circular shift:

```fortran
      ishftc(i, shift)
```

### **Options**

- **i**
  : used to define the left pattern of bits in the combined pattern

- **j**
  : used for the right pattern of bits in the combined pattern

- **shift**
  : shall be nonnegative and less than or equal to the number of bits
  in an _integer_ input value (ie. the bit size of either one that is
  not a BOZ literal constant).

### **Result**

The leftmost **shift** bits of **j** are copied to the rightmost bits
of the result, and the remaining bits are the rightmost bits of **i**.

### **Examples**

Sample program:

```fortran
program demo_dshiftl
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer(kind=int32) :: i, j
integer             :: shift

  ! basic usage
   write(*,*) dshiftl (1, 2**30, 2) ! int32 values on little-endian => 5

  ! print some simple calls as binary to better visual the results
   i=-1
   j=0
   shift=5
   call printit()

   ! the leftmost SHIFT bits of J are copied to the rightmost result bits
   j=int(b"11111000000000000000000000000000")
   ! and the other bits are the rightmost bits of I
   i=int(b"00000000000000000000000000000000")
   call printit()

   j=int(b"11111000000000000000000000000000")
   i=int(b"00000111111111111111111111111111")
   ! result should be all 1s
   call printit()

contains
subroutine printit()
   ! print i,j,shift and then i,j, and the result as binary values
    write(*,'(*(g0))')'I=',i,' J=',j,' SHIFT=',shift
    write(*,'(b32.32)') i,j, dshiftl (i, j, shift)
end subroutine printit

end program demo_dshiftl
```

Results:

```text
   > I=-1 J=0 SHIFT=5
   > 11111111111111111111111111111111
   > 00000000000000000000000000000000
   > 11111111111111111111111111100000
   > I=0 J=-134217728 SHIFT=5
   > 00000000000000000000000000000000
   > 11111000000000000000000000000000
   > 00000000000000000000000000011111
   > I=134217727 J=-134217728 SHIFT=5
   > 00000111111111111111111111111111
   > 11111000000000000000000000000000
   > 11111111111111111111111111111111
```

### **Standard**

Fortran 2008

### **See Also**

[**dshiftr**(3)](#dshiftr)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
