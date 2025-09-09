(atomic_and)=
## atomic_and

### **Name**

**atomic_and**(3) - \[ATOMIC:BIT MANIPULATION\] Atomic bitwise AND operation

### **Synopsis**

```fortran
    call atomic_and(atom, value [,stat])
```

```fortran
     subroutine atomic_and(atom,value,stat)

      integer(atomic_int_kind)            :: atom[*]
      integer(atomic_int_kind),intent(in) :: value
      integer,intent(out),intent(out)     :: stat
```

### **Characteristics**

- **atom** is a scalar coarray or coindexed variable of integer type with
  atomic_int_kind kind.

- **value** is a scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **stat** is a Scalar default-kind integer variable.

### **Description**

**atomic_and**(3) atomically defines **atom** with the bitwise
**and** between the values of **atom** and **value**. When **stat** is present and the
invocation was successful, it is assigned the value 0. If it is present
and the invocation has failed, it is assigned a positive value; in
particular, for a coindexed **atom**, if the remote image has stopped, it is
assigned the value of iso_fortran_env's stat_stopped_image and if
the remote image has failed, the value stat_failed_image.

### **Options**

- **atom**
  : Scalar coarray or coindexed variable of integer type with
  atomic_int_kind kind.

- **value**
  : Scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **stat**
  : (optional) Scalar default-kind integer variable.

### **Examples**

Sample program:

```fortran
program demo_atomic_and
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*]
   call atomic_and(atom[1], int(b'10100011101'))
end program demo_atomic_and
```

### **Standard**

TS 18508

### **See Also**

[**atomic_fetch_and**(3)](#atomic_fetch_and),
[**atomic_define**(3)](#atomic_define),
[**atomic_ref**(3)](#atomic_ref),
[**atomic_cas**(3)](#atomic_cas),
**iso_fortran_env**(3),
[**atomic_add**(3)](#atomic_add),
[**atomic_or**(3)](#atomic_or),
[**atomic_xor**(3)](#atomic_xor)

_fortran-lang intrinsic descriptions_
