## rank

### **Name**

**rank**(3) - \[ARRAY INQUIRY\] Rank of a data object

### **Syntax**

```fortran
result = rank(a)
```

### **Description**

**rank(a)** returns the rank of a scalar or array data object.

### **Arguments**

- **a**
  : can be of any type

### **Returns**

The return value is of type _integer_ and of the default integer kind. For
arrays, their rank is returned; for scalars zero is returned.

### **Examples**

Sample program:

```fortran
program demo_rank
implicit none
integer :: a
real, allocatable :: b(:,:)
real  :: c(10,20,30)
   print *, rank(a), rank(b), rank(c)
end program demo_rank
```

Results:

```text
   0           2           3
```

### **Standard**

TS 29113

###### fortran-lang intrinsic descriptions
