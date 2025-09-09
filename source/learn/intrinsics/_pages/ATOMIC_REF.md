(atomic_ref)=
## atomic_ref

### **Name**

**atomic_ref**(3) - \[ATOMIC\] Obtaining the value of a variable atomically

### **Synopsis**

```fortran
    call atomic_ref(value, atom [,stat] )
```

```fortran
     subroutine atomic_ref(value,atom,stat)

      integer(atomic_int_kind),intent(in) :: value
      integer(atomic_int_kind)            :: atom[*]
      integer,intent(out),intent(out)     :: stat
```

### **Characteristics**

- **atom** is a scalar coarray or coindexed variable of either integer
  type with atomic_int_kind kind or logical type with atomic_logical_kind
  kind.

- **value** is a scalar of the same type as **atom**. If the kind is
  different, the value is converted to the kind of **atom**.

- **stat** is a Scalar default-kind integer variable.

### **Description**

**atomic_ref**(3) atomically assigns the value of the
variable **atom** to **value**. When **stat** is present and the invocation was
successful, it is assigned the value **0**. If it is present and the
invocation has failed, it is assigned a positive value; in particular,
for a coindexed **atom**, if the remote image has stopped, it is assigned
the value of iso_fortran_env's **stat_stopped_image** and if the remote
image has failed, the value **stat_failed_image**.

### **Options**

- **value**
  : Scalar of the same type as **atom**. If the kind is different, the value
  is converted to the kind of **atom**.

- **atom**
  : Scalar coarray or coindexed variable of either integer type with
  atomic_int_kind kind or logical type with atomic_logical_kind
  kind.

- **stat**
  : (optional) Scalar default-kind integer variable.

### **Examples**

Sample program:

```fortran
program demo_atomic_ref
use iso_fortran_env
implicit none
logical(atomic_logical_kind) :: atom[*]
logical :: val
   call atomic_ref( val, atom[1] )
   if (val) then
      print *, "Obtained"
   endif
end program demo_atomic_ref
```

### **Standard**

Fortran 2008 ; with STAT, TS 18508

### **See Also**

[**atomic_define**(3)](#atomic_define),
[**atomic_cas**(3)](#atomic_cas),
[**iso_fortran_env**(3)](#),

[**atomic_fetch_add**(3)](#atomic_add),
[**atomic_fetch_and**(3)](#atomic_and),

[**atomic_fetch_or**(3)](#atomic_or),
[**atomic_fetch_xor**(3)](#atomic_xor)

_fortran-lang intrinsic descriptions_
