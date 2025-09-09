(co_ubound)=
## co_ubound

### **Name**

**co_ubound**(3) - \[COLLECTIVE\] Upper codimension bounds of an array

### **Synopsis**

```fortran
    result = co_ubound(coarray [,dim] [,kind] )
```

```fortran

```

### **Characteristics**

### **Description**

**co_ubound**(3) returns the upper cobounds of a coarray, or a single
upper cobound along the **dim** codimension.

### **Options**

- **array**
  : Shall be an coarray, of any type.

- **dim**
  : (Optional) Shall be a scalar _integer_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Result**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default integer kind. If **dim** is absent, the
result is an array of the lower cobounds of **coarray**. If **dim** is present,
the result is a scalar corresponding to the lower cobound of the array
along that codimension.

### **Standard**

Fortran 2008

### **See Also**

[**co_lbound**(3)](#co_lbound),
[**lbound**(3)](#lbound),
[**ubound**(3)](#ubound)

_fortran-lang intrinsic descriptions_
