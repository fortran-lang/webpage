## is_iostat_eor

### **Name**

**is_iostat_eor**(3) - \[STATE\] Test for end-of-record value

### **Syntax**

```fortran
result = is_iostat_eor(i)
```

### **Description**

is_iostat_eor tests whether an variable has the value of the I/O
status "end of record". The function is equivalent to comparing the
variable with the iostat_eor parameter of the intrinsic module
**iso_fortran_env**.

### **Arguments**

- **i**
  : Shall be of the type _integer_.

### **Returns**

Returns a _logical_ of the default kind, which .true. if **i** has the value
which indicates an end of file condition for iostat= specifiers, and is
.false. otherwise.

### **Examples**

Sample program:

```fortran
program demo_is_iostat_eor
implicit none
integer :: stat, i(50)

  open(88, file='test.dat', form='unformatted')
  read(88, iostat=stat) i

  if(is_iostat_eor(stat)) stop 'end of record'

end program demo_is_iostat_eor
```

### **Standard**

Fortran 2003 and later

_fortran-lang intrinsic descriptions_
