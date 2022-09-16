## c_sizeof

### **Name**

**c_sizeof**(3) - \[ISO_C_BINDING\] Size in bytes of an expression

### **Syntax**

```fortran
n = c_sizeof(x)
```

### **Description**

**c_sizeof(x)** calculates the number of bytes of storage the
expression **x** occupies.

### **Arguments**

- **x**
  : The argument shall be an interoperable data entity.

### **Returns**

The return value is of type integer and of the system-dependent kind
c*size_t (from the \_iso_c_binding* module). Its value is the
number of bytes occupied by the argument. If the argument has the
_pointer_ attribute, the number of bytes of the storage area pointed to is
returned. If the argument is of a derived type with _pointer_ or
_allocatable_ components, the return value does not account for the sizes
of the data pointed to by these components.

### **Examples**

Sample program:

```fortran
program demo_c_sizeof
use iso_c_binding
implicit none
real(c_float) :: r, s(5)
   print *, (c_sizeof(s)/c_sizeof(r) == 5)
end program demo_c_sizeof
```

Results:

```text
    T
```

The example will print .true. unless you are using a platform where
default _real_ variables are unusually padded.

### **Standard**

Fortran 2008

### **See Also**

[**storage_size**(3)](#storage_size)

 _fortran-lang intrinsic descriptions_
