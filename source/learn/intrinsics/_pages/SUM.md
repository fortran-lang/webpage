(sum)=
## sum

### **Name**

**sum**(3) - \[ARRAY:REDUCTION\] Sum the elements of an array

### **Synopsis**

```fortran
   result = sum(array [,dim[,mask]] | [mask] )
```

```fortran
     TYPE(kind=KIND) function sum(array, dim, mask)

      TYPE(kind=KIND),intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **array** may be of any numeric type - _integer_, _real_ or _complex_.
- **dim** is an _integer_
- **mask** is _logical_ and conformable with **array**.
- The result is of the same type and kind as **array**. It is scalar
  if **dim** is not present or **array** is a vector, else it is an array.

### **Description**

**sum**(3) adds the elements of **array**.

When only **array** is specified all elements are summed, but groups
of sums may be returned along the dimension specified by **dim**
and/or elements to add may be selected by a logical mask.

No method is designated for how the sum is conducted, so whether or not
accumulated error is compensated for is processor-dependent.

### **Options**

- **array**
  : an array containing the elements to add

- **dim**
  : a value in the range from 1 to n, where n equals the rank (the number
  of dimensions) of **array**. **dim** designates the dimension
  along which to create sums. When absent a scalar sum of the elements
  optionally selected by **mask** is returned.

- **mask**
  : an array of the same shape as **array** that designates
  which elements to add. If absent all elements are used in the sum(s).

### **Result**

If **dim** is absent, a scalar with the sum of all selected elements
in **array** is returned. Otherwise, an array of rank n-1, where n
equals the rank of **array**, and a shape similar to that of **array**
with dimension **dim** dropped is returned. Since a vector has a rank
of one, the result is a scalar (if n==1, n-1 is zero; and a rank of
zero means a scalar).

### **Examples**

Sample program:

```fortran
program demo_sum
implicit none
integer :: vector(5) , matrix(3,4), box(5,6,7)

   vector = [ 1, 2, -3, 4, 5 ]

   matrix(1,:)=[  -1,   2,    -3,   4    ]
   matrix(2,:)=[  10,   -20,  30,   -40  ]
   matrix(3,:)=[  100,  200, -300,  400  ]

   box=11

  ! basics
   print *, 'sum all elements:',sum(vector)
   print *, 'real :',sum([11.0,-5.0,20.0])
   print *, 'complex :',sum([(1.1,-3.3),(4.0,5.0),(8.0,-6.0)])
  ! with MASK option
   print *, 'sum odd elements:',sum(vector, mask=mod(vector, 2)==1)
   print *, 'sum positive values:', sum(vector, mask=vector>0)

   call printi('the input array', matrix )
   call printi('sum of all elements in matrix', sum(matrix) )
   call printi('sum of positive elements', sum(matrix,matrix>=0) )
  ! along dimensions
   call printi('sum along rows', sum(matrix,dim=1) )
   call printi('sum along columns', sum(matrix,dim=2) )
   call printi('sum of a vector is always a scalar', sum(vector,dim=1) )
   call printi('sum of a volume by row', sum(box,dim=1) )
   call printi('sum of a volume by column', sum(box,dim=2) )
   call printi('sum of a volume by depth', sum(box,dim=3) )

contains
! CONVENIENCE ROUTINE; NOT DIRECTLY CONNECTED TO SPREAD(3)
subroutine printi(title,a)
use, intrinsic :: iso_fortran_env, only : stderr=>ERROR_UNIT,&
 & stdin=>INPUT_UNIT, stdout=>OUTPUT_UNIT
implicit none

!@(#) print small 2d integer scalar, vector, matrix in row-column format

character(len=*),intent(in)  :: title
integer,intent(in)           :: a(..)

character(len=*),parameter   :: all='(" ",*(g0,1x))'
character(len=20)            :: row
integer,allocatable          :: b(:,:)
integer                      :: i
   write(*,all,advance='no')trim(title)
   ! copy everything to a matrix to keep code simple
   select rank(a)
   rank (0); write(*,'(a)')' (a scalar)'; b=reshape([a],[1,1])
   rank (1); write(*,'(a)')' (a vector)'; b=reshape(a,[size(a),1])
   rank (2); write(*,'(a)')' (a matrix)'; b=a
   rank default; stop '*printi* unexpected rank'
   end select
   ! find how many characters to use for integers
   write(row,'(i0)')ceiling(log10(real(maxval(abs(b)))))+2
   ! use this format to write a row
   row='(" > [",*(i'//trim(row)//':,","))'
   do i=1,size(b,dim=1)
      write(*,fmt=row,advance='no')b(i,:)
      write(*,'(" ]")')
   enddo
   write(*,all) '>shape=',shape(a),',rank=',rank(a),',size=',size(a)
   write(*,*)
end subroutine printi
end program demo_sum
```

Results:

```text
    sum all elements:           9
    real :   26.00000
    complex : (13.10000,-4.300000)
    sum odd elements:           6
    sum positive values:          12
    the input array  (a matrix)
    > [   -1,    2,   -3,    4 ]
    > [   10,  -20,   30,  -40 ]
    > [  100,  200, -300,  400 ]
    >shape= 3 4 ,rank= 2 ,size= 12

    sum of all elements in matrix  (a scalar)
    > [  382 ]
    >shape= ,rank= 0 ,size= 1

    sum of positive elements  (a scalar)
    > [  746 ]
    >shape= ,rank= 0 ,size= 1

    sum along rows  (a vector)
    > [  109 ]
    > [  182 ]
    > [ -273 ]
    > [  364 ]
    >shape= 4 ,rank= 1 ,size= 4

    sum along columns  (a vector)
    > [    2 ]
    > [  -20 ]
    > [  400 ]
    >shape= 3 ,rank= 1 ,size= 3

    sum of a vector is always a scalar  (a scalar)
    > [  9 ]
    >shape= ,rank= 0 ,size= 1

    sum of a volume by row  (a matrix)
    > [  55,  55,  55,  55,  55,  55,  55 ]
    > [  55,  55,  55,  55,  55,  55,  55 ]
    > [  55,  55,  55,  55,  55,  55,  55 ]
    > [  55,  55,  55,  55,  55,  55,  55 ]
    > [  55,  55,  55,  55,  55,  55,  55 ]
    > [  55,  55,  55,  55,  55,  55,  55 ]
    >shape= 6 7 ,rank= 2 ,size= 42

    sum of a volume by column  (a matrix)
    > [  66,  66,  66,  66,  66,  66,  66 ]
    > [  66,  66,  66,  66,  66,  66,  66 ]
    > [  66,  66,  66,  66,  66,  66,  66 ]
    > [  66,  66,  66,  66,  66,  66,  66 ]
    > [  66,  66,  66,  66,  66,  66,  66 ]
    >shape= 5 7 ,rank= 2 ,size= 35

    sum of a volume by depth  (a matrix)
    > [  77,  77,  77,  77,  77,  77 ]
    > [  77,  77,  77,  77,  77,  77 ]
    > [  77,  77,  77,  77,  77,  77 ]
    > [  77,  77,  77,  77,  77,  77 ]
    > [  77,  77,  77,  77,  77,  77 ]
    >shape= 5 6 ,rank= 2 ,size= 30
```

### **Standard**

Fortran 95

### **See Also**

- [**all**(3)](#all) - Determines if all the values are true
- [**any**(3)](#any) - Determines if any of the values in the logical array are true.
- [**count**(3)](#count) - Count true values in an array
- [**maxval**(3)](#maxval) - Determines the maximum value in an array
- [**minval**(3)](#minval) - Minimum value of an array
- [**product**(3)](#product) - Product of array elements
- [**merge**(3)](#merge) - Merge variables

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
