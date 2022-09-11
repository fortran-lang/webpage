## bgt

### **Name**

**bgt**(3) - \[BIT:COMPARE\] Bitwise greater than

### **Syntax**

```fortran
    result = bgt(i, j)
```

### **Description**

Determines whether an integer is bitwise greater than another.

### **Arguments**

- **i**
  : Shall be of _integer_ type or a BOZ literal constant.

- **j**
  : Shall be of _integer_ type, and of the same kind as **i**; or a BOZ
  literal constant.

### **Returns**

The return value is of type _logical_ and of the default kind. The result
is true if the sequence of bits represented by _i_ is greater than the
sequence of bits represented by _j_, otherwise the result is false.

### **Standard**

Fortran 2008 and later

### **See Also**

[**bge**(3)](BGE),
[**ble**(3)](BLE),
[**blt**(3)](BLT)

###### fortran-lang intrinsic descriptions
