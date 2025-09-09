(iand)=
## iand

### **Name**

**iand**(3) - \[BIT:LOGICAL\] Bitwise logical AND

### **Synopsis**

```fortran
    result = iand(i, j)
```

```fortran
     elemental integer(kind=KIND) function iand(i,j)

      integer(kind=KIND),intent(in) :: i
      integer(kind=KIND),intent(in) :: j
```

### **Characteristics**

- **i**, **j** and the result shall have the same _integer_ type and kind,
  with the exception that one of **i** or **j** may be a BOZ constant.

### **Description**

**iand**(3) returns the bitwise logical **and** of two values.

### **Options**

- **i**
  : one of the pair of values to compare the bits of

- **j**
  : one of the pair of values to compare the bits of

If either **i** or **j** is a BOZ-literal-constant, it is first converted
as if by the intrinsic function **int**(3) to type _integer_ with the
kind type parameter of the other.

### **Result**

The result has the value obtained by combining **i** and **i**
bit-by-bit according to the following table:

```text
    I  |  J  |  IAND (I, J)
  ----------------------------
    1  |  1  |    1
    1  |  0  |    0
    0  |  1  |    0
    0  |  0  |    0
```

So if both the bit in **i** and **j** are on the resulting bit is on
(a one); else the resulting bit is off (a zero).

This is commonly called the "bitwise logical AND" of the two values.

### **Examples**

Sample program:

```fortran
program demo_iand
implicit none
integer :: a, b
 data a / z'f' /, b / z'3' /
 write (*,*) 'a=',a,' b=',b,'iand(a,b)=',iand(a, b)
 write (*,'(b32.32)') a,b,iand(a,b)
end program demo_iand
```

Results:

```text
    a= 15  b= 3 iand(a,b)= 3
   00000000000000000000000000001111
   00000000000000000000000000000011
   00000000000000000000000000000011
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
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
