## cshift

### **Name**

**cshift**(3) - \[TRANSFORMATIONAL\] Circular shift elements of an array

### **Syntax**

```fortran
result = cshift(array, shift, dim)
```

### **Description**

**cshift(array, shift \[, dim\])** performs a circular shift on elements
of **array** along the dimension of **dim**. If **dim** is omitted it is taken to be
**1**. **dim** is a scalar of type _integer_ in the range of **1 \<= dim \<= n**,
where "n" is the rank of **array**. If the rank of **array** is one, then all
elements of **array** are shifted by **shift** places. If rank is greater than
one, then all complete rank one sections of **array** along the given
dimension are shifted. Elements shifted out one end of each rank one
section are shifted back in the other end.

### **Arguments**

- **array**
  : Shall be an array of any type.

- **shift**
  : The type shall be _integer_.

- **dim**
  : The type shall be _integer_.

### **Returns**

Returns an array of same type and rank as the **array** argument.

### **Examples**

Sample program:

```fortran
program demo_cshift
implicit none
integer, dimension(3,3) :: a
    a = reshape( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [ 3, 3 ])
    print '(3i3)', a(1,:)
    print '(3i3)', a(2,:)
    print '(3i3)', a(3,:)
    a = cshift(a, SHIFT=[1, 2, -1], DIM=2)
    print *
    print '(3i3)', a(1,:)
    print '(3i3)', a(2,:)
    print '(3i3)', a(3,:)
end program demo_cshift
```

Results:

```text
     1  4  7
     2  5  8
     3  6  9

     4  7  1
     8  2  5
     9  3  6
```

### **Standard**

Fortran 95 and later

_fortran-lang intrinsic descriptions_
