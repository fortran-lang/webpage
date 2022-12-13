## c_associated

### **Name**

**c_associated**(3) - \[ISO_C_BINDING\] Status of a C pointer

### **Syntax**

```fortran
result = c_associated(c_prt_1, c_ptr_2)
```

### **Description**

**c_associated(c_prt_1\[, c_ptr_2\])** determines the status of the
C pointer c_ptr_1 or if c_ptr_1 is associated with the target
c_ptr_2.

### **Arguments**

- **c_ptr_1**
  : Scalar of the type c_ptr or c_funptr.

- **c_ptr_2**
  : (Optional) Scalar of the same type as c_ptr_1.

### **Returns**

The return value is of type _logical_; it is .false. if either c_ptr_1
is a C NULL pointer or if c_ptr1 and c_ptr_2 point to different
addresses.

### **Examples**

Sample program:

```fortran
program demo_c_associated

contains

subroutine association_test(a,b)
use iso_c_binding, only: c_associated, c_loc, c_ptr
implicit none
real, pointer :: a
type(c_ptr) :: b
   if(c_associated(b, c_loc(a))) &
      stop 'b and a do not point to same target'
end subroutine association_test

end program demo_c_associated
```

### **Standard**

Fortran 2003 and later

### **See Also**

[**c_loc**(3)](#c_loc),
[**c_funloc**(3)](#c_funloc),
**iso_c_binding**(3)

 _fortran-lang intrinsic descriptions_
