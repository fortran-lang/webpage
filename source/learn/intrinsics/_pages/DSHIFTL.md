## dshiftl

### **Name**

**dshiftl**(3) - \[BIT:COPY\] combines bits of arguments **i** and **j**

### **Syntax**

```fortran
result = dshiftl(i, j, shift)
```

### **Description**

**dshiftl(i, j, shift)** combines bits of **i** and **j**. The rightmost **shift**
bits of the result are the leftmost **shift** bits of **j**, and the remaining
bits are the rightmost bits of **i**.

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

[**dshiftr**(3)](DSHIFTR)

###### fortran-lang intrinsic descriptions
