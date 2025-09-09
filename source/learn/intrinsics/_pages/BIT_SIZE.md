(bit_size)=
## bit_size

### **Name**

**bit_size**(3) - \[BIT:INQUIRY\] Bit size inquiry function

### **Synopsis**

```fortran
    result = bit_size(i)
```

```fortran
     integer(kind=KIND) function bit_size(i)

      integer(kind=KIND),intent(in) :: i(..)
```

### **Characteristics**

- **i** shall be of type integer. It may be a scalar or an array.
- the value of **KIND** is any valid value for an _integer_ kind
  parameter on the processor.
- the return value is a scalar of the same kind as the input value.

### **Description**

**bit_size**(3) returns the number of bits (integer precision plus
sign bit) represented by the type of the _integer_ **i**.

### **Options**

- **i**
  : An _integer_ value of any kind whose size in bits is to be determined.
  Because only the type of the argument is examined, the argument need not
  be defined; **i** can be a scalar or an array, but a scalar representing
  just a single element is always returned.

### **Result**

The number of bits used to represent a value of the type and kind
of _i_. The result is a _integer_ scalar of the same kind as _i_.

### **Examples**

Sample program:

```fortran
program demo_bit_size
use,intrinsic :: iso_fortran_env, only : int8, int16, int32, int64
use,intrinsic :: iso_fortran_env, only : integer_kinds
implicit none
character(len=*),parameter   :: fmt=&
& '(a,": bit size is ",i3," which is kind=",i3," on this platform")'

    ! default integer bit size on this platform
    write(*,fmt) "default", bit_size(0), kind(0)

    write(*,fmt) "int8   ", bit_size(0_int8),   kind(0_int8)
    write(*,fmt) "int16  ", bit_size(0_int16),  kind(0_int16)
    write(*,fmt) "int32  ", bit_size(0_int32),  kind(0_int32)
    write(*,fmt) "int64  ", bit_size(0_int64),  kind(0_int64)

    write(*,'(a,*(i0:,", "))') "The available kinds are ",integer_kinds

end program demo_bit_size
```

Typical Results:

```text
    default: bit size is  32 which is kind=  4 on this platform
    int8   : bit size is   8 which is kind=  1 on this platform
    int16  : bit size is  16 which is kind=  2 on this platform
    int32  : bit size is  32 which is kind=  4 on this platform
    int64  : bit size is  64 which is kind=  8 on this platform
    The available kinds are 1, 2, 4, 8, 16
```

### **Standard**

Fortran 95

### **See Also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
