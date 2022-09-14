## c_loc

### **Name**

**c_loc**(3) - \[ISO_C_BINDING\] Obtain the C address of an object

### **Syntax**

```fortran
result = c_loc(x)
```

### **Description**

**c_loc(x)** determines the C address of the argument.

### **Arguments**

- **x**
  : Shall have either the _pointer_ or _target_ attribute. It shall not be a
  coindexed object. It shall either be a variable with interoperable
  type and kind type parameters, or be a scalar, nonpolymorphic
  variable with no length type parameters.

### **Returns**

The return value is of type c_ptr and contains the C address of the
argument.

### **Examples**

Sample program:

```fortran
   subroutine association_test(a,b)
   use iso_c_binding, only: c_associated, c_loc, c_ptr
   implicit none
   real, pointer :: a
   type(c_ptr) :: b
     if(c_associated(b, c_loc(a))) &
        stop 'b and a do not point to same target'
   end subroutine association_test
```

### **Standard**

Fortran 2003 and later

### **See Also**

[**c_associated**(3)](C_ASSOCIATED),
[**c_funloc**(3)](C_FUNLOC),
[**c_f_pointer**(3)](C_F_POINTER),

[**c_f_procpointer**(3)](C_F_PROCPOINTER),
**iso_c_binding**(3)

_fortran-lang intrinsic descriptions_
