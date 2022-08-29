## ishft

### **Name**

**ishft**(3) - \[BIT:SHIFT\] Shift bits

### **Syntax**

```fortran
result = ishft(i, shift)
```

### **Description**

**ishft**(3) returns a value corresponding to **i** with all of the bits shifted
**shift** places. A value of **shift** greater than zero corresponds to a left
shift, a value of zero corresponds to no shift, and a value less than
zero corresponds to a right shift. If the absolute value of **shift** is
greater than **bit_size(i)**, the value is undefined. Bits shifted out
from the left end or right end are lost; zeros are shifted in from the
opposite end.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **shift**
  : The type shall be _integer_.

### **Returns**

The return value is of type _integer_ and of the same kind as **i**.

### **Standard**

Fortran 95 and later

### **See Also**

[**ishftc**(3)](ISHFTC)

###### fortran-lang intrinsic descriptions
