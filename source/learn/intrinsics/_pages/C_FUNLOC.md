(c_funloc)=
## c_funloc

### **Name**

**c_funloc**(3) - \[ISO_C_BINDING\] Obtain the C address of a procedure

### **Synopsis**

```fortran
    result = c_funloc(x)
```

```fortran

```

### **Characteristics**

### **Description**

**c_funloc**(3) determines the C address of the argument.

### **Options**

- **x**
  : Interoperable function or pointer to such function.

### **Result**

The return value is of type c_funptr and contains the C address of the
argument.

### **Examples**

Sample program:

```fortran
! program demo_c_funloc and module
module x
use iso_c_binding
implicit none
contains
subroutine sub(a) bind(c)
real(c_float) :: a
   a = sqrt(a)+5.0
end subroutine sub
end module x
!
program demo_c_funloc
use iso_c_binding
use x
implicit none
interface
   subroutine my_routine(p) bind(c,name='myC_func')
     import :: c_funptr
     type(c_funptr), intent(in) :: p
   end subroutine
end interface
   call my_routine(c_funloc(sub))
!
end program demo_c_funloc
```

### **Standard**

Fortran 2003

### **See Also**

[**c_associated**(3)](#c_associated),
[**c_loc**(3)](#c_loc),
[**c_f_pointer**(3)](#c_f_pointer),

[**c_f_procpointer**(3)](#c_f_procpointer),
**iso_c_binding**(3)

_fortran-lang intrinsic descriptions_
