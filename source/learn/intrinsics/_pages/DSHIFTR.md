## dshiftr

### **Name**

**dshiftr**(3) - \[BIT:COPY\] combines bits of arguments **i** and **j**

### **Syntax**

```fortran
result = dshiftr(i, j, shift)
```

### **Description**

**dshiftr(i, j, shift)** combines bits of **i** and **j**. The leftmost **shift**
bits of the result are the rightmost **shift** bits of **i**, and the remaining
bits are the leftmost bits of **j**.

### **Arguments**

- **i**
  : Shall be of type _integer_.

- **j**
  : Shall be of type _integer_, and of the same kind as **i**.

- **shift**
  : Shall be of type _integer_.

### **Returns**

The return value has same type and kind as **i**.

### **Standard**

Fortran 2008 and later

### **See Also**

[**dshiftl**(3)](DSHIFTL)

_fortran-lang intrinsic descriptions_
