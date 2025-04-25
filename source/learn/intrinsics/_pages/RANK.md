(rank)=
## rank

### **Name**

**rank**(3) - \[ARRAY:INQUIRY\] Rank of a data object

### **Synopsis**

```fortran
    result = rank(a)
```

```fortran
     integer function rank(a)

      type(TYPE(kind=**)),intent(in) :: a(..)
```

### **Characteristics**

- **a** can be of any type **TYPE** and rank.
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**rank**(3) returns the rank of a scalar or array data object.

The rank of an array is the number of dimensions it has (zero for a scalar).

### **Options**

- **a** is the data object to query the dimensionality of. The rank returned
  may be from 0 to 16.

  The argument **a** may be any data object type, including an assumed-rank
  array.

### **Result**

For arrays, their rank is returned; for scalars zero is returned.

### **Examples**

Sample program:

```fortran
program demo_rank
implicit none

! a bunch of data objects to query
integer           :: a
real, allocatable :: b(:,:)
real, pointer     :: c(:)
complex           :: d

! make up a type
type mytype
   integer :: int
   real :: float
   character :: char
end type mytype
type(mytype) :: any_thing(1,2,3,4,5)

  ! basics
   print *, 'rank of scalar a=',rank(a)
   ! you can query this array even though it is not allocated
   print *, 'rank of matrix b=',rank(b)
   print *, 'rank of vector pointer c=',rank(c)
   print *, 'rank of complex scalar d=',rank(d)

  ! you can query any type, not just intrinsics
   print *, 'rank of any arbitrary type=',rank(any_thing)

  ! an assumed-rank object may be queried
   call query_int(10)
   call query_int([20,30])
   call query_int( reshape([40,50,60,70],[2,2]) )

  ! you can even query an unlimited polymorphic entity
   call query_anything(10.0)
   call query_anything([.true.,.false.])
   call query_anything( reshape([40.0,50.0,60.0,70.0],[2,2]) )

contains

subroutine query_int(data_object)
! It is hard to do much with something dimensioned
! name(..) if not calling C except inside of a
! SELECT_RANK construct but one thing you can
! do is call the inquiry functions ...
integer,intent(in) :: data_object(..)
character(len=*),parameter :: all='(*(g0,1x))'

   if(rank(data_object).eq.0)then
      print all,&
      & 'passed a scalar to an assumed rank,  &
      & rank=',rank(data_object)
   else
      print all,&
      & 'passed an array to an assumed rank,  &
      & rank=',rank(data_object)
   endif

end subroutine query_int

subroutine query_anything(data_object)
class(*),intent(in) ::data_object(..)
character(len=*),parameter :: all='(*(g0,1x))'
  if(rank(data_object).eq.0)then
    print all,&
    &'passed a scalar to an unlimited polymorphic rank=', &
    & rank(data_object)
  else
    print all,&
    & 'passed an array to an unlimited polymorphic, rank=', &
    & rank(data_object)
  endif
end subroutine query_anything

end program demo_rank
```

Results:

```text
    rank of scalar a=           0
    rank of matrix b=           2
    rank of vector pointer c=           1
    rank of complex scalar d=           0
    rank of any arbitrary type=           5
   passed a scalar to an assumed rank,   rank= 0
   passed an array to an assumed rank,   rank= 1
   passed an array to an assumed rank,   rank= 2
   passed a scalar to an unlimited polymorphic rank= 0
   passed an array to an unlimited polymorphic, rank= 1
   passed an array to an unlimited polymorphic, rank= 2
```

### **Standard**

### **See also**

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

#
