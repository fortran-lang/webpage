(spread)=
## spread

### **Name**

**spread**(3) - \[ARRAY:CONSTRUCTION\] Add a dimension and replicate data

### **Synopsis**

```fortran
    result = spread(source, dim, ncopies)
```

```fortran
     TYPE(kind=KIND) function spread(source, dim, ncopies)

      TYPE(kind=KIND)             :: source(..)
      integer(kind=**),intent(in) :: dim
      integer(kind=**),intent(in) :: ncopies
```

### **Characteristics**

- **source** is a scalar or array of any type.
- **dim** is an _integer_ scalar
- **ncopies** is an integer scalar

### **Description**

**spread**(3) replicates a **source** array along a specified dimension
**dim**. The copy is repeated **ncopies** times.

So to add additional rows to a matrix **dim=1** would be used, but to
add additional rows **dim=2** would be used, for example.

If **source** is scalar, the size of the resulting vector is **ncopies**
and each element of the result has a value equal to **source**.

### **Options**

- **source**
  : a scalar or array of any type and a rank less than fifteen.

- **dim**

  : The additional dimension value in the range from
  **1** to **n+1**, where **n** equals the rank of **source**.

- **ncopies**
  : the number of copies of the original data to generate

### **Result**

The result is an array of the same type as **source** and has rank **n+1**
where **n** equals the rank of **source**.

### **Examples**

Sample program:

```fortran
program demo_spread
implicit none

integer a1(4,3), a2(3,4), v(4), s

   write(*,'(a)' ) &
   'TEST SPREAD(3)                                      ', &
   '  SPREAD(3) is a FORTRAN90 function which replicates', &
   '  an array by adding a dimension.                   ', &
   ' '

   s = 99
   call printi('suppose we have a scalar S',s)

   write(*,*) 'to add a new dimension (1) of extent 4 call'
   call printi('spread( s, dim=1, ncopies=4 )',spread ( s, 1, 4 ))

   v = [ 1, 2, 3, 4 ]
   call printi(' first we will set V to',v)

   write(*,'(a)')' and then do "spread ( v, dim=2, ncopies=3 )"'
   a1 = spread ( v, dim=2, ncopies=3 )
   call printi('this adds a new dimension (2) of extent 3',a1)

   a2 = spread ( v, 1, 3 )
   call printi(' spread(v,1,3) adds a new dimension (1) of extent 3',a2)
   ! add more
   a2 = spread ( v, 1, 3 )
   call printi(' spread(v,1,3) adds a new dimension (1) of extent 3',a2)

contains
! CONVENIENCE ROUTINE; NOT DIRECTLY CONNECTED TO SPREAD(3)
subroutine printi(title,a)
use, intrinsic :: iso_fortran_env, only : stderr=>ERROR_UNIT,&
 & stdin=>INPUT_UNIT, stdout=>OUTPUT_UNIT
implicit none

!@(#) print small 2d integer scalar, vector, matrix in row-column format

character(len=*),parameter   :: all='(" ",*(g0,1x))'
character(len=*),intent(in)  :: title
character(len=20)            :: row
integer,intent(in)           :: a(..)
integer                      :: i

   write(*,all,advance='no')trim(title)
   ! select rank of input
   select rank(a)
   rank (0); write(*,'(a)')' (a scalar)'
      write(*,'(" > [ ",i0," ]")')a
   rank (1); write(*,'(a)')' (a vector)'
      ! find how many characters to use for integers
      write(row,'(i0)')ceiling(log10(real(maxval(abs(a)))))+2
      ! use this format to write a row
      row='(" > [",*(i'//trim(row)//':,","))'
      do i=1,size(a)
         write(*,fmt=row,advance='no')a(i)
         write(*,'(" ]")')
      enddo
   rank (2); write(*,'(a)')' (a matrix) '
      ! find how many characters to use for integers
      write(row,'(i0)')ceiling(log10(real(maxval(abs(a)))))+2
      ! use this format to write a row
      row='(" > [",*(i'//trim(row)//':,","))'
      do i=1,size(a,dim=1)
         write(*,fmt=row,advance='no')a(i,:)
         write(*,'(" ]")')
      enddo
   rank default
      write(stderr,*)'*printi* did not expect rank=', rank(a), &
       & 'shape=', shape(a),'size=',size(a)
      stop '*printi* unexpected rank'
   end select
   write(*,all) '>shape=',shape(a),',rank=',rank(a),',size=',size(a)
   write(*,*)

end subroutine printi

end program demo_spread
```

Results:

```text
   TEST SPREAD(3)
     SPREAD(3) is a FORTRAN90 function which replicates
     an array by adding a dimension.

    suppose we have a scalar S  (a scalar)
    > [ 99 ]
    >shape= ,rank= 0 ,size= 1

    to add a new dimension (1) of extent 4 call
    spread( s, dim=1, ncopies=4 )  (a vector)
    > [  99 ]
    > [  99 ]
    > [  99 ]
    > [  99 ]
    >shape= 4 ,rank= 1 ,size= 4

     first we will set V to  (a vector)
    > [  1 ]
    > [  2 ]
    > [  3 ]
    > [  4 ]
    >shape= 4 ,rank= 1 ,size= 4

    and then do "spread ( v, dim=2, ncopies=3 )"
    this adds a new dimension (2) of extent 3  (a matrix)
    > [  1,  1,  1 ]
    > [  2,  2,  2 ]
    > [  3,  3,  3 ]
    > [  4,  4,  4 ]
    >shape= 4 3 ,rank= 2 ,size= 12

     spread(v,dim=1,ncopies=3) adds a new dimension (1) (a matrix)
    > [  1,  2,  3,  4 ]
    > [  1,  2,  3,  4 ]
    > [  1,  2,  3,  4 ]
    >shape= 3 4 ,rank= 2 ,size= 12
```

### **Standard**

Fortran 95

### **See Also**

[**merge**(3)](#merge),
[**pack**(3)](#pack),
[**unpack**(3)](#unpack)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

<!--
when adding dimension 3,4,5, ... why is 15 not allowed if 16 is allowed?

need an illustration of what happens with higher dimension array
-->
