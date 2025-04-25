(len)=
## len

### **Name**

**len**(3) - \[CHARACTER\] Length of a character entity

### **Synopsis**

```fortran
    result = len(string [,kind])
```

```fortran
     integer(kind=KIND) function len(string,KIND)

      character(len=*),intent(in) :: string(..)
      integer,optional,intent(in) :: KIND
```

### **Characteristics**

- **string** is a scalar or array _character_ variable
- **KIND** is a scalar integer constant expression.
- the returned value is the same integer kind as the **kind**
  argument, or of the default integer kind if **kind** is not specified.

### **Description**

**len**(3) returns the length of a _character_ string.

If **string** is an array, the length of a single element of **string**
is returned, as all elements of an array are the same length.

Note that **string** need not be defined when this intrinsic is invoked,
as only the length (not the content) of **string** is needed.

### **Options**

- **string**
  : A scalar or array string to return the length of.
  If it is an unallocated allocatable variable or a pointer that is
  not associated, its length type parameter shall not be deferred.

- **kind**
  : A constant indicating the _kind_ parameter of the result.

### **Result**

The result has a value equal to the number of characters in STRING
if it is scalar or in an element of STRING if it is an array.

### **Examples**

Sample program

```fortran
program demo_len
implicit none

! fixed length
character(len=40) :: string
! allocatable length
character(len=:),allocatable :: astring
character(len=:),allocatable :: many_strings(:)
integer :: ii
  ! BASIC USAGE
   ii=len(string)
   write(*,*)'length =',ii

  ! ALLOCATABLE VARIABLE LENGTH CAN CHANGE
  ! the allocatable string length will be the length of RHS expression
   astring=' How long is this allocatable string? '
   write(*,*)astring, ' LEN=', len(astring)
  ! print underline
   write(*,*) repeat('=',len(astring))
  ! assign new value to astring and length changes
   astring='New allocatable string'
   write(*,*)astring, ' LEN=', len(astring)
  ! print underline
   write(*,*) repeat('=',len(astring))

  ! THE STRING LENGTH WILL BE CONSTANT FOR A FIXED-LENGTH VARIABLE
   string=' How long is this fixed string? '
   write(*,*)string,' LEN=',len(string)
   string='New fixed string '
   write(*,*)string,' LEN=',len(string)

  ! ALL STRINGS IN AN ARRAY ARE THE SAME LENGTH
  ! a scalar is returned for an array, as all values in a Fortran
  ! character array must be of the same length.
   many_strings = [ character(len=7) :: 'Tom', 'Dick', 'Harry' ]
   write(*,*)'length of ALL elements of array=',len(many_strings)

  ! NAME%LEN IS ESSENTIALLY THE SAME AS LEN(NAME)
  ! you can also query the length (and other attributes) of a string
  ! using a "type parameter inquiry" (available since fortran 2018)
   write(*,*)'length from type parameter inquiry=',string%len
  ! %len is equivalent to a call to LEN() except the kind of the integer
  ! value returned is always of default kind.

  ! LOOK AT HOW A PASSED STRING CAN BE USED ...
   call passed(' how long? ')

contains

   subroutine passed(str)
   character(len=*),intent(in)  :: str
   ! the length of str can be used in the definitions of variables
      ! you can query the length of the passed variable
      write(*,*)'length of passed value is ', LEN(str)
   end subroutine passed

end program demo_len
```

Results:

```text
 >  length =          40
 >   How long is this allocatable string?  LEN=          38
 >  ======================================
 >  New allocatable string LEN=          22
 >  ======================
 >   How long is this fixed string?          LEN=          40
 >  New fixed string                         LEN=          40
 >  length of ALL elements of array=           7
 >  length from type parameter inquiry=          40
 >  length of passed value is           11
```

### **Standard**

FORTRAN 77 ; with **kind** argument - Fortran 2003

### **See Also**

len_trim(3), adjustr(3), trim(3), and adjustl(3) are related routines that
allow you to deal with leading and trailing blanks.

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl),
  [**adjustr**(3)](#adjustr),
  [**index**(3)](#index),
  [**scan**(3)](#scan),
  [**verify**(3)](#verify)

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat),
  [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
