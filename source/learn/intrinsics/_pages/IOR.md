(ior)=
## ior

### **Name**

**ior**(3) - \[BIT:LOGICAL\] Bitwise logical inclusive OR

### **Synopsis**

```fortran
    result = ior(i, j)
```

```fortran
     elemental integer(kind=KIND) function ior(i,j)

      integer(kind=KIND ,intent(in) :: i
      integer(kind=KIND ,intent(in) :: j
```

### **Characteristics**

- **i**, **j** and the result shall have the same _integer_ type and kind,
  with the exception that one of **i** or **j** may be a BOZ constant.

### **Description**

**ior**(3) returns the bit-wise Boolean inclusive-or of **i** and **j**.

### **Options**

- **i**
  : one of the pair of values to compare the bits of

- **j**
  : one of the pair of values to compare the bits of

If either **i** or **j** is a BOZ-literal-constant, it is first converted
as if by the intrinsic function **int**(3) to type _integer_ with the
kind type parameter of the other.

### **Result**

The result has the value obtained by combining I and J
bit-by-bit according to the following table:

```text
          I   J   IOR (I, J)
          1   1        1
          1   0        1
          0   1        1
          0   0        0
```

Where if the bit is set in either input value, it is set in the
result. Otherwise the result bit is zero.

This is commonly called the "bitwise logical inclusive OR" of the two values.

### **Examples**

Sample program:

```fortran
program demo_ior
implicit none
integer :: i, j, k
   i=53       ! i=00110101 binary (lowest order byte)
   j=45       ! j=00101101 binary (lowest order byte)
   k=ior(i,j) ! k=00111101 binary (lowest order byte), k=61 decimal
   write(*,'(i8,1x,b8.8)')i,i,j,j,k,k
end program demo_ior
```

Results:

```
         53 00110101
         45 00101101
         61 00111101
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
[**ieor**(3)](#ieor),
[**mvbits**(3)](#mvbits)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
