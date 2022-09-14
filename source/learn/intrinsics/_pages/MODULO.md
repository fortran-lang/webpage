## modulo

### **Name**

**modulo**(3) - \[NUMERIC\] Modulo function

### **Syntax**

```fortran
result = modulo(a, p)
```

### **Description**

**modulo(a,p)** computes the **a** modulo **p**.

### **Arguments**

- **a**
  : Shall be a scalar of type _integer_ or _real_.

- **p**
  : Shall be a scalar of the same type and kind as **a**. It shall not be
  zero.

### **Returns**

The type and kind of the result are those of the arguments.

- If **a** and **p** are of type _integer_: **modulo(a,p)** has the value of
  **a - floor (real(a) / real(p)) \* p**.

- If **a** and **p** are of type _real_: **modulo(a,p)** has the value of
  **a - floor (a / p) \* p**.

The returned value has the same sign as **p** and a magnitude less than the
magnitude of **p**.

### **Examples**

Sample program:

```fortran
program demo_modulo
implicit none
     print *, modulo(17,3)        ! yields 2
     print *, modulo(17.5,5.5)    ! yields 1.0

     print *, modulo(-17,3)       ! yields 1
     print *, modulo(-17.5,5.5)   ! yields 4.5

     print *, modulo(17,-3)       ! yields -1
     print *, modulo(17.5,-5.5)   ! yields -4.5
end program demo_modulo
```

Results:

```text
              2
      1.00000000
              1
      4.50000000
             -1
     -4.50000000
```

### **Standard**

Fortran 95 and later

### **See Also**

[**mod**(3)](MOD)

_fortran-lang intrinsic descriptions_
