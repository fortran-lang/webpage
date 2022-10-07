## matmul

### **Name**

**matmul**(3) - \[TRANSFORMATIONAL\] matrix multiplication

### **Syntax**

```fortran
result = matmul(matrix_a, matrix_b)
```

### **Description**

Performs a matrix multiplication on numeric or logical arguments.

### **Arguments**

- **matrix_a**
  : An array of _integer_, _real_, _complex_, or _logical_ type, with a rank of
  one or two.

- **matrix_b**
  : An array of _integer_, _real_, or _complex_ type if **matrix_a** is of a
  numeric type; otherwise, an array of _logical_ type. The rank shall be
  one or two, and the first (or only) dimension of **matrix_b** shall be
  equal to the last (or only) dimension of **matrix_a**.

### **Returns**

The matrix product of **matrix_a** and **matrix_b**. The type and kind of the
result follow the usual type and kind promotion rules, as for the \* or
.and. operators.

### **Standard**

Fortran 95 and later

###### fortran-lang intrinsic descriptions
