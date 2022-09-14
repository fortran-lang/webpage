## len

### **Name**

**len**(3) - \[CHARACTER\] Length of a character entity

### **Syntax**

```fortran
   l = len(string, kind)

    integer(kind=KIND) function len(string,kind) result(value)
    character(len=*),intent(in) :: string
    integer,optional,intent(in) :: KIND
    integer(kind=KIND) :: value
```

where the returned value is the same kind as the **KIND**, or of
the default kind if **KIND** is not specified.

### **Description**

**len(3)** Returns the length of a _character_ string.

If **string** is an array, the length of an element of **string**
is returned.

Note that **string** need not be defined when this intrinsic is invoked,
as only the length (not the content) of **string** is needed.

### **Arguments**

- **string**
  : Shall be a scalar or array of type _character_.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default integer kind.

### **Standard**

FORTRAN 77 and later; with **kind** argument - Fortran 2003 and later

### **Examples**

Sample program

```fortran
program demo_len
implicit none
character(len=40) :: string
character(len=:),allocatable :: astring
character(len=:),allocatable :: many_strings(:)
integer :: ii

   ii=len(string)
  write(*,*)'length =',ii

  ! the string length will be constant for the fixed-length variable
  string=' How long is this string? '
  write(*,'(a)')' ',string,repeat('=',len(string))

  ! the allocatable string length will be the length of LHS expression
  astring=' How long is this string? '
  write(*,'(a)')' ',astring,repeat('=',len(astring))

   ! you can also query the length (and other attributes) of a string
   ! using a "type parameter inquiry:" (available since fortran 2018)
   write(*,*)'length from type parameter inquiry=',string%len

   ! a scalar is returned for an array, as all values in a Fortran
   ! character array must be of the same length:

   ! define an allocatable array with a constructor ...
     many_strings = [ character(len=7) :: 'Takata', 'Tanaka', 'Hayashi' ]
   write(*,*)
   write(*,*)'length of ALL elements of array=',len(many_strings)

   call proc_star(' how long? ')

contains

   subroutine proc_star(str)
   character(len=*),intent(in)  :: str
   character(len=:),allocatable :: str2
   ! the length of str can be used in the definitions of variables
   character(len=len(str))      :: str3

      if(allocated(str2))deallocate(str2)
      ! syntax for allocating a scalar string
      allocate(character(len=len(str)) :: str2)

      write(*,*)len(str),len(str2),len(str3)
      ! these are other allowable ways to define str2
      str2=str
      str2=repeat(' ',len(str))

   end subroutine proc_star

end program demo_len
```

Results:

```text

```

### **See Also**

len_trim(3), adjustr(3), trim(3), and adjustl(3) are related routines that
allow you to deal with leading and trailing blanks.

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](ADJUSTL),
  [**adjustr**(3)](ADJUSTR),
  [**index**(3)](INDEX),
  [**scan**(3)](SCAN),
  [**verify**(3)](VERIFY)

- **Nonelemental:**
  [**len_trim**(3)](LEN_TRIM),
  [**len**(3)](LEN),
  [**repeat**(3)](REPEAT),
  [**trim**(3)](TRIM)

_fortran-lang intrinsic descriptions (license: MIT) @urbanjost_
