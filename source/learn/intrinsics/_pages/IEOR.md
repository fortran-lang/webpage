(ieor)=
## ieor

### **Name**

**ieor**(3) - \[BIT:LOGICAL\] Bitwise exclusive OR

### **Synopsis**

```fortran
    result = ieor(i, j)
```

```fortran
     elemental integer(kind=**) function ieor(i,j)

      integer(kind=**),intent(in) :: i
      integer(kind=**),intent(in) :: j
```

### **Characteristics**

- **i**, **j** and the result must be of the same _integer_ kind.
- An exception is that one of **i** and **j** may be a BOZ literal
  constant

### **Description**

**ieor**(3) returns a bitwise exclusive-**or** of **i** and **j**.

An exclusive OR or "exclusive disjunction" is a logical operation that
is true if and only if its arguments differ. In this case a one-bit
and a zero-bit substitute for true and false.

This is often represented with the notation "XOR", for "eXclusive OR".

An alternate way to view the process is that the result has the value
obtained by combining **i** and **j** bit-by-bit according to the
following table:

      >  I | J |IEOR (I, J)
      >  --#---#-----------
      >  1 | 1 |  0
      >  1 | 0 |  1
      >  0 | 1 |  1
      >  0 | 0 |  0

### **Options**

- **i**
  : the first of the two values to XOR

- **j**
  : the second of the two values to XOR

If either I or J is a boz-literal-constant, it is first converted
as if by the intrinsic function INT to type integer with the kind
type parameter of the other.

### **Result**

If a bit is different at the same location in **i** and **j**
the corresponding bit in the result is **1**, otherwise it is **0**.

### **Examples**

Sample program:

```fortran
program demo_ieor
use,intrinsic :: iso_fortran_env,  only : int8, int16, int32, int64
implicit none
integer(kind=int16) :: i,j
  ! basic usage
   print *,ieor (16, 1), ' ==> ieor(16,1) has the value 17'

   ! it is easier to see using binary representation
   i=int(b'0000000000111111',kind=int16)
   j=int(b'0000001111110000',kind=int16)
   write(*,'(a,b16.16,1x,i0)')'i=     ',i, i
   write(*,'(a,b16.16,1x,i0)')'j=     ',j, j
   write(*,'(a,b16.16,1x,i0)')'result=',ieor(i,j), ieor(i,j)

  ! elemental
   print *,'arguments may be arrays. If both are arrays they '
   print *,'must have the same shape.                        '
   print *,ieor(i=[7,4096,9], j=2)

   ! both may be arrays if of the same size

end program demo_ieor
```

Results:

```text
 >           17  ==> ieor(16,1) has the value 17
 > i=     0000000000111111 63
 > j=     0000001111110000 1008
 > result=0000001111001111 975
 >  arguments may be arrays. If both are arrays they
 >  must have the same shape.
 >            5        4098          11
```

### **Standard**

Fortran 95

### **See Also**

[**ieor**(3)](#ieor),
[**ibclr**(3)](#ibclr),
[**not**(3)](#not),
[**btest**(3)](#btest),
[**ibclr**(3)](#ibclr),
[**ibits**(3)](#ibits),
[**ibset**(3)](#ibset),
[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
