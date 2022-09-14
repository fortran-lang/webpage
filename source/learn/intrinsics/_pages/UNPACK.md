## unpack

### **Name**

**unpack**(3) - \[ARRAY CONSTRUCTION\] scatter the elements of a vector
into an array using a mask

### **Syntax**

```fortran
result = unpack(vector, mask, field)

 type(TYPE(kind=KIND)),intent(in) :: vector(:)
 logical,intent(in)               :: mask(..)
 type(TYPE(kind=KIND)),intent(in) :: field(..)
 type(TYPE(kind=KIND))            :: result(..)
```
### **Description**

Scatter the elements of **vector** into a copy of an array **field**
of any rank using _.true._ values from **mask** in array element order
to specify placement of the **vector** values.

So a copy of **field** is generated with select elements replaced with
values from **vector**. This allows for complex replacement patterns
that would be difficult when using array syntax or multiple assignment
statements, particularly when the replacements are conditional.

### **Arguments**

- **vector**
  : New values to place into specified locations in **field**. Shall
  be an array of any type and rank one. It shall have at least as many
  elements as **mask** has **.true.** values.

- **mask**
  : Shall be an array of type _logical_ that specifies which values
  in **field** are to be replaced with values from **vector**.

- **field**
  : The original data to be edited. Shall be of the same type and type
  parameters as **vector** and shall be conformable with **mask**.


### **Returns**

The result is an array of the same type and type parameters as **vector**
and the same shape as **mask**.

The element of the result that corresponds to the ith true element
of MASK, in array element order, has the value VECTOR (i) for i =
1, 2, . . ., t, where t is the number of true values in MASK. Each
other element has a value equal to FIELD if FIELD is scalar or to the
corresponding element of FIELD if it is an array.

The resulting array corresponds to **field** with **.true.** elements
of **mask** replaced by values from **vector** in array element order.


### **Examples**
Particular values may be "scattered" to particular positions in an array by using
```text
                       1 0 0
    If M is the array  0 1 0
                       0 0 1

    V is the array [1, 2, 3],
                               . T .
    and Q is the logical mask  T . .
                               . . T
    where "T" represents true and "." represents false, then the result of

    UNPACK (V, MASK = Q, FIELD = M) has the value

      1 2 0
      1 1 0
      0 0 3

    and the result of UNPACK (V, MASK = Q, FIELD = 0) has the value

      0 2 0
      1 0 0
      0 0 3
```

Sample program:

```fortran
program demo_unpack
implicit none
logical,parameter :: T=.true., F=.false.

integer :: vector(2)  = [1,1]

! mask and field must conform
integer,parameter :: r=2, c=2
logical :: mask(r,c)  = reshape([ T,F,F,T ],[2,2])
integer :: field(r,c) = 0, unity(2,2)

   ! basic usage
   unity = unpack( vector, mask, field )
   call print_matrix_int('unity=', unity)

   ! if FIELD is a scalar it is used to fill all the elements
   ! not assigned to by the vector and mask.
   call print_matrix_int('scalar field',         &
   & unpack(                                     &
   & vector=[ 1, 2, 3, 4 ],                      &
   & mask=reshape([ T,F,T,F,F,F,T,F,T ], [3,3]), &
   & field=0) )

contains

   subroutine print_matrix_int(title,arr)
   ! convenience routine:
   ! just prints small integer arrays in row-column format
   implicit none
   character(len=*),intent(in)  :: title
   integer,intent(in)           :: arr(:,:)
   integer                      :: i
   character(len=:),allocatable :: biggest

        write(*,*)trim(title)
        ! make buffer to write integer into
        biggest='           '
        ! find how many characters to use for integers
        write(biggest,'(i0)')ceiling(log10(real(maxval(abs(arr)))))+2
        ! use this format to write a row
        biggest='("  [",*(i'//trim(biggest)//':,","))'
        ! print one row of array at a time
        do i=1,size(arr,dim=1)
           write(*,fmt=biggest,advance='no')arr(i,:)
           write(*,'(" ]")')
        enddo
   end subroutine print_matrix_int

end program demo_unpack
```
  Results:

```text
   > unity=
   >  [ 1, 0 ]
   >  [ 0, 1 ]
   > scalar field
   >  [  1,  0,  3 ]
   >  [  0,  0,  0 ]
   >  [  2,  0,  4 ]
```

### **Standard**

Fortran 95 and later

### **See Also**

[**merge**(3)](MERGE),
[**pack**(3)](PACK),
[**spread**(3)](SPREAD)

_fortran-lang intrinsic descriptions_
