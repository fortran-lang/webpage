## ceiling

### **Name**

**ceiling**(3) - \[NUMERIC\] Integer ceiling function

### **Syntax**

```fortran
result = ceiling(a, kind)

   integer(kind=KIND) elemental function ceiling(a,kind)
   real(kind=ANY),intent(in)   :: a
   integer,intent(in),optional :: kind
```

### **Description**

**ceiling(a)** returns the least integer greater than or equal to **a**.

### **Arguments**

- **a**
  : The type shall be _real_.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type **integer**(kind) if **kind** is present and a
default-kind _integer_ otherwise.

The result is undefined if it cannot be represented in the specified
integer type.

### **Examples**

Sample program:

```fortran
program demo_ceiling
implicit none
real :: x = 63.29
real :: y = -63.59
   print *, ceiling(x)
   print *, ceiling(y)
   ! elemental
   print *,ceiling([ &
   &  -2.7,  -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, &
   &  0.0,   &
   &  +0.5,  +1.0, +1.5, +2.0, +2.2, +2.5, +2.7  ])
end program demo_ceiling
```

Results:

```text
   64
  -63
   -2      -2      -2      -2      -1      -1
    0       0       1       1       2       2
    3       3       3
```

### **Standard**

Fortran 95 and later

### **See Also**

[**floor**(3)](FLOOR),
[**nint**(3)](NINT)

[**aint**(3)](AINT),
[**anint**(3)](ANINT),
[**int**(3)](INT),
[**selected_int_kind**(3)](SELECTED_INT_KIND)

###### fortran-lang intrinsic descriptions
