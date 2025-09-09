(atomic_cas)=
## atomic_cas

### **Name**

**atomic_cas**(3) - \[ATOMIC\] Atomic compare and swap

### **Synopsis**

```fortran
    call atomic_cas (atom, old, compare, new [,stat] )
```

```fortran
     subroutine atomic_cas (atom, old, compare, new, stat)
```

### **Characteristics**

### **Description**

**atomic_cas**(3) compares the variable **atom** with the value of
**compare**; if the value is the same, **atom** is set to the value of
**new**. Additionally, **old** is set to the value of **atom** that was
used for the comparison. When **stat** is present and the invocation
was successful, it is assigned the value 0. If it is present and the
invocation has failed, it is assigned a positive value; in particular,
for a coindexed **atom**, if the remote image has stopped, it is assigned
the value of iso_fortran_env's stat_stopped_image and if the remote
image has failed, the value stat_failed_image.

### **Options**

- **atom**
  : Scalar coarray or coindexed variable of either integer type with
  atomic_int_kind kind or logical type with atomic_logical_kind
  kind.

- **old**
  : Scalar of the same type and kind as **atom**.

- **compare**
  : Scalar variable of the same type and kind as **atom**.

- **new**
  : Scalar variable of the same type as **atom**. If kind is different, the
  value is converted to the kind of **atom**.

- **stat**
  : (optional) Scalar default-kind integer variable.

### **Examples**

Sample program:

```fortran
program demo_atomic_cas
use iso_fortran_env
implicit none
logical(atomic_logical_kind) :: atom[*], prev
   call atomic_cas(atom[1], prev, .false., .true.)
end program demo_atomic_cas
```

### **Standard**

TS 18508

### **See Also**

[**atomic_define**(3)](#atomic_define),
[**atomic_ref**(3)](#atomic_ref),
[**iso_fortran_env**(3)](#)

_fortran-lang intrinsic descriptions_
