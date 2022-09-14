## extends_type_of

### **Name**

**extends_type_of**(3) - \[STATE\] determine if the dynamic type of **a** is an extension of the dynamic type of **mold**.

### **Syntax**

```fortran
result=extends_type_of(a, mold)
```

### **Description**

**extends_type_of**(3) is **.true.** if and only if the dynamic type of **a**
is an extension of the dynamic type of **mold**.

### **Options**

- **a**
  : shall be an object of extensible type. If it is a pointer, it
  shall not have an undefined association status.

- **mold**
  : shall be an object of extensible type. If it is a pointer, it
  shall not have an undefined association status.

### **Returns**

- **result**
  : Default logical scalar.

- **value**
  : If **mold** is unlimited polymorphic and is either a disassociated
  pointer or unallocated allocatable variable, the result is
  true; otherwise if **a** is unlimited polymorphic and is either a
  disassociated pointer or unallocated allocatable variable, the result
  is false; otherwise the result is true if and only if the dynamic
  type of **a** is an extension type of the dynamic type of **mold**.

  The dynamic type of a disassociated pointer or unallocated
  allocatable variable is its declared type.

### **Examples**

_fortran-lang intrinsic descriptions_
