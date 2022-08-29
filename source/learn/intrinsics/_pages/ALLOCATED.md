## allocated

### **Name**

**allocated**(3) - \[ARRAY INQUIRY\] Status of an allocatable entity

### **Syntax**

```fortran
  result = allocated(array)
```

or

```fortran
  result = allocated(scalar)
```

### **Description**

**allocated(array)** and **allocated(scalar)** check the allocation
status of **array** and **scalar**, respectively.

### **Arguments**

- **array**
  : the argument shall be an _allocatable_ array.

- **scalar**
  : the argument shall be an _allocatable_ scalar.

### **Returns**

The return value is a scalar _logical_ with the default logical kind type
parameter. If the argument is allocated then the result is .true.;
otherwise, it returns .false..

### **Examples**

Sample program:

```fortran
program demo_allocated
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
integer :: i = 4
real(kind=sp), allocatable :: x(:)

   ! if already allocated, deallocate
   if ( allocated(x) ) deallocate(x)

   ! only if not allocated, allocate
   if ( .not. allocated(x) ) allocate(x(i))

   write(*,*)allocated(x), size(x)
   if( allocated(x)) then
       write(*,*)'do things if allocated'
   else
       write(*,*)'do things if not allocated'
   endif
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
    T           4
    do things if allocated
    note it was allocated in calling program F
    note it is deallocated! F
```

### **Standard**

Fortran 95 and later. Note, the scalar= keyword and allocatable
scalar entities are available in Fortran 2003 and later.

### **See Also**

[**move_alloc**(3)](MOVE_ALLOC)

###### fortran-lang intrinsic descriptions
