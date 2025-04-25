(findloc)=
## findloc

### **Name**

**findloc**(3) - \[ARRAY:LOCATION\] Location of first element of ARRAY
identified by MASK along dimension DIM matching a target value

### **Synopsis**

```fortran
    result = findloc (array, value, dim [,mask] [,kind] [,back]) |
             findloc (array, value [,mask] [,kind] [,back])
```

```fortran
     function findloc (array, value, dim, mask, kind, back)

      type TYPE(kind=KIND),intent(in)      :: array(..)
      type TYPE(kind=KIND),intent(in)      :: value
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
      integer(kind=**),intent(in),optional :: kind
      logical(kind=**),intent(in),optional :: back
```

### **Characteristics**

- **array** is an array of any intrinsic type.
- **value** shall be scalar but in type conformance with **array**,
  as specified for the operator == or the operator .EQV..
- **dim** an _integer_ corresponding to a dimension of **array**.
  The corresponding actual argument shall not be an optional dummy
  argument.
- **mask** is logical and shall be conformable with **array**.
- **kind** a scalar integer initialization expression (ie. a constant)
- **back** a logical scalar.
- the result is _integer_ of default kind or kind **kind** if the
  **kind** argument is present. If **dim** does not appear, the result
  is an array of rank one and of size equal to the rank of **array**;
  otherwise, the result is an array of the same rank and shape as
  **array** reduced by the dimension **dim**.

**NOTE**: a kind designated as \*\* may be any supported kind for the type

### **Description**

**findloc**(3) returns the location of the first element of **array**
identified by **mask** along dimension **dim** having a value equal
to **value**.

If both **array** and **value** are of type logical, the comparison is
performed with the **.eqv.** operator; otherwise, the comparison is
performed with the == operator. If the value of the comparison is
_.true._, that element of **array** matches **value**.

If only one element matches **value**, that element's subscripts are
returned. Otherwise, if more than one element matches **value** and
**back** is absent or present with the value _.false._, the element whose
subscripts are returned is the first such element, taken in array
element order. If **back** is present with the value _.true._, the element
whose subscripts are returned is the last such element, taken in array
element order.

### **Options**

- **array**
  : shall be an array of intrinsic type.

- **value**
  : shall be scalar and in type conformance with **array**.

- **dim**
  : shall be an integer scalar with a value in the range 1 <= **DIM** <=
  n, where n is the rank of **array**. The corresponding actual argument
  shall not be an optional dummy argument.

- **mask**
  : (optional) shall be of type logical and shall be conformable with
  **array**.

- **kind**
  : (optional) shall be a scalar integer initialization expression.

- **back**
  : (optional) shall be a logical scalar.

### **Result**

**kind** is present, the kind type
parameter is that specified by the value of **kind**; otherwise the kind
type parameter is that of default integer type. If **dim** does not appear,
the result is an array of rank one and of size equal to the rank of
**array**; otherwise, the result is of rank n - 1 and shape

```
   [d1, d2, . . ., dDIM-1, dDIM+1, . . ., dn ]
```

where

```
   [d1, d2, . . ., dn ]
```

is the shape of **array**.

### **Result**

- **Case (i):**
  The result of **findloc (array, value)** is a rank-one array whose
  element values are the values of the subscripts of an element of
  **array** whose value matches **value**. If there is such a value, the
  ith subscript returned lies in the range 1 to ei, where ei is the
  extent of the ith dimension of **array**. If no elements match **value**
  or **array** has size zero, all elements of the result are zero.

- **Case (ii):**
  the result of **findloc (array, value, mask = mask)** is a
  rank-one array whose element values are the values of the subscripts
  of an element of **array**, corresponding to a true element of **mask**,
  whose value matches **value**. If there is such a value, the ith
  subscript returned lies in the range 1 to ei, where ei is the
  extent of the ith dimension of **array**. If no elements match
  **value**, **array** has size zero, or every element of **mask** has the
  value false, all elements of the result are zero.

### **Examples**

Sample program:

```fortran
program demo_findloc
logical,parameter :: T=.true., F=.false.
integer,allocatable :: ibox(:,:)
logical,allocatable :: mask(:,:)
  ! basics
   ! the first element matching the value is returned AS AN ARRAY
   call printi('== 6',findloc ([2, 6, 4, 6], value = 6))
   call printi('== 6',findloc ([2, 6, 4, 6], value = 6,back=.true.))
   ! the first element matching the value is returned AS A SCALAR
   call printi('== 6',findloc ([2, 6, 4, 6], value = 6,dim=1))
   call printi('== 6',findloc ([2, 6, 4, 6], value = 6,back=.true.,dim=1))

   ibox=reshape([ 0,-5,  7, 7, &
                  3, 4, -1, 2, &
                  1, 5,  6, 7] ,shape=[3,4],order=[2,1])

   mask=reshape([ T, T, F, T, &
                  T, T, F, T, &
                  T, T, F, T] ,shape=[3,4],order=[2,1])

   call printi('array is', ibox )
   call printl('mask  is', mask )
   print *, 'so for == 7 and back=.false.'
   call printi('so for == 7 the address of the element is', &
           & findloc (ibox, 7, mask = mask) )
   print *, 'so for == 7 and back=.true.'
   call printi('so for == 7 the address of the element is', &
           & findloc (ibox, 7, mask = mask, back=.true.) )

   print *,'This is independent of declared lower bounds for the array'

   print *, ' using dim=N'
   ibox=reshape([ 1,  2, -9,  &
                  2,  2,  6 ] ,shape=[2,3],order=[2,1])

   call printi('array is', ibox )
   ! has the value [2, 1, 0] and
   call printi('',findloc (ibox, value = 2, dim = 1) )
   ! has the value [2, 1].
   call printi('',findloc (ibox, value = 2, dim = 2) )
contains
! GENERIC ROUTINES TO PRINT MATRICES
subroutine printl(title,a)
implicit none
!@(#) print small 2d logical scalar, vector, matrix in row-column format
character(len=*),intent(in)  :: title
logical,intent(in)           :: a(..)

character(len=*),parameter   :: row='(" > [ ",*(l1:,","))'
character(len=*),parameter   :: all='(" ",*(g0,1x))'
logical,allocatable          :: b(:,:)
integer                      :: i
   write(*,all,advance='no')trim(title)
   ! copy everything to a matrix to keep code simple
   select rank(a)
   rank (0); write(*,'(a)')' (a scalar)'; b=reshape([a],[1,1])
   rank (1); write(*,'(a)')' (a vector)'; b=reshape(a,[size(a),1])
   rank (2); write(*,'(a)')' (a matrix)'; b=a
   rank default; stop '*printl* unexpected rank'
   end select
   do i=1,size(b,dim=1)
      write(*,fmt=row,advance='no')b(i,:)
      write(*,'(" ]")')
   enddo
   write(*,all) '>shape=',shape(a),',rank=',rank(a),',size=',size(a)
   write(*,*)
end subroutine printl

subroutine printi(title,a)
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
end program demo_findloc
```

Results:

```text
 >  == 6  (a vector)
 >  > [  2 ]
 >  >shape= 1 ,rank= 1 ,size= 1
 >
 >  == 6  (a vector)
 >  > [  4 ]
 >  >shape= 1 ,rank= 1 ,size= 1
 >
 >  == 6  (a scalar)
 >  > [  2 ]
 >  >shape= ,rank= 0 ,size= 1
 >
 >  == 6  (a scalar)
 >  > [  4 ]
 >  >shape= ,rank= 0 ,size= 1
 >
 >  array is  (a matrix)
 >  > [  0, -5,  7,  7 ]
 >  > [  3,  4, -1,  2 ]
 >  > [  1,  5,  6,  7 ]
 >  >shape= 3 4 ,rank= 2 ,size= 12
 >
 >  mask  is  (a matrix)
 >  > [ T,T,F,T ]
 >  > [ T,T,F,T ]
 >  > [ T,T,F,T ]
 >  >shape= 3 4 ,rank= 2 ,size= 12
 >
 >  so for == 7 and back=.false.
 >  so for == 7 the address of the element is  (a vector)
 >  > [  1 ]
 >  > [  4 ]
 >  >shape= 2 ,rank= 1 ,size= 2
 >
 >  so for == 7 and back=.true.
 >  so for == 7 the address of the element is  (a vector)
 >  > [  3 ]
 >  > [  4 ]
 >  >shape= 2 ,rank= 1 ,size= 2
 >
 >  This is independent of declared lower bounds for the array
 >   using dim=N
 >  array is  (a matrix)
 >  > [  1,  2, -9 ]
 >  > [  2,  2,  6 ]
 >  >shape= 2 3 ,rank= 2 ,size= 6
 >
 >    (a vector)
 >  > [  2 ]
 >  > [  1 ]
 >  > [  0 ]
 >  >shape= 3 ,rank= 1 ,size= 3
 >
 >    (a vector)
 >  > [  2 ]
 >  > [  1 ]
 >  >shape= 2 ,rank= 1 ,size= 2
 >
```

### **Standard**

Fortran 95

### **See Also**

- [**maxloc**(3)](#maxloc) - Location of the maximum value within an array
- [**minloc**(3)](#minloc) - Location of the minimum value within an array

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
