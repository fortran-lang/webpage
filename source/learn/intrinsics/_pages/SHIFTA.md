## shifta

### **Name**

**shifta**(3) - \[BIT:SHIFT\] shift bits right with fill

### **Syntax**

```fortran
result = shifta(i, shift)
```

### **Description**

Returns a value corresponding to **i** with all of the bits shifted right by
**shift** places. If the absolute value of **shift** is greater than
**bit_size(i)**, the value is undefined. Bits shifted out from the
right end are lost. The fill is arithmetic: the bits shifted in from the
left end are equal to the leftmost bit, which in two's complement
representation is the sign bit.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **shift**
  : The type shall be _integer_.

### **Returns**

The return value is of type _integer_ and of the same kind as **i**.

### **Standard**

Fortran 2008 and later

### **See Also**

[**shiftl**(3)](#shiftl),
[**shiftr**(3)](#shiftr)

 _fortran-lang intrinsic descriptions_
