(atomic_define)=
## atomic_define

### **Name**

**atomic_define**(3) - \[ATOMIC\] Setting a variable atomically

### **Synopsis**

```fortran
    call atomic_define (atom, value [,stat] )
```

```fortran
     subroutine atomic_define(atom, value, stat)

      TYPE(kind=atomic_KIND_kind) :: atom[*]
      TYPE(kind=KIND) :: value
      integer,intent(out),optional :: stat
```

### **Characteristics**

- **atom**
  : Scalar coarray or coindexed variable of either integer type with
  atomic_int_kind kind or logical type with atomic_logical_kind
  kind.

- **value**
  : Scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **stat**
  : (optional) Scalar default-kind integer variable.

### **Description**

**atomic_define**(3) defines the variable **atom** with the value
**value** atomically.

### **Options**

- **atom**
  : Scalar coarray or coindexed variable to atomically assign the
  value **value** to.
  kind.

- **value**
  : value to assign to **atom**

- **stat**
  : When **stat** is present and the invocation was
  successful, it is assigned the value **0**. If it is present and the
  invocation has failed, it is assigned a positive value; in particular,
  for a coindexed **atom**, if the remote image has stopped, it is assigned
  the value of iso_fortran_env's stat_stopped_image and if the remote
  image has failed, the value stat_failed_image.

### **Examples**

Sample program:

```fortran
program demo_atomic_define
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*]
    call atomic_define(atom[1], this_image())
end program demo_atomic_define
```

### **Standard**

Fortran 2008 ; with **stat**, TS 18508

### **See Also**

[**atomic_ref**(3)](#atomic_ref),
[**atomic_cas**(3)](#atomic_cas),
**iso_fortran_env**(3),
[**atomic_add**(3)](#atomic_add),
[**atomic_and**(3)](#atomic_and),
[**atomic_or**(3)](#atomic_or),
[**atomic_xor**(3)](#atomic_xor)

_fortran-lang intrinsic descriptions_
