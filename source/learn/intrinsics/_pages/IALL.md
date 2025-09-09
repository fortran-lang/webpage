(iall)=
## iall

### **Name**

**iall**(3) - \[BIT:LOGICAL\] Bitwise and of array elements

### **Synopsis**

```fortran
    result = iall(array [,mask]) | iall(array ,dim [,mask])
```

```fortran
     integer(kind=KIND) function iall(array,dim,mask)

      integer(kind=KIND),intent(in)        :: array(*)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(*)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **array** must be an _integer_ array
- **mask** is a _logical_ array that conforms to **array** of any
  _logical_ kind.
- **dim** may be of any _integer_ kind.
- The result will by of the same type and kind as **array**.

### **Description**

**iall**(3) reduces with a bitwise _and_ the elements of **array** along
dimension **dim** if the corresponding element in **mask** is _.true._.

### **Options**

- **array**
  : Shall be an array of type _integer_

- **dim**
  : (Optional) shall be a scalar of type _integer_ with a value in the
  range from **1 to n**, where **n** equals the rank of **array**.

- **mask**
  : (Optional) shall be of type _logical_ and either be a scalar or an
  array of the same shape as **array**.

### **Result**

The result is of the same type as **array**.

If **dim** is absent, a scalar with the bitwise _all_ of all elements in
**array** is returned. Otherwise, an array of rank **n-1**, where **n**
equals the rank of **array**, and a shape similar to that of **array**
with dimension **dim** dropped is returned.

### **Examples**

Sample program:

```fortran
program demo_iall
use, intrinsic :: iso_fortran_env, only : integer_kinds, &
 & int8, int16, int32, int64
implicit none
integer(kind=int8) :: a(2)

   a(1) = int(b'00100100')
   a(2) = int(b'01101010')

   print '(b8.8)', iall(a)

end program demo_iall
```

Results:

```text
 > 00100000
```

### **Standard**

Fortran 2008

### **See Also**

[**iany**(3)](#iany),
[**iparity**(3)](#iparity),
[**iand**(3)](#iand)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
