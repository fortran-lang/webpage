(allocated)=
## allocated

### **Name**

**allocated**(3) - \[ARRAY:INQUIRY\] Allocation status of an allocatable entity

### **Synopsis**

```fortran
    result = allocated(array|scalar)
```

```fortran
     logical function allocated(array,scalar)

      type(TYPE(kind=**)),allocatable,optional :: array(..)
      type(TYPE(kind=**)),allocatable,optional :: scalar
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **array** may be any allocatable array object of any type.
- **scalar** may be any allocatable scalar of any type.
- the result is a default logical scalar

### **Description**

**allocated**(3) checks the allocation status of both arrays
and scalars.

At least one and only one of **array** or **scalar** must be specified.

### **Options**

- **entity**
  : the _allocatable_ object to test.

### **Result**

If the argument is allocated then the result is _.true._; otherwise,
it returns _.false._.

### **Examples**

Sample program:

```fortran
program demo_allocated
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp), allocatable :: x(:)
character(len=256) :: message
integer :: istat
  ! basics
   if( allocated(x)) then
       write(*,*)'do things if allocated'
   else
       write(*,*)'do things if not allocated'
   endif

   ! if already allocated, deallocate
   if ( allocated(x) ) deallocate(x,STAT=istat, ERRMSG=message )
   if(istat.ne.0)then
      write(*,*)trim(message)
      stop
   endif

   ! only if not allocated, allocate
   if ( .not. allocated(x) ) allocate(x(20))

  ! allocation and intent(out)
   call intentout(x)
   write(*,*)'note it is deallocated!',allocated(x)

   contains

   subroutine intentout(arr)
   ! note that if arr has intent(out) and is allocatable,
   ! arr is deallocated on entry
   real(kind=sp),intent(out),allocatable :: arr(:)
       write(*,*)'note it was allocated in calling program',allocated(arr)
   end subroutine intentout

end program demo_allocated
```

Results:

```text
 >  do things if not allocated
 >  note it was allocated in calling program F
 >  note it is deallocated! F
```

### **Standard**

Fortran 95. allocatable scalar entities were added in Fortran 2003.

### **See Also**

[**move_alloc**(3)](#move_alloc)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
