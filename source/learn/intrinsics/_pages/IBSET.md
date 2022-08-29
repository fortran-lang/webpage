## ibset

### **Name**

**ibset**(3) - \[BIT:SET\] Set bit

### **Syntax**

```fortran
result = ibset(i, pos)
```

### **Description**

**ibset** returns the value of **i** with the bit at position **pos** set to one.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **pos**
  : The type shall be _integer_. A value of zero refers to the least
  significant bit. pos is an **intent(in)** scalar or array of type
  _integer_. The value of pos must be within the range zero to
  **(bit_size(i)-1**).

### **Returns**

The return value is of type _integer_ and of the same kind as **i**.

### **Standard**

Fortran 95 and later

### **See Also**

[**ieor**(3)](IEOR),
[**ibclr**(3)](IBCLR),
[**not**(3)](NOT),
[**btest**(3)](BTEST),
[**ibclr**(3)](IBCLR),
[**ibits**(3)](IBITS),
[**iand**(3)](IAND),
[**ior**(3)](IOR),
[**ieor**(3)](IEOR),
[**mvbits**(3)](MVBITS)

###### fortran-lang intrinsic descriptions
