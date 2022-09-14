## atomic_define

### **Name**

**atomic_define**(3) - \[ATOMIC\] Setting a variable atomically

### **Syntax**

```fortran
call atomic_define (atom, value, stat)

   subroutine atomic_define(atom, value, stat)
   TYPE(kind=KIND) :: atom
   TYPE(kind=KIND) :: value
   integer,intent(out),optional :: stat
```

### **Description**

**atomic_define(atom, value)** defines the variable **atom** with the value
**value** atomically. When **stat** is present and the invocation was
successful, it is assigned the value **0**. If it is present and the
invocation has failed, it is assigned a positive value; in particular,
for a coindexed **atom**, if the remote image has stopped, it is assigned
the value of iso_fortran_env's stat_stopped_image and if the remote
image has failed, the value stat_failed_image.

### **Arguments**

- **atom**
  : Scalar coarray or coindexed variable of either integer type with
  atomic_int_kind kind or logical type with atomic_logical_kind
  kind.

- **value**
  : Scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **stat**
  : (optional) Scalar default-kind integer variable.

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

Fortran 2008 and later; with **stat**, TS 18508 or later

### **See Also**

[**atomic_ref**(3)](ATOMIC_REF),
[**atomic_cas**(3)](ATOMIC_CAS),
**iso_fortran_env**(3),
[**atomic_add**(3)](ATOMIC_ADD),
[**atomic_and**(3)](ATOMIC_AND),
[**atomic_or**(3)](ATOMIC_OR),
[**atomic_xor**(3)](ATOMIC_XOR)

_fortran-lang intrinsic descriptions_
