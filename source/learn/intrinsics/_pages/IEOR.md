## ieor

### **Name**

**ieor**(3) - \[BIT:LOGICAL\] Bitwise logical exclusive or

### **Syntax**

```fortran
result = ieor(i, j)
```

### **Description**

**ieor** returns the bitwise Boolean exclusive-**or** of **i** and **j**.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **j**
  : The type shall be _integer_, of the same kind as **i**.

### **Returns**

The return type is _integer_, of the same kind as the arguments. (If the
argument kinds differ, it is of the same kind as the larger argument.)

### **Standard**

Fortran 95 and later

### **See Also**

[**btest**(3)](BTEST),
[**iand**(3)](IAND),
[**ibclr**(3)](IBCLR),
[**ibits**(3)](IBITS),
[**ibset**(3)](IBSET),
[**ieor**(3)](IEOR),
[**ior**(3)](IOR),
[**not**(3)](NOT),
[**mvbits**(3)](MVBITS)

_fortran-lang intrinsic descriptions_
