## ibits

### **Name**

**ibits**(3) - \[BIT:COPY\] Bit extraction

### **Syntax**

```fortran
result = ibits(i, pos, len)
```

### **Description**

**ibits** extracts a field of length **len** from **i**, starting from
bit position **pos** and extending left for **len** bits. The result is
right-justified and the remaining bits are zeroed. The value of pos+len
must be less than or equal to the value **bit_size(i)**.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **pos**
  : The type shall be _integer_. A value of zero refers to the least
  significant bit.

- **len**
  : The type shall be _integer_.

### **Returns**

The return value is of type _integer_ and of the same kind as **i**.

### **Standard**

Fortran 95 and later

### **See Also**

[**btest**(3)](BTEST),
[**iand**(3)](IAND),
[**ibclr**(3)](IBCLR),
[**ibset**(3)](IBSET),
[**ieor**(3)](IEOR),
[**ior**(3)](IOR),
[**not**(3)](NOT),
[**mvbits**(3)](MVBITS)

_fortran-lang intrinsic descriptions_
