(c_f_pointer)=
## c_f_pointer

### **Name**

**c_f_pointer**(3) - \[ISO_C_BINDING\] Convert C into Fortran pointer

### **Synopsis**

```fortran
    call c_f_pointer(cptr, fptr [,shape] )
```

```fortran
     subroutine c_f_pointer(cptr, fptr ,shape )

      type(c_ptr),intent(in) :: cprt
      type(TYPE),pointer,intent(out) :: fprt
      integer,intent(in),optional :: shape(:)
```

### **Characteristics**

The Fortran pointer **fprt** must be interoperable with **cptr**

**shape** is only specified if **fptr** is an array.

### **Description**

**c_f_pointer**(3) assigns the target (the C pointer **cptr**) to the
Fortran pointer **fptr** and specifies its shape if **fptr** points to
an array.

### **Options**

- **cptr**
  : scalar of the type c_ptr. It is **intent(in)**.

- **fptr**
  : pointer interoperable with **cptr**. it is **intent(out)**.

- **shape**
  : (Optional) Rank-one array of type _integer_ with **intent(in)** .
  It shall be present if and only if **fptr** is an array. The size
  must be equal to the rank of **fptr**.

### **Examples**

Sample program:

```fortran
program demo_c_f_pointer
use iso_c_binding
implicit none
interface
   subroutine my_routine(p) bind(c,name='myC_func')
      import :: c_ptr
      type(c_ptr), intent(out) :: p
   end subroutine
end interface
type(c_ptr) :: cptr
real,pointer :: a(:)
   call my_routine(cptr)
   call c_f_pointer(cptr, a, [12])
end program demo_c_f_pointer
```

### **Standard**

Fortran 2003

### **See Also**

[**c_loc**(3)](#c_loc),
[**c_f_procpointer**(3)](#c_f_procpointer),
**iso_c_binding**(3)

_fortran-lang intrinsic descriptions_
