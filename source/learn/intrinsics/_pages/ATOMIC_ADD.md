(atomic_add)=
## atomic_add

### **Name**

**atomic_add**(3) - \[ATOMIC\] Atomic ADD operation

### **Synopsis**

```fortran
    call atomic_add (atom, value [,stat] )
```

```fortran
     subroutine atomic_add(atom,value,stat)

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

**atomic_add**(3) atomically adds the value of VAR to the
variable **atom**. When **stat** is present and the invocation was successful,
it is assigned the value 0. If it is present and the invocation has
failed, it is assigned a positive value; in particular, for a coindexed
ATOM, if the remote image has stopped, it is assigned the value of
iso_fortran_env's STAT_STOPPED_IMAGE and if the remote image has
failed, the value STAT_FAILED_IMAGE.

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
program demo_atomic_add
use iso_fortran_env
implicit none
integer(atomic_int_kind) :: atom[*]
   call atomic_add (atom[1], this_image())
end program demo_atomic_add
```

### **Standard**

TS 18508

### **See Also**

[**atomic_define**(3)](#atomic_define),
[**atomic_fetch_add**(3)](#atomic_fetch),
[**atomic_and**(3)](#atomic_and),
[**atomic_or**(3)](#atomic_or),
[**atomic_xor**(3)](#atomic_xor)
**iso_fortran_env**(3),

_fortran-lang intrinsic descriptions_
