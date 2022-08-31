## count

### **Name**

**count**(3) - \[ARRAY REDUCTION\] Count function

### **Syntax**

```fortran
result = count(mask, dim, kind)
```

### **Description**

Counts the number of **.true.** elements in a logical **mask**, or, if the **dim**
argument is supplied, counts the number of elements along each row of
the array in the **dim** direction. If the array has zero size, or all of
the elements of **mask** are false, then the result is **0**.

### **Arguments**

- **mask**
  : The type shall be _logical_.

- **dim**
  : (Optional) The type shall be _integer_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default integer kind. If **dim** is present, the
result is an array with a rank one less than the rank of **array**, and a
size corresponding to the shape of **array** with the **dim** dimension removed.

### **Examples**

Sample program:

```fortran
program demo_count
implicit none
integer, dimension(2,3) :: a, b
logical, dimension(2,3) :: mymask
      a = reshape( [ 1, 2, 3, 4, 5, 6 ], [ 2, 3 ])
      b = reshape( [ 0, 7, 3, 4, 5, 8 ], [ 2, 3 ])
      print '(3i3)', a(1,:)
      print '(3i3)', a(2,:)
      print *
      print '(3i3)', b(1,:)
      print '(3i3)', b(2,:)
      print *
      mymask = a.ne.b
      print '(3l3)', mymask(1,:)
      print '(3l3)', mymask(2,:)
      print *
      print '(3i3)', count(mymask)
      print *
      print '(3i3)', count(mymask, 1)
      print *
      print '(3i3)', count(mymask, 2)
end program demo_count
```

Expected Results:

```text
  1  3  5
  2  4  6

  0  3  5
  7  4  8

  T  F  F
  T  F  T

  3

  2  0  1

  1  2
```

### **Standard**

Fortran 95 and later, with KIND argument - Fortran 2003
and later

###### fortran-lang intrinsic descriptions
