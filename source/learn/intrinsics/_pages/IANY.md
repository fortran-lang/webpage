## iany

### **Name**

**iany**(3) - \[BIT:LOGICAL\] Bitwise or of array elements

### **Syntax**

```fortran
  result = iany(array, mask)

    or

  result = iany(array, dim, mask)
```

### **Description**

Reduces with bitwise or (inclusive or) the elements of **array** along
dimension **dim** if the corresponding element in **mask** is **.true.**.

### **Arguments**

- **array**
  : Shall be an array of type _integer_

- **dim**
  : (Optional) shall be a scalar of type _integer_ with a value in the
  range from **1 to n**, where **n** equals the rank of **array**.

- **mask**
  : (Optional) shall be of type _logical_ and either be a scalar or an
  array of the same shape as **array**.

### **Returns**

The result is of the same type as **array**.

If **dim** is absent, a scalar with the bitwise _or_ of all elements in **array**
is returned. Otherwise, an array of rank **n-1**, where **n** equals the
rank of **array**, and a shape similar to that of **array** with dimension **dim**
dropped is returned.

### **Examples**

Sample program:

```fortran
program demo_iany
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
 & int8, int16, int32, int64
implicit none
integer(kind=int8) :: a(2)
     a(1) = int(b'00100100')
     a(2) = int(b'01101010')
     print '(b8.8)', iany(a)
end program demo_iany
```

Results:

```
   01101110
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**iparity**(3)](#iparity),
[**iall**(3)](#iall),
[**ior**(3)](#ior)

 _fortran-lang intrinsic descriptions_
