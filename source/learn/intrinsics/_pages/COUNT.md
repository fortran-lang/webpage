(count)=
## count

### **Name**

**count**(3) - \[ARRAY:REDUCTION\] Count true values in an array

### **Synopsis**

```fortran
    result = count(mask [,dim] [,kind] )
```

```fortran
     integer(kind=KIND) function count(mask, dim, KIND )

      logical(kind=**),intent(in) :: mask(..)
      integer(kind=**),intent(in),optional :: dim
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **mask** is a _logical_ array of any shape and kind.
- If **dim** is present, the result is an array with the specified rank
  removed.
- **KIND** is a scalar integer constant expression valid as an _integer_ kind
- The return value is of default _integer_ type unless **kind** is specified
  to declare the kind of the result.

### **Description**

**count**(3) counts the number of _.true._ elements in a logical
**mask**, or, if the **dim** argument is supplied, counts the number
of elements along each row of the array in the **dim** direction. If
the array has zero size or all of the elements of **mask** are false,
then the result is **0**.

### **Options**

- **mask**
  : an array to count the number of _.true._ values in

- **dim**
  : specifies to remove this dimension from the result and produce an
  array of counts of _.true._ values along the removed dimension.
  If not present, the result is a scalar count of the true elements in **mask**
  the value must be in the range 1 <= dim <= n, where n is the
  rank(number of dimensions) of **mask**.

  The corresponding actual argument shall not be an optional dummy
  argument, a disassociated pointer, or an unallocated allocatable.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Result**

The return value is the number of _.true_. values in **mask** if **dim**
is not present.

If **dim** is present, the result is an array with a rank one less
than the rank of the input array **mask**, and a size corresponding
to the shape of **array** with the **dim** dimension removed, with the
remaining elements containing the number of _.true._ elements along the
removed dimension.

### **Examples**

Sample program:

```fortran
   program demo_count
   implicit none
   character(len=*),parameter :: ints='(*(i2,1x))'
   ! two arrays and a mask all with the same shape
   integer, dimension(2,3) :: a, b
   logical, dimension(2,3) :: mymask
   integer :: i
   integer :: c(2,3,4)

   print *,'the numeric arrays we will compare'
   a = reshape( [ 1, 2, 3, 4, 5, 6 ], [ 2, 3 ])
   b = reshape( [ 0, 7, 3, 4, 5, 8 ], [ 2, 3 ])
   c = reshape( [( i,i=1,24)], [ 2, 3 ,4])
   print '(3i3)', a(1,:)
   print '(3i3)', a(2,:)
   print *
   print '(3i3)', b(1,:)
   print '(3i3)', b(2,:)
   !
   ! basic calls
   print *, 'count a few basic things creating a mask from an expression'
   print *, 'count a>b',count(a>b)
   print *, 'count b<a',count(a<b)
   print *, 'count b==a',count(a==b)
   print *, 'check sum = ',count(a>b) + &
                         & count(a<b) + &
                         & count(a==b).eq.size(a)
   !
   ! The common usage is just getting a count, but if you want
   ! to specify the DIM argument and get back reduced arrays
   ! of counts this is easier to visualize if we look at a mask.
   print *, 'make a mask identifying unequal elements ...'
   mymask = a.ne.b
   print *, 'the mask generated from a.ne.b'
   print '(3l3)', mymask(1,:)
   print '(3l3)', mymask(2,:)
   !
   print *,'count total and along rows and columns ...'
   !
   print '(a)', 'number of elements not equal'
   print '(a)', '(ie. total true elements in the mask)'
   print '(3i3)', count(mymask)
   !
   print '(a)', 'count of elements not equal in each column'
   print '(a)', '(ie. total true elements in each column)'
   print '(3i3)', count(mymask, dim=1)
   !
   print '(a)', 'count of elements not equal in each row'
   print '(a)', '(ie. total true elements in each row)'
   print '(3i3)', count(mymask, dim=2)
   !
   ! working with rank=3 ...
   print *, 'lets try this with c(2,3,4)'
   print *,'  taking the result of the modulo   '
   print *,'   z=1      z=2      z=3      z=4   '
   print *,'  1 3 0 || 2 4 1 || 3 0 2 || 4 1 3 |'
   print *,'  2 4 1 || 3 0 2 || 4 1 3 || 0 2 4 |'
   print *,'                                    '
   print *,'  would result in the mask ..       '
   print *,'  F F T || F F F || F T F || F F F |'
   print *,'  F F F || F T F || F F F || T F F |'
   print *,'                                    '
   print *,' the total number of .true.values is'
   print ints, count(modulo(c,5).eq.0)
   call printi('counting up along a row and removing rows',&
   count(modulo(c,5).eq.0,dim=1))
   call printi('counting up along a column and removing columns',&
   count(modulo(c,5).eq.0,dim=2))
   call printi('counting up along a depth and removing depths',&
   count(modulo(c,5).eq.0,dim=3))
   !
   contains
   !
   ! CONVENIENCE ROUTINE FOR PRINTING SMALL INTEGER MATRICES
   subroutine printi(title,arr)
   implicit none
   !
   !@(#) print small 2d integer arrays in row-column format
   !
   character(len=*),parameter :: all='(*(g0,1x))' ! a handy format
   character(len=*),intent(in)  :: title
   integer,intent(in)           :: arr(:,:)
   integer                      :: i
   character(len=:),allocatable :: biggest
      !
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
      !
   end subroutine printi
   end program demo_count
```

Results:

```text
 >   the numeric arrays we will compare
 >    1  3  5
 >    2  4  6
 >
 >    0  3  5
 >    7  4  8
 >   count a few basic things creating a mask from an expression
 >   count a>b           1
 >   count b<a           2
 >   count b==a           3
 >   check sum =  T
 >   make a mask identifying unequal elements ...
 >   the mask generated from a.ne.b
 >    T  F  F
 >    T  F  T
 >   count total and along rows and columns ...
 >  number of elements not equal
 >  (ie. total true elements in the mask)
 >    3
 >  count of elements not equal in each column
 >  (ie. total true elements in each column)
 >    2  0  1
 >  count of elements not equal in each row
 >  (ie. total true elements in each row)
 >    1  2
 >   lets try this with c(2,3,4)
 >     taking the result of the modulo
 >      z=1      z=2      z=3      z=4
 >     1 3 0 || 2 4 1 || 3 0 2 || 4 1 3 |
 >     2 4 1 || 3 0 2 || 4 1 3 || 0 2 4 |
 >
 >     would result in the mask ..
 >     F F T || F F F || F T F || F F F |
 >     F F F || F T F || F F F || T F F |
 >
 >    the total number of .true.values is
 >   4
 >
 >  counting up along a row and removing rows :( 3 4 )
 >   > [ 0, 0, 0, 1 ]
 >   > [ 0, 1, 1, 0 ]
 >   > [ 1, 0, 0, 0 ]
 >
 >  counting up along a column and removing columns :( 2 4 )
 >   > [ 1, 0, 1, 0 ]
 >   > [ 0, 1, 0, 1 ]
 >
 >  counting up along a depth and removing depths :( 2 3 )
 >   > [ 0, 1, 1 ]
 >   > [ 1, 1, 0 ]
```

### **Standard**

Fortran 95 , with KIND argument - Fortran 2003

### **See Also**

[**any**(3)](#any),
[**all**(3)](#all),
[**sum**(3)](#sum),

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
