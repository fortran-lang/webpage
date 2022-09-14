## storage_size

### **Name**

**storage_size**(3) - \[BIT:INQUIRY\] Storage size in bits

### **Syntax**

```fortran
result = storage_size(a, kind)
```

### **Description**

Returns the storage size of argument **a** in bits.

### **Arguments**

- **a**
  : Shall be a scalar or array of any type.

- **kind**
  : (Optional) shall be a scalar integer constant expression.

### **Returns**

The result is a scalar integer with the kind type parameter specified by
**kind** (or default integer type if **kind** is missing). The result value is
the size expressed in bits for an element of an array that has the
dynamic type and type parameters of **a**.

### **Examples**

Sample program

```fortran
program demo_storage_size
implicit none
   write(*,*)'size of integer       ',storage_size(0)
   write(*,*)'size of real          ',storage_size(0.0)
   write(*,*)'size of logical       ',storage_size(.true.)
   write(*,*)'size of complex       ',storage_size((0.0,0.0))
   write(*,*)'size of integer array ',storage_size([0,1,2,3,4,5,6,7,8,9])
end program demo_storage_size
```

Results:

```text
    size of integer                 32
    size of real                    32
    size of logical                 32
    size of complex                 64
    size of integer array           32
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**c_sizeof**(3)](C_SIZEOF)

_fortran-lang intrinsic descriptions_
