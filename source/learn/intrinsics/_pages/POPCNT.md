## popcnt

### **Name**

**popcnt**(3) - \[BIT:COUNT\] Number of bits set

### **Syntax**

```fortran
result = popcnt(i)
```

### **Description**

Returns the number of bits set in the binary representation of an
_integer_.

### **Arguments**

- **i**
  : Shall be of type _integer_.

### **Returns**

The return value is of type _integer_ and of the default integer kind.

### **Examples**

Sample program:

```fortran
program demo_popcnt
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
   & int8, int16, int32, int64
implicit none
     print *, popcnt(127),       poppar(127)
     print *, popcnt(huge(0)), poppar(huge(0))
     print *, popcnt(huge(0_int8)), poppar(huge(0_int8))
     print *, popcnt(huge(0_int16)), poppar(huge(0_int16))
     print *, popcnt(huge(0_int32)), poppar(huge(0_int32))
     print *, popcnt(huge(0_int64)), poppar(huge(0_int64))
end program demo_popcnt
```

Results:

```text
        7           1
       31           1
        7           1
       15           1
       31           1
       63           1
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**poppar**(3)](#poppar),
[**leadz**(3)](#leadz),
[**trailz**(3)](#trailz)

 _fortran-lang intrinsic descriptions_
