(dshiftr)=
## dshiftr

### **Name**

**dshiftr**(3) - \[BIT:COPY\] Combined right shift of the bits of two integers

### **Synopsis**

```fortran
    result = dshiftr(i, j, shift)
```

```fortran
     elemental integer(kind=KIND) function dshiftr(i, j, shift)

      integer(kind=KIND),intent(in) :: i
      integer(kind=KIND),intent(in) :: j
      integer(kind=**),intent(in) :: shift
```

### **Characteristics**

- a kind designated as \*\* may be any kind value for the _integer_ type

- the kind of **i**, **j**, and the return value are the same. An
  exception is that one of **i** and **j** may be a BOZ literal constant
  (A BOZ literal constant is a binary, octal or hex constant).

- If either I or J is a BOZ-literal-constant, it is first converted
  as if by the intrinsic function **int**(3) to type _integer_ with the
  kind type parameter of the other.

### **Description**

**dshiftr**(3) combines bits of **i** and **j**. The leftmost **shift**
bits of the result are the rightmost **shift** bits of **i**, and the
remaining bits are the leftmost bits of **j**.

It may be thought of as appending the bits of **i** and **j**, dropping
off the **shift** rightmost bits, and then retaining the same number
of rightmost bits as an input value, hence the name "combined right
shift"...

Given two 16-bit values labeled alphabetically ...

```text
   i=ABCDEFGHIJKLMNOP
   j=abcdefghijklmnop
```

Append them together

```text
   ABCDEFGHIJKLMNOPabcdefghijklmnop
```

Shift them N=6 bits to the right dropping off bits

```text
         ABCDEFGHIJKLMNOPabcdefghij
```

Keep the 16 right-most bits

```text
                   KLMNOPabcdefghij
```

#### NOTE

**dshifr(i,j,shift)** is equivalent to

```fortran
     ior(shiftl (i, bit_size(i) - shift), shiftr(j, shift) )
```

it can also be seen that if **i** and **j** have the same
value

```fortran
     dshiftr( i, i, shift )
```

this has the same result as a negative circular shift

```fortran
     ishftc( i,   -shift ).
```

### **Options**

- **i**
  : left value of the pair of values to be combine-shifted right

- **j**
  : right value of the pair of values to be combine-shifted right

- **shift**
  : the shift value is non-negative and less than or equal to the number
  of bits in an input value as can be computed by **bit_size**(3).

### **Result**

The result is a combined right shift of **i** and **j** that is the
same as the bit patterns of the inputs being combined left to right,
dropping off **shift** bits on the right and then retaining the same
number of bits as an input value from the rightmost bits.

### **Examples**

Sample program:

```fortran
program demo_dshiftr
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
implicit none
integer(kind=int32) :: i, j
integer             :: shift

  ! basic usage
   write(*,*) dshiftr (1, 2**30, 2)

  ! print some calls as binary to better visualize the results
   i=-1
   j=0
   shift=5

   ! print values
    write(*,'(*(g0))')'I=',i,' J=',j,' SHIFT=',shift
    write(*,'(b32.32)') i,j, dshiftr (i, j, shift)

  ! visualizing a "combined right shift" ...
   i=int(b"00000000000000000000000000011111")
   j=int(b"11111111111111111111111111100000")
   ! appended together ( i//j )
   ! 0000000000000000000000000001111111111111111111111111111111100000
   ! shifted right SHIFT values dropping off shifted values
   !      00000000000000000000000000011111111111111111111111111111111
   ! keep enough rightmost bits to fill the kind
   !                                 11111111111111111111111111111111
   ! so the result should be all 1s bits ...

    write(*,'(*(g0))')'I=',i,' J=',j,' SHIFT=',shift
    write(*,'(b32.32)') i,j, dshiftr (i, j, shift)

end program demo_dshiftr
```

Results:

```text
 >    1342177280
 >  I=-1 J=0 SHIFT=5
 >  11111111111111111111111111111111
 >  00000000000000000000000000000000
 >  11111000000000000000000000000000
 >  I=31 J=-32 SHIFT=5
 >  00000000000000000000000000011111
 >  11111111111111111111111111100000
 >  11111111111111111111111111111111
```

### **Standard**

Fortran 2008

### **See Also**

[**dshiftl**(3)](#dshiftl)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
