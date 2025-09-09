(c_loc)=
## c_loc

### **Name**

**c_loc**(3) - \[ISO_C_BINDING\] Obtain the C address of an object

### **Synopsis**

```fortran
    result = c_loc(x)
```

```fortran

```

### **Characteristics**

### **Description**

**c_loc**(3) determines the C address of the argument.

### **Options**

- **x**
  : Shall have either the _pointer_ or _target_ attribute. It shall not be a
  coindexed object. It shall either be a variable with interoperable
  type and kind type parameters, or be a scalar, nonpolymorphic
  variable with no length type parameters.

### **Result**

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

Fortran 2003

### **See Also**

[**c_associated**(3)](#c_associated),
[**c_funloc**(3)](#c_funloc),
[**c_f_pointer**(3)](#c_f_pointer),

[**c_f_procpointer**(3)](#c_f_procpointer),
**iso_c_binding**(3)

_fortran-lang intrinsic descriptions_
