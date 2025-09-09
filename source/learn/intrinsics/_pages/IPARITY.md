(iparity)=
## iparity

### **Name**

**iparity**(3) - \[BIT:LOGICAL\] Bitwise exclusive OR of array elements

### **Synopsis**

```fortran
    result = iparity( array [,mask] ) | iparity( array, dim [,mask] )
```

```fortran
     integer(kind=KIND) function iparity(array, dim, mask )

      integer(kind=KIND),intent(in) :: array(..)
      logical(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

- **array** - An _integer_ array.
- **dim** - an _integer_ scalar from 1 to the rank of **array**
- **mask** - _logical_ conformable with **array**.

### **Description**

**iparity**(3) reduces with bitwise _xor_ (exclusive _or_) the elements
of **array** along dimension **dim** if the corresponding element in
**mask** is _.true._.

### **Options**

- **array**
  : an array of _integer_ values

- **dim** a value from 1 to the rank of **array**.

- **mask**
  : a _logical_ mask either a scalar or an array of the same shape
  as **array**.

### **Result**

The result is of the same type as **array**.

If **dim** is absent, a scalar with the bitwise _xor_ of all elements in **array**
is returned. Otherwise, an array of rank **n-1**, where **n** equals the
rank of **array**, and a shape similar to that of **array** with dimension **dim**
dropped is returned.

Case (i): The result of IPARITY (ARRAY) has a value equal to the
bitwise exclusive OR of all the elements of ARRAY. If
ARRAY has size zero the result has the value zero.

Case (ii): The result of IPARITY (ARRAY, MASK=MASK) has a value
equal to that of

```fortran
               IPARITY (PACK (ARRAY, MASK)).
```

Case (iii): The result of IPARITY (ARRAY, DIM=DIM [, MASK=MASK])
has a value equal to that of IPARITY (ARRAY [, MASK=MASK])
if ARRAY has rank one.

               Otherwise, an array of values reduced along the dimension
               **dim** is returned.

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

Fortran 2008

### **See Also**

[**iany**(3)](#iany),
[**iall**(3)](#iall),
[**ieor**(3)](#ieor),
[**parity**(3)](#parity)

_fortran-lang intrinsic descriptions_
