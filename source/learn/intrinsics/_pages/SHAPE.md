(shape)=
## shape

### **Name**

**shape**(3) - \[ARRAY:INQUIRY\] Determine the shape of an array or scalar

### **Synopsis**

```fortran
  result = shape( source [,kind] )
```

```fortran
   integer(kind=KIND) function shape( source, KIND )

    type(TYPE(kind=**)),intent(in)       :: source(..)
    integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type

- **source** is an array or scalar of any type. If **source** is a pointer
  it must be associated and allocatable arrays must be allocated. It shall
  not be an assumed-size array.

- **KIND** is a constant _integer_ initialization expression.

- the result is an _integer_ array of rank one with size equal to the
  rank of **source** of the kind specified by **KIND** if **KIND**
  is present, otherwise it has the default integer kind.

### **Description**

**shape**(3) queries the shape of an array.

### **Options**

- **source**
  : an array or scalar of any type. If **source** is a pointer it
  must be associated and allocatable arrays must be allocated.

- **kind**
  : indicates the kind parameter of the result.

### **Result**

An _integer_ array of rank one with as many elements as **source**
has dimensions.

The elements of the resulting array correspond to the extent of
**source** along the respective dimensions.

If **source** is a scalar, the result is an empty array (a rank-one
array of size zero).

### **Examples**

Sample program:

```fortran
program demo_shape
implicit none
character(len=*),parameter :: all='(*(g0,1x))'
integer, dimension(-1:1, -1:2) :: a
   print all, 'shape of array=',shape(a)
   print all, 'shape of constant=',shape(42)
   print all, 'size of shape of constant=',size(shape(42))
   print all, 'ubound of array=',ubound(a)
   print all, 'lbound of array=',lbound(a)
end program demo_shape
```

Results:

```text
   shape of array= 3 4
   shape of constant=
   size of shape of constant= 0
   ubound of array= 1 2
   lbound of array= -1 -1
```

### **Standard**

Fortran 95 ; with KIND argument Fortran 2003

### **See Also**

#### Array inquiry:

- [**size**(3)](#size) - Determine the size of an array
- [**rank**(3)](#rank) - Rank of a data object
- [**ubound**(3)](#ubound) - Upper dimension bounds of an array
- [**lbound**(3)](#lbound) - Lower dimension bounds of an array

#### State Inquiry:

- [**allocated**(3)](#allocated) - Status of an allocatable entity
- [**is_contiguous**(3)](#is_contiguous) - Test if object is contiguous

#### Kind Inquiry:

- [**kind**(3)](#kind) - Kind of an entity

#### Bit Inquiry:

- [**storage_size**(3)](#storage_size) - Storage size in bits
- [**bit_size**(3)](#bit_size) - Bit size inquiry function
- [**btest**(3)](#btest) - Tests a bit of an _integer_ value.

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
