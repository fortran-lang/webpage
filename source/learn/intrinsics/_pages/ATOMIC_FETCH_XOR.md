(atomic_fetch_xor)=
## atomic_fetch_xor

### **Name**

**atomic_fetch_xor**(3) - \[ATOMIC:BIT MANIPULATION\] Atomic bitwise XOR operation with prior fetch

### **Synopsis**

```fortran
    call atomic_fetch_xor (atom, value, old [,stat] )
```

```fortran
     subroutine atomic_fetch_xor (atom, value, old, stat)
```

### **Characteristics**

### **Description**

**atomic_fetch_xor**(3) atomically stores the value of
**atom** in **old** and defines **atom** with the bitwise **xor** between the values of
**atom** and **value**. When **stat** is present and the invocation was successful,
it is assigned the value **0**. If it is present and the invocation has
failed, it is assigned a positive value; in particular, for a coindexed
**atom**, if the remote image has stopped, it is assigned the value of
iso_fortran_env's stat_stopped_image and if the remote image has
failed, the value stat_failed_image.

### **Options**

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

TS 18508

### **See Also**

[**atomic_define**(3)](#atomic_define),
[**atomic_xor**(3)](#atomic_xor),
[**iso_fortran_env**(3)](#),

[**atomic_fetch_add**(3)](#atomic_fetch_add),
[**atomic_fetch_and**(3)](#atomic_fetch_and),

[**atomic_fetch_or**(3)](#atomic_fetch_or)

_fortran-lang intrinsic descriptions_
