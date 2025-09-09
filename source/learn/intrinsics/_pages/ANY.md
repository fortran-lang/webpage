(any)=
## any

### **Name**

**any**(3) - \[ARRAY:REDUCTION\] Determines if any of the values in the logical array are _.true._

### **Synopsis**

```fortran
    result = any(mask [,dim])
```

```fortran
     function any(mask, dim)

      logical(kind=KIND),intent(in) :: mask(..)
      integer,intent(in),optional   :: dim
      logical(kind=KIND)            :: any(..)
```

### **Characteristics**

- **mask** is a _logical_ array
- **dim** is a scalar integer
- the result is a logical array if **dim** is supplied,
  otherwise it is a logical scalar.

### **Description**

**any**(3) determines if any of the values in the logical
array **mask** along dimension **dim** are _.true._.

### **Options**

- **mask**
  : an array of _logical_ expressions or values to be tested in groups
  or in total for a _.true._ value.

- **dim**
  : a whole number value that lies between one and **rank(mask)** that
  indicates to return an array of values along the indicated dimension
  instead of a scalar answer.

### **Result**

**any(mask)** returns a scalar value of type _logical_ where the kind type
parameter is the same as the kind type parameter of **mask**. If **dim**
is present, then **any(mask, dim)** returns an array with the rank of
**mask** minus 1. The shape is determined from the shape of **mask**
where the **dim** dimension is elided.

1.  **any(mask)** is _.true._ if any element of **mask** is _.true._;
    otherwise, it is _.false._. It also is _.false._ if **mask** has
    zero size.

2.  If the rank of **mask** is one, then **any(mask, dim)** is
    equivalent to **any(mask)**. If the rank is greater than one, then
    **any(mask, dim)** is determined by applying **any(mask)** to the
    array sections.

### **Examples**

Sample program:

```fortran
program demo_any
implicit none
logical,parameter :: T=.true., F=.false.
integer           :: a(2,3), b(2,3)
logical           :: bool
  ! basic usage
   bool = any([F,F,T,F])
   print *,bool
   bool = any([F,F,F,F])
   print *,bool
  ! fill two integer arrays with values for testing
   a = 1
   b = 1
   b(:,2) = 2
   b(:,3) = 3
  ! using any(3) with logical expressions you can compare two arrays
  ! in a myriad of ways
   ! first, print where elements of b are bigger than in a
   call printl( 'first print b > a             ', b > a         )
   ! now use any() to test
   call printl( 'any true values?  any(b > a)  ', any(b > a )   )
   call printl( 'again by columns? any(b > a,1)', any(b > a, 1) )
   call printl( 'again by rows?    any(b > a,2)', any(b > a, 2) )
contains
! CONVENIENCE ROUTINE. this is not specific to ANY()
subroutine printl(title,a)
use, intrinsic :: iso_fortran_env, only : &
 & stderr=>ERROR_UNIT,&
 & stdin=>INPUT_UNIT,&
 & stdout=>OUTPUT_UNIT
implicit none

!@(#) print small 2d logical scalar, vector, or matrix

character(len=*),parameter   :: all='(*(g0,1x))'
character(len=*),parameter   :: row='(" > [ ",*(l1:,","))'
character(len=*),intent(in)  :: title
logical,intent(in)           :: a(..)
integer                      :: i
   write(*,*)
   write(*,all,advance='no')trim(title),&
    & ' : shape=',shape(a),',rank=',rank(a),',size=',size(a)
   ! get size and shape of input
   select rank(a)
   rank (0); write(*,'(a)')'(a scalar)'
      write(*,fmt=row,advance='no')a
      write(*,'(" ]")')
   rank (1); write(*,'(a)')'(a vector)'
      do i=1,size(a)
         write(*,fmt=row,advance='no')a(i)
         write(*,'(" ]")')
      enddo
   rank (2); write(*,'(a)')'(a matrix) '
      do i=1,size(a,dim=1)
         write(*,fmt=row,advance='no')a(i,:)
         write(*,'(" ]")')
      enddo
   rank default
      write(stderr,*)'*printl* did not expect rank=', rank(a), &
       & 'shape=', shape(a),'size=',size(a)
      stop '*printl* unexpected rank'
   end select

end subroutine printl

end program demo_any
```

Results:

```text
 >  T
 >  F
 >
 > first print b > a : shape=23,rank=2,size=6(a matrix)
 >  > [ F,T,T ]
 >  > [ F,T,T ]
 >
 > any true values?  any(b > a) : shape=,rank=0,size=1(a scalar)
 >  > [ T ]
 >
 > again by columns? any(b > a,1) : shape=3,rank=1,size=3(a vector)
 >  > [ F ]
 >  > [ T ]
 >  > [ T ]
 >
 > again by rows?    any(b > a,2) : shape=2,rank=1,size=2(a vector)
 >  > [ T ]
 >  > [ T ]
```

### **Standard**

Fortran 95

### **See Also**

[**all**(3)](#all)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
