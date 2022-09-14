## atomic_add

### **Name**

**atomic_add**(3) - \[ATOMIC\] Atomic ADD operation

### **Syntax**

```fortran
call atomic_add (atom, value, stat)
```

### **Description**

**atomic_ad(atom, value)** atomically adds the value of VAR to the
variable **atom**. When **stat** is present and the invocation was successful,
it is assigned the value 0. If it is present and the invocation has
failed, it is assigned a positive value; in particular, for a coindexed
ATOM, if the remote image has stopped, it is assigned the value of
iso_fortran_env's stat_stopped_image and if the remote image has
failed, the value stat_failed_image.

### **Arguments**

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
program demo_atomic_add
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*]
   call atomic_add (atom[1], this_image())
end program demo_atomic_add
```

### **Standard**

TS 18508 or later

### **See Also**

[**atomic_define**(3)](ATOMIC_DEFINE),
[**atomic_fetch_add**(3)](ATOMIC_FETCH),
[**atomic_and**(3)](ATOMIC_AND),
[**atomic_or**(3)](ATOMIC_OR),
[**atomic_xor**(3)](ATOMIC_XOR)
**iso_fortran_env**(3),

_fortran-lang intrinsic descriptions_
