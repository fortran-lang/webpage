## ishftc

### **Name**

**ishftc**(3) - \[BIT:SHIFT\] Shift bits circularly

### **Syntax**

```fortran
result = ishftc(i, shift, size)
```

### **Description**

**ishftc**(3) returns a value corresponding to **i** with the rightmost **size** bits
shifted circularly **shift** places; that is, bits shifted out one end are
shifted into the opposite end. A value of **shift** greater than zero
corresponds to a left shift, a value of zero corresponds to no shift,
and a value less than zero corresponds to a right shift. The absolute
value of **shift** must be less than **size**. If the **size** argument is omitted,
it is taken to be equivalent to **bit_size(i)**.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **shift**
  : The type shall be _integer_.

- **size**
  : (Optional) The type shall be _integer_; the value must be greater than
  zero and less than or equal to **bit_size**(i).

### **Returns**

The return value is of type _integer_ and of the same kind as **i**.

### **Standard**

Fortran 95 and later

### **See Also**

[**ishft**(3)](#ishft)

 _fortran-lang intrinsic descriptions_
