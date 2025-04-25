(c_f_procpointer)=
## c_f_procpointer

### **Name**

**c_f_procpointer**(3) - \[ISO_C_BINDING\] Convert C into Fortran procedure pointer

### **Synopsis**

```fortran
    call c_f_procpointer(cptr, fptr)
```

```fortran
     subroutine c_f_procpointer(cptr, fptr )

      type(c_funptr),intent(in) :: cprt
      type(TYPE),pointer,intent(out) :: fprt
```

### **Characteristics**

### **Description**

**c_f_procpointer**(3) assigns the target of the C function
pointer **cptr** to the Fortran procedure pointer **fptr**.

### **Options**

- **cptr**
  : scalar of the type c_funptr. It is **intent(in)**.

- **fptr**
  : procedure pointer interoperable with **cptr**. It is **intent(out)**.

### **Examples**

Sample program:

```fortran
program demo_c_f_procpointer
use iso_c_binding
implicit none
abstract interface
   function func(a)
   import :: c_float
   real(c_float), intent(in) :: a
   real(c_float) :: func
   end function
end interface
interface
   function getIterFunc() bind(c,name="getIterFunc")
   import :: c_funptr
   type(c_funptr) :: getIterFunc
   end function
end interface
type(c_funptr) :: cfunptr
procedure(func), pointer :: myFunc
   cfunptr = getIterFunc()
   call c_f_procpointer(cfunptr, myFunc)
end program demo_c_f_procpointer
```

### **Standard**

Fortran 2003

### **See Also**

[**c_loc**(3)](#c_loc),
[**c_f_pointer**(3)](#c_f_pointer),
**iso_c_binding**(3)

_fortran-lang intrinsic descriptions_
