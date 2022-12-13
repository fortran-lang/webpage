## move_alloc

### **Name**

**move_alloc**(3) - \[\] Move allocation from one object to another

### **Syntax**

```fortran
call move_alloc(src, dest)
```

### **Description**

**move_alloc(src, dest)** moves the allocation from **src*( to
**dest*. **src** will become deallocated in the process.

### **Arguments**

- **src**
  : allocatable, **intent(inout)**, may be of any type and kind.

- **dest**
  : allocatable, **intent(out)**, shall be of the same type, kind and
  rank as **src*.

### **Examples**

Basic Sample program to allocate a bigger grid

```fortran
program demo_move_alloc
implicit none
! Example to allocate a bigger GRID
real, allocatable :: grid(:), tempgrid(:)
integer :: n, i

   ! initialize small GRID
   n = 3
   allocate (grid(1:n))
   grid = [ (real (i), i=1,n) ]

   ! initialize TEMPGRID which will be used to replace GRID
   allocate (tempgrid(1:2*n))    ! Allocate bigger grid
   tempgrid(::2)  = grid         ! Distribute values to new locations
   tempgrid(2::2) = grid + 0.5   ! initialize other values

   ! move TEMPGRID to GRID
   call MOVE_ALLOC (from=tempgrid, to=grid)

   ! TEMPGRID should no longer be allocated
   ! and GRID should be the size TEMPGRID was
   if (size (grid) /= 2*n .or. allocated (tempgrid)) then
      print *, "Failure in move_alloc!"
   endif
   print *, allocated(grid), allocated(tempgrid)
   print '(99f8.3)', grid
end program demo_move_alloc
```

Results:

```text
    T F
      1.000   1.500   2.000   2.500   3.000   3.500
```

### **Standard**

Fortran 2003 and later

### **See Also**

[**allocated**(3)](#allocated)

 _fortran-lang intrinsic descriptions_
