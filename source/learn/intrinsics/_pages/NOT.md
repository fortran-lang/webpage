(not)=
## not

### **Name**

**not**(3) - \[BIT:LOGICAL\] Logical negation; flips all bits in an integer

### **Synopsis**

```fortran
    result = not(i)
```

```fortran
    elemental integer(kind=KIND) function not(i)

     integer(kind=KIND), intent(in) :: i
```

### **Characteristics**

- **i** may be an _integer_ of any valid kind
- The returned _integer_ is of the same kind as the argument **i**.

### **Description**

**not**(3) returns the bitwise Boolean inverse of **i**. This is also
known as the "Bitwise complement" or "Logical negation" of the value.

If an input bit is a one, that position is a zero on output. Conversely
any input bit that is zero is a one on output.

### **Options**

- **i**
  : The value to flip the bits of.

### **Result**

The result has the value obtained by complementing **i** bit-by-bit
according to the following truth table:

       >    I   |  NOT(I)
       >    ----#----------
       >    1   |   0
       >    0   |   1

That is, every input bit is flipped.

### **Examples**

Sample program

```fortran
program demo_not
implicit none
integer :: i
  ! basics
   i=-13741
   print *,'the input value',i,'represented in bits is'
   write(*,'(1x,b32.32,1x,i0)') i, i
   i=not(i)
   print *,'on output it is',i
   write(*,'(1x,b32.32,1x,i0)') i, i
   print *, " on a two's complement machine flip the bits and add 1"
   print *, " to get the value with the sign changed, for example."
   print *, 1234, not(1234)+1
   print *, -1234, not(-1234)+1
   print *, " of course 'x=-x' works just fine and more generally."
end program demo_not
```

Results:

```text
    the input value      -13741 represented in bits is
    11111111111111111100101001010011 -13741
    on output it is       13740
    00000000000000000011010110101100 13740
     on a two's complement machine flip the bits and add 1
     to get the value with the sign changed, for example.
           1234       -1234
          -1234        1234
     of course 'x=-x' works just fine and more generally.
```

### **Standard**

Fortran 95

### **See Also**

[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**ibits**(3)](#ibits),
[**ibset**(3)](#ibset),

[**ibclr**(3)](#ibclr)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
