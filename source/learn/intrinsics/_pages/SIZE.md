(size)=
## size

### **Name**

**size**(3) - \[ARRAY:INQUIRY\] Determine the size of an array or extent of one dimension

### **Synopsis**

```fortran
    result = size(array [,dim] [,kind])
```

```fortran
     integer(kind=KIND) function size(array,dim,kind)

      type(TYPE(kind=KIND),intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- **array** is an assumed-rank array or array of any type and associated
  kind.

  If **array** is a pointer it must be associated and allocatable arrays
  must be allocated.

- **dim** is an integer scalar
- **kind** is a scalar integer constant expression.
- the result is an integer scalar of kind **KIND**. If **KIND** is absent
  a _integer_ of default kind is returned.
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**size(3)** returns the total number of elements in an array, or
if **dim** is specified returns the number of elements along that
dimension.

**size**(3) determines the extent of **array** along a specified
dimension **dim**, or the total number of elements in **array** if
**dim** is absent.

### **Options**

- **array**
  : the array to measure the number of elements of.
  If **array\* is an assumed-size array, **dim** shall be present with a value less
  than the rank of **array\*\*.

- **dim**
  : a value shall be
  in the range from 1 to n, where n equals the rank of **array**.

  If not present the total number of elements of the entire array
  are returned.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

  If absent the kind type parameter of the returned value is that of
  default integer type.

  The **kind** must allow for the magnitude returned by **size** or
  results are undefined.

  If **kind** is absent, the return value is of default _integer_ kind.

### **Result**

If **dim** is not present **array** is assumed-rank, the result has a
value equal to **PRODUCT(SHAPE(ARRAY,KIND))**. Otherwise, the result
has a value equal to the total number of elements of **array**.

If **dim** is present the number of elements along that dimension
are returned, except that if ARRAY is assumed-rank and associated
with an assumed-size array and DIM is present with a value equal to
the rank of **array**, the value is -1.

NOTE1

If **array** is assumed-rank and has rank zero, **dim** cannot be
present since it cannot satisfy the requirement

1 <= DIM <= 0.

### **Examples**

Sample program:

```fortran
program demo_size
implicit none
integer :: arr(0:2,-5:5)
   write(*,*)'SIZE of simple two-dimensional array'
   write(*,*)'SIZE(arr)       :total count of elements:',size(arr)
   write(*,*)'SIZE(arr,DIM=1) :number of rows         :',size(arr,dim=1)
   write(*,*)'SIZE(arr,DIM=2) :number of columns      :',size(arr,dim=2)

   ! pass the same array to a procedure that passes the value two
   ! different ways
   call interfaced(arr,arr)
contains

subroutine interfaced(arr1,arr2)
! notice the difference in the array specification
! for arr1 and arr2.
integer,intent(in) :: arr1(:,:)
integer,intent(in) :: arr2(2,*)
   !
   write(*,*)'interfaced assumed-shape array'
   write(*,*)'SIZE(arr1)        :',size(arr1)
   write(*,*)'SIZE(arr1,DIM=1)  :',size(arr1,dim=1)
   write(*,*)'SIZE(arr1,DIM=2)  :',size(arr1,dim=2)

!  write(*,*)'SIZE(arr2)        :',size(arr2)
   write(*,*)'SIZE(arr2,DIM=1)  :',size(arr2,dim=1)
!
! CANNOT DETERMINE SIZE OF ASSUMED SIZE ARRAY LAST DIMENSION
!  write(*,*)'SIZE(arr2,DIM=2)  :',size(arr2,dim=2)

end subroutine interfaced

end program demo_size
```

Results:

```text
    SIZE of simple two-dimensional array
    SIZE(arr)       :total count of elements:          33
    SIZE(arr,DIM=1) :number of rows         :           3
    SIZE(arr,DIM=2) :number of columns      :          11
    interfaced assumed-shape array
    SIZE(arr1)        :          33
    SIZE(arr1,DIM=1)  :           3
    SIZE(arr1,DIM=2)  :          11
    SIZE(arr2,DIM=1)  :           2
```

### **Standard**

Fortran 95 , with **kind** argument - Fortran 2003

### **See Also**

#### Array inquiry:

- [**size**(3)](#size) - Determine the size of an array
- [**rank**(3)](#rank) - Rank of a data object
- [**shape**(3)](#shape) - Determine the shape of an array
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
