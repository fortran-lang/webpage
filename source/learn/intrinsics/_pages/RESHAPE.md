(reshape)=
## reshape

### **Name**

**reshape**(3) - \[ARRAY:RESHAPE\] Function to reshape an array

### **Synopsis**

```fortran
    result = reshape( source, shape [,pad] [,order] )
```

```fortran
     type(TYPE(kind=KIND) function reshape

      type(TYPE(kind=KIND),intent(in)          :: source(..)
      integer(kind=**),intent(in)              :: shape(:)
      type(TYPE(kind=KIND),intent(in),optional :: pad(..)
      integer(kind=**),intent(in),optional     :: order(:)
```

### **Characteristics**

- **source** is an array of any type
- **shape** defines a Fortran shape and therefore an _integer_ vector
  (of rank one) of constant size of up to 16 non-negative values.
- **pad** is the same type as **source**
- **order** is the same shape as **shape**
- The result is an array of shape **shape** with the same type as **source**.
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**reshape** constructs an array of arbitrary shape **shape** using the elements
from **source** and possibly **pad** to fill it.

If necessary, the new array may be padded with elements from **pad**
or permuted as defined by **order**.

Among many other uses, **reshape** can be used to reorder a Fortran array
to match C array ordering before the array is passed from Fortran to a
C procedure.

### **Options**

- **source**
  : an array containing the elements to be copied to the result.
  there must be enough elements in the source to fill the new shape
  if **pad** is omitted or has size zero. Expressed in Fortran ...

```fortran
   if(.not.present(pad))then
      if(size(source) < product(shape))then
        stop 'not enough elements in the old array to fill the new one'
      endif
   endif
```

- **shape**
  : This is the shape of the new array being generated.
  Being by definition a shape; all elements are either positive integers
  or zero, the size but be 1 or greater, it may have up to 16 elements
  but must be of constant fixed size and rank one.

- **pad**
  : used to fill in extra values if the result array is larger than **source**.
  It will be used repeatedly after all the elements of **source** have been
  placed in the result until the result has all elements assigned.
  : If it is absent or is a zero-sized array, you can only make
  **source** into another array of the same size as **source** or smaller.

- **order**
  : used to insert elements in the result in an order other
  than the normal Fortran array element order, in which the first dimension
  varies fastest.
  : By definition of ranks the values have to be a permutation of the numbers
  from 1 to n, where n is the rank of **shape**.
  : the elements of **source** and pad are placed into the result in order;
  changing the left-most rank most rapidly by default. To change the order by
  which the elements are placed in the result use **order**.

### **Result**

The result is an array of shape **shape** with the same type and type
parameters as **source**. It is first filled with the values of elements
of **source**, with the remainder filled with repeated copies of **pad**
until all elements are filled. The new array may be smaller than
**source**.

### **Examples**

Sample program:

```fortran
program demo_reshape
implicit none
! notice the use of "shape(box)" on the RHS
integer :: box(3,4)=reshape([1,2,3,4,5,6,7,8,9,10,11,12],shape(box))
integer,allocatable :: v(:,:)
integer :: rc(2)
   ! basics0
    ! what is the current shape of the array?
    call printi('shape of box is ',box)
    ! change the shape
    call printi('reshaped ',reshape(box,[2,6]))
    call printi('reshaped ',reshape(box,[4,3]))

   ! fill in row column order using order
    v=reshape([1,2,3,4,10,20,30,40,100,200,300,400],[1,12])
    call printi('here is some data to shape',v)
    call printi('normally fills columns first ',reshape([v],[3,4]))
    call printi('fill rows first', reshape([v],[3,4],order=[2,1]))

    ! if we take the data and put in back in filling
    ! rows first instead of columns, and flipping the
    ! height and width of the box we not only fill in
    ! a vector using row-column order we actually
    ! transpose it.
    rc(2:1:-1)=shape(box)
    ! copy the data in changing column number fastest
    v=reshape(box,rc,order=[2,1])
    call printi('reshaped and reordered',v)
    ! of course we could have just done a transpose
    call printi('transposed',transpose(box))

   ! making the result bigger than source using pad
    v=reshape(box,rc*2,pad=[-1,-2,-3],order=[2,1])
    call printi('bigger and padded and reordered',v)
contains

subroutine printi(title,arr)
implicit none

!@(#) print small 2d integer arrays in row-column format

character(len=*),parameter :: all='(*(g0,1x))' ! a handy format
character(len=*),intent(in)  :: title
integer,intent(in)           :: arr(:,:)
integer                      :: i
character(len=:),allocatable :: biggest

   print all
   print all, trim(title),':(',shape(arr),')'  ! print title
   biggest='           '  ! make buffer to write integer into
   ! find how many characters to use for integers
   write(biggest,'(i0)')ceiling(log10(real(maxval(abs(arr)))))+2
   ! use this format to write a row
   biggest='(" > [",*(i'//trim(biggest)//':,","))'
   ! print one row of array at a time
   do i=1,size(arr,dim=1)
      write(*,fmt=biggest,advance='no')arr(i,:)
      write(*,'(" ]")')
   enddo

end subroutine printi

end program demo_reshape
```

Results:

```text
   shape of box is :( 3 4 )
    > [   1,   4,   7,  10 ]
    > [   2,   5,   8,  11 ]
    > [   3,   6,   9,  12 ]

   reshaped :( 2 6 )
    > [   1,   3,   5,   7,   9,  11 ]
    > [   2,   4,   6,   8,  10,  12 ]

   reshaped :( 4 3 )
    > [   1,   5,   9 ]
    > [   2,   6,  10 ]
    > [   3,   7,  11 ]
    > [   4,   8,  12 ]

   here is some data to shape :( 1 12 )
    > [   1,   2,   3,   4,  10,  20,  30,  40, 100, 200, 300, 400 ]

   normally fills columns first :( 3 4 )
    > [    1,    4,   30,  200 ]
    > [    2,   10,   40,  300 ]
    > [    3,   20,  100,  400 ]

   fill rows first :( 3 4 )
    > [    1,    2,    3,    4 ]
    > [   10,   20,   30,   40 ]
    > [  100,  200,  300,  400 ]

   reshaped and reordered :( 4 3 )
    > [   1,   2,   3 ]
    > [   4,   5,   6 ]
    > [   7,   8,   9 ]
    > [  10,  11,  12 ]

   transposed :( 4 3 )
    > [   1,   2,   3 ]
    > [   4,   5,   6 ]
    > [   7,   8,   9 ]
    > [  10,  11,  12 ]

   bigger and padded and reordered :( 8 6 )
    > [   1,   2,   3,   4,   5,   6 ]
    > [   7,   8,   9,  10,  11,  12 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
    > [  -1,  -2,  -3,  -1,  -2,  -3 ]
```

### **Standard**

Fortran 95

### **See Also**

[**shape**(3)](#shape),
[**pack**(3)](#pack),
[**transpose**(3)](#transpose)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
