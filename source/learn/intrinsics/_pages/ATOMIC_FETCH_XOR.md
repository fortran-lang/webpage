## atomic_fetch_xor

### **Name**

**atomic_fetch_xor**(3) - \[ATOMIC:BIT MANIPULATION\] Atomic bitwise XOR operation with prior fetch

### **Syntax**

```fortran
call atomic_fetch_xor (atom, value, old, stat)
```

### **Description**

**atomic_fetch_xor(atom, value, old)** atomically stores the value of
**atom** in **old** and defines **atom** with the bitwise **xor** between the values of
**atom** and **value**. When **stat** is present and the invocation was successful,
it is assigned the value **0**. If it is present and the invocation has
failed, it is assigned a positive value; in particular, for a coindexed
**atom**, if the remote image has stopped, it is assigned the value of
iso_fortran_env's stat_stopped_image and if the remote image has
failed, the value stat_failed_image.

### **Arguments**

- **atom**
  : Scalar coarray or coindexed variable of integer type with
  atomic_int_kind kind.

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
program demo_atomic_fetch_xor
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*], old
   call atomic_fetch_xor (atom[1], int(b'10100011101'), old)
end program demo_atomic_fetch_xor
```

### **Standard**

TS 18508 or later

### **See Also**

[**atomic_define**(3)](ATOMIC_DEFINE),
[**atomic_xor**(3)](ATOMIC_XOR),
[**iso_fortran_env**(3)](),

[**atomic_fetch_add**(3)](ATOMIC_FETCH_ADD),
[**atomic_fetch_and**(3)](ATOMIC_FETCH_AND),

[**atomic_fetch_or**(3)](ATOMIC_FETCH_OR)

_fortran-lang intrinsic descriptions_
