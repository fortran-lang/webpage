## poppar

### **Name**

**poppar**(3) - \[BIT:COUNT\] Parity of the number of bits set

### **Syntax**

```fortran
result = poppar(i)
```

### **Description**

Returns the parity of an integer's binary representation (i.e., the
parity of the number of bits set).

### **Arguments**

- **i**
  : Shall be of type _integer_.

### **Returns**

The return value is equal to **0** if **i** has an even number of bits set and 1 if an odd
number of bits are set.

It is of type _integer_ and of the default _integer_ kind.

### **Examples**

Sample program:

```fortran
program demo_popcnt
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
   & int8, int16, int32, int64
implicit none
   print  *,  popcnt(127),            poppar(127)
   print  *,  popcnt(huge(0_int8)),   poppar(huge(0_int8))
   print  *,  popcnt(huge(0_int16)),  poppar(huge(0_int16))
   print  *,  popcnt(huge(0_int32)),  poppar(huge(0_int32))
   print  *,  popcnt(huge(0_int64)),  poppar(huge(0_int64))
end program demo_popcnt
```

Results:

```text
              7           1
              7           1
             15           1
             31           1
             63           1
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**popcnt**(3)](POPCNT),
[**leadz**(3)](LEADZ),
[**trailz**(3)](TRAILZ)

_fortran-lang intrinsic descriptions_
