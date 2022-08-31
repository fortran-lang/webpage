## any

### **Name**

**any**(3) - \[ARRAY REDUCTION\] determines if any of the values in the logical array are true.

### **Syntax**

```fortran
result = any(mask, dim)
```

### **Description**

**any(mask, dim)** determines if any of the values in the logical
array **mask** along dimension **dim** are **.true.**.

### **Arguments**

- **mask**
  : the type of the argument shall be _logical_ and it shall not be
  scalar.

- **dim**
  : (optional) dim shall be a scalar integer with a value that lies
  between one and the rank of mask.

### **Returns**

**any(mask)** returns a scalar value of type _logical_ where the kind type
parameter is the same as the kind type parameter of **mask**. If **dim** is
present, then **any(mask, dim)** returns an array with the rank of **mask**
minus 1. The shape is determined from the shape of **mask** where the **dim**
dimension is elided.

1.  **any(mask)** is true if any element of **mask** is true; otherwise, it
    is **.false.**. It also is false if **mask** has zero size.

2.  If the rank of **mask** is one, then **any(mask, dim)** is equivalent to
    **any(mask)**. If the rank is greater than one, then **any(mask,
    dim)** is determined by applying **any()** to the array sections.

### **Examples**

Sample program:

```fortran
program demo_any
implicit none
logical l
   l = any([.true., .true., .true.])
   print *, l
   call section
   contains
     subroutine section
     integer a(2,3), b(2,3)
       a = 1
       b = 1
       b(2,2) = 2
       print *, any(a .eq. b, 1)
       print *, any(a .eq. b, 2)
     end subroutine section
end program demo_any
```

Results:

```text
    T
    T T T
    T T
```

### **Standard**

Fortran 95 and later

###### fortran-lang intrinsic descriptions
