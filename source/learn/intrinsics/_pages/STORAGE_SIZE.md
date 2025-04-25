(storage_size)=
## storage_size

### **Name**

**storage_size**(3) - \[BIT:INQUIRY\] Storage size in bits

### **Synopsis**

```fortran
    result = storage_size(a [,KIND] )
```

```fortran
     integer(kind=KIND) storage_size(a,KIND)

      type(TYPE(kind=**)) :: a
      integer,intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type

- **a** may be of any type and kind. If it is polymorphic it shall not
  be an undefined pointer. If it is unlimited polymorphic or has any
  deferred type parameters, it shall not be an unallocated allocatable
  variable or a disassociated or undefined pointer.

- The kind type parameter of the returned value is that specified by
  the value of **kind**; otherwise, the kind type parameter is that of
  default integer type.

- The result is an _integer_ scalar of default kind unless **kind** is
  specified, in which case it has the kind specified by **kind**.

### **Description**

**storage_size**(3) returns the storage size of argument **a** in bits.

### **Options**

- **a**
  : The entity to determine the storage size of

- **kind**
  : a scalar integer constant expression that defines the kind of the
  output value.

### **Result**

The result value is the size expressed in bits for an element of an
array that has the dynamic type and type parameters of **a**.

If the type and type parameters are such that storage association
applies, the result is consistent with the named constants
defined in the intrinsic module ISO_FORTRAN_ENV.

NOTE1

An array element might take "type" more bits to store than an isolated
scalar, since any hardware-imposed alignment requirements for array
elements might not apply to a simple scalar variable.

NOTE2

This is intended to be the size in memory that an object takes when it
is stored; this might differ from the size it takes during expression
handling (which might be the native register size) or when stored in a
file. If an object is never stored in memory but only in a register,
this function nonetheless returns the size it would take if it were
stored in memory.

### **Examples**

Sample program

```fortran
program demo_storage_size
implicit none

   ! a default real, integer, and logical are the same storage size
   write(*,*)'size of integer       ',storage_size(0)
   write(*,*)'size of real          ',storage_size(0.0)
   write(*,*)'size of logical       ',storage_size(.true.)
   write(*,*)'size of complex       ',storage_size((0.0,0.0))

   ! note the size of an element of the array, not the storage size of
   ! the entire array is returned for array arguments
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

Fortran 2008

### **See Also**

[**c_sizeof**(3)](#c_sizeof)

_fortran-lang intrinsic descriptions_
