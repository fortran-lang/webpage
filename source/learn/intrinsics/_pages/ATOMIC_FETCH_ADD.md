## atomic_fetch_add

### **Name**

**atomic_fetch_add**(3) - \[ATOMIC\] Atomic ADD operation with prior fetch

### **Syntax**

```fortran
call atomic_fetch_add(atom, value, old, stat)
```

### **Description**

**atomic_fetch_add(atom, value, old)** atomically stores the value of
**atom** in **old** and adds the value of **var** to the variable **atom**. When **stat** is
present and the invocation was successful, it is assigned the value **0**.
If it is present and the invocation has failed, it is assigned a
positive value; in particular, for a coindexed **atom**, if the remote image
has stopped, it is assigned the value of iso_fortran_env's
stat_stopped_image and if the remote image has failed, the value
stat_failed_image.

### **Arguments**

- **atom**
  : Scalar coarray or coindexed variable of integer type with
  atomic_int_kind kind. atomic_logical_kind kind.

- **value**
  : Scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **old**
  : Scalar of the same type and kind as **atom**.

- **stat**
  : (optional) Scalar default-kind integer variable.

### **Examples**

Sample program:

```fortran
program demo_atomic_fetch_add
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*], old
   call atomic_add(atom[1], this_image(), old)
end program demo_atomic_fetch_add
```

### **Standard**

TS 18508 or later

### **See Also**

[**atomic_define**(3)](ATOMIC_DEFINE),
[**atomic_add**(3)](ATOMIC_ADD),
**iso_fortran_env**(3),

[**atomic_fetch_and**(3)](ATOMIC_FETCH_AND),
[**atomic_fetch_or**(3)](ATOMIC_FETCH_OR),

[**atomic_fetch_xor**(3)](ATOMIC_FETCH_XOR)

_fortran-lang intrinsic descriptions_
