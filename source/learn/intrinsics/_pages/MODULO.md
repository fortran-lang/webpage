(modulo)=
## modulo

### **Name**

**modulo**(3) - \[NUMERIC\] Modulo function

### **Synopsis**

```fortran
    result = modulo(a, p)
```

```fortran
     elemental TYPE(kind=KIND) function modulo(a,p)

      TYPE(kind=KIND),intent(in) :: a
      TYPE(kind=KIND),intent(in) :: p
```

### **Characteristics**

- **a** may be any kind of _real_ or _integer_.
- **p** is the same type and kind as **a**
- The result and arguments are all of the same type and kind.

### **Description**

**modulo**(3) computes the **a** modulo **p**.

### **Options**

- **a**
  : the value to take the **modulo** of

- **p**
  : The value to reduce **a** by till the remainder is <= **p**.
  It shall not be zero.

### **Result**

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
 >            2
 >    1.000000
 >            1
 >    4.500000
 >           -1
 >   -4.500000
```

### **Standard**

Fortran 95

### **See Also**

[**mod**(3)](#mod)

_fortran-lang intrinsic descriptions_
