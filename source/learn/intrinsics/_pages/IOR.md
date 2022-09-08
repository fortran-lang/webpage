## ior

### **Name**

**ior**(3) - \[BIT:LOGICAL\] Bitwise logical inclusive or

### **Syntax**

```fortran
   result = ior(i, j)
    integer,intent(in) :: i
    integer,intent(in) :: j
```

### **Description**

**ior** returns the bit-wise Boolean inclusive-**or** of **i** and **j**.

### **Arguments**

- **i**
  : an _integer_ scalar or array.

- **j**
  : _integer_ scalar or array, of the same kind as **i**.

### **Returns**

The return type is _integer_, of the same kind as the arguments. (If the
argument kinds differ, it is of the same kind as the larger argument.)

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

Fortran 95 and later

### **See Also**

[**ieor**(3)](IEOR),
[**ibclr**(3)](IBCLR),
[**not**(3)](NOT),
[**btest**(3)](BTEST),
[**ibclr**(3)](IBCLR),
[**ibits**(3)](IBITS),
[**ibset**(3)](IBSET),
[**iand**(3)](IAND),
[**ieor**(3)](IEOR),
[**mvbits**(3)](MVBITS)

###### fortran-lang intrinsic descriptions
