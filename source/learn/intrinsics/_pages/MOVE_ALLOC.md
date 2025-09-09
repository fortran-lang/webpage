(move_alloc)=
## move_alloc

### **Name**

**move_alloc**(3) - \[MEMORY\] Move allocation from one object to another

### **Synopsis**

```fortran
    call move_alloc(from, to [,stat] [,errmsg] )
```

```fortran
     subroutine move_alloc(from, to)

      type(TYPE(kind=**)),intent(inout),allocatable :: from(..)
      type(TYPE(kind=**)),intent(out),allocatable   :: to(..)
      integer(kind=**),intent(out)   :: stat
      character(len=*),intent(inout) :: errmsg
```

### **Characteristics**

- **from** may be of any type and kind.
- **to** shall be of the same type, kind and rank as **from**.

### **Description**

**move_alloc**(3) moves the allocation from **from** to
**to**. **from** will become deallocated in the process.

This is potentially more efficient than other methods of assigning
the values in **from** to **to** and explicitly deallocating **from**,
which are for more likely to require a temporary object or a copy of
the elements of the array.

### **Options**

- **from**
  : The data object to be moved to **to** and deallocated.

- **to**
  : The destination data object to move the allocated data object **from**
  to. Typically, it is a different shape than **from**.

- **stat**
  : If **stat** is present and execution is successful, it is assigned the
  value zero.
  : If an error condition occurs,

      o if **stat** is absent, error termination is initiated;
      o otherwise, if **from** is a coarray and the current team contains a
        stopped image, **stat** is assigned the value STAT\_STOPPED\_IMAGE
        from the intrinsic module ISO\_FORTRAN\_ENV;
      o otherwise, if **from** is a coarray and the current team contains
      a failed image, and no other error condition
        occurs, **stat** is assigned the value STAT\_FAILED\_IMAGE from the
        intrinsic module ISO\_FORTRAN\_ENV;
      o otherwise, **stat** is assigned a processor-dependent positive value
        that differs from that of STAT\_STOPPED\_IMAGE or STAT\_FAILED\_IMAGE.

- **errmsg**
  : If the **errmsg** argument is present and an error condition occurs,
  it is assigned an explanatory message. If no error condition occurs,
  the definition status and value of **errmsg** are unchanged.

### **Examples**

Basic sample program to allocate a bigger grid

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

Fortran 2003, STAT and ERRMSG options added 2018

### **See Also**

[**allocated**(3)](#allocated)

_fortran-lang intrinsic descriptions_

<!--
    35  2 Class. Subroutine, pure if and only if FROM is not a coarray.
    1   3 Arguments.
    2     FROM      may be of any type, rank, and corank. It shall be allocatable and shall not be a coindexed object.
    3               It is an INTENT (INOUT) argument.
    4     TO        shall be type compatible (7.3.2.3) with FROM and have the same rank and corank. It shall be
    5               allocatable and shall not be a coindexed object. It shall be polymorphic if FROM is polymorphic.
    6               It is an INTENT (OUT) argument. Each nondeferred parameter of the declared type of TO shall
    7               have the same value as the corresponding parameter of the declared type of FROM.
    8     STAT (optional) shall be a noncoindexed integer scalar with a decimal exponent range of at least four. It is an
    9               INTENT (OUT) argument.
    10    ERRMSG(optional) shall be a noncoindexed default character scalar. It is an INTENT (INOUT) argument.

    11  4 If execution of MOVE_ALLOC is successful, or if STAT_FAILED_IMAGE is assigned to STAT,
    12          On invocation of MOVE_ALLOC, if the allocation status of TO is allocated, it is deallocated. Then,
    13        if FROM has an allocation status of allocated on entry to MOVE_ALLOC, TO becomes allocated with
    14        dynamic type, type parameters, bounds, cobounds, and value identical to those that FROM had on entry
    15        to MOVE_ALLOC. Note that if FROM and TO are the same variable, it shall be unallocated when
    16        MOVE_ALLOC is invoked.
    17          If TO has the TARGET attribute, any pointer associated with FROM on entry to MOVE_ALLOC becomes
    18        correspondingly associated with TO. If TO does not have the TARGET attribute, the pointer association
    19        status of any pointer associated with FROM on entry becomes undefined.
    20          The allocation status of FROM becomes unallocated.
    21  5 When a reference to MOVE_ALLOC is executed for which the FROM argument is a coarray, there is an implicit
    22    synchronization of all active images of the current team. On those images, execution of the segment (11.6.2)
    23    following the CALL statement is delayed until all other active images of the current team have executed the same
    24    statement the same number of times. When such a reference is executed, if any image of the current team has
    25    stopped or failed, an error condition occurs.
    38  9 Example. The example below demonstrates reallocation of GRID to twice its previous size, with its previous
    39    contents evenly distributed over the new elements so that intermediate points can be inserted.
    40          REAL,ALLOCATABLE :: GRID(:),TEMPGRID(:)
    41          . . .
    42          ALLOCATE(GRID(-N:N))   ! initial allocation of GRID
    43          . . .
    44          ALLOCATE(TEMPGRID(-2*N:2*N)) ! allocate bigger grid
    45          TEMPGRID(::2)=GRID ! distribute values to new locations
    46          CALL MOVE_ALLOC(TO=GRID,FROM=TEMPGRID)
     1      The old grid is deallocated because TO is INTENT (OUT), and GRID then takes over the new grid allocation.
                NOTE1
                It is expected that the implementation of allocatable objects will typically involve descriptors to locate the
                allocated storage; MOVE_ALLOC could then be implemented by transferring the contents of the descriptor
                for FROM to the descriptor for TO and clearing the descriptor for FROM.
-->
