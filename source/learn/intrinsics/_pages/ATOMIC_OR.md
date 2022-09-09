## atomic_or

### **Name**

**atomic_or**(3) - \[ATOMIC:BIT MANIPULATION\] Atomic bitwise OR operation

### **Syntax**

```fortran
call atomic_or(atom, value, stat)
```

### **Description**

**atomic_or(atom, value)** atomically defines **atom** with the bitwise **or**
between the values of **atom** and **value**. When **stat** is present and the
invocation was successful, it is assigned the value **0**. If it is present
and the invocation has failed, it is assigned a positive value; in
particular, for a coindexed **atom**, if the remote image has stopped, it is
assigned the value of iso_fortran_env's stat_stopped_image and if
the remote image has failed, the value stat_failed_image.

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
program demo_atomic_or
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*]
   call atomic_or(atom[1], int(b'10100011101'))
end program demo_atomic_or
```

### **Standard**

TS 18508 or later

### **See Also**

[**atomic_define**(3)](ATOMIC_DEFINE),
[**atomic_fetch_or**(3)](ATOMIC_FETCH),

[**iso_fortran_env**(3)](),
[**atomic_add**(3)](ATOMIC_ADD),
[**atomic_or**(3)](ATOMIC_OR),

[**atomic_xor**(3)](ATOMIC_XOR)

###### fortran-lang intrinsic descriptions
