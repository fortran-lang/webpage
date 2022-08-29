## iparity

### **Name**

**iparity**(3) - \[BIT:LOGICAL\] Bitwise exclusive or of array elements

### **Syntax**

```fortran
  result = iparity(array, mask)

   or

  result = iparity(array, dim, mask)
```

### **Description**

Reduces with bitwise _xor_ (exclusive _or_) the elements of **array** along
dimension **dim** if the corresponding element in **mask** is **.true.**.

### **Arguments**

- **array**
  : Shall be an array of type _integer_

- **dim**
  : (Optional) shall be a scalar of type _integer_ with a value in the
  range from **"1" to "n"**, where **"n"** equals the rank of **array**.

- **mask**
  : (Optional) shall be of type _logical_ and either be a scalar or an
  array of the same shape as **array**.

### **Returns**

The result is of the same type as **array**.

If **dim** is absent, a scalar with the bitwise _xor_ of all elements in **array**
is returned. Otherwise, an array of rank **n-1**, where **n** equals the
rank of **array**, and a shape similar to that of **array** with dimension **dim**
dropped is returned.

### **Examples**

Sample program:

```fortran
program demo_iparity
implicit none
integer, dimension(2) :: a
  a(1) = int(b'00100100')
  a(2) = int(b'01101010')
  print '(b8.8)', iparity(a)
end program demo_iparity
```

Results:

```
   01001110
```

### **Standard**

Fortran 2008 and later

### **See Also**

[**iany**(3)](IANY),
[**iall**(3)](IALL),
[**ieor**(3)](IEOR),
[**parity**(3)](PARITY)

###### fortran-lang intrinsic descriptions
