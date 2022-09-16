## mod

### **Name**

**mod**(3) - \[NUMERIC\] Remainder function

### **Syntax**

```fortran
result = mod(a, p)
```

### **Description**

**mod**(a,p) computes the remainder of the division of **a** by **p**.

### **Arguments**

- **a**
  : Shall be a scalar of type _integer_ or _real_.

- **p**
  : Shall be a scalar of the same type and kind as **a** and not equal to
  zero.

### **Returns**

The return value is the result of **a - (int(a/p) \* p)**. The type and kind
of the return value is the same as that of the arguments. The returned
value has the same sign as **a** and a magnitude less than the magnitude of
**p**.

### **Examples**

Sample program:

```fortran
program demo_mod
implicit none
     print *, mod(17,3)           ! yields 2
     print *, mod(17.5,5.5)       ! yields 1.0
     print *, mod(17.5d0,5.5d0)   ! yields 1.0d0
     print *, mod(17.5d0,5.5d0)   ! yields 1.0d0

     print *, mod(-17,3)          ! yields -2
     print *, mod(-17.5,5.5)      ! yields -1.0
     print *, mod(-17.5d0,5.5d0)  ! yields -1.0d0
     print *, mod(-17.5d0,5.5d0)  ! yields -1.0d0

     print *, mod(17,-3)          ! yields 2
     print *, mod(17.5,-5.5)      ! yields 1.0
     print *, mod(17.5d0,-5.5d0)  ! yields 1.0d0
     print *, mod(17.5d0,-5.5d0)  ! yields 1.0d0
end program demo_mod
```

Results:

```text
              2
      1.00000000
      1.0000000000000000
      1.0000000000000000
             -2
     -1.00000000
     -1.0000000000000000
     -1.0000000000000000
              2
      1.00000000
      1.0000000000000000
      1.0000000000000000
```

### **Standard**

FORTRAN 77 and later

### **See Also**

[**modulo**(3)](#modulo)

 _fortran-lang intrinsic descriptions_
