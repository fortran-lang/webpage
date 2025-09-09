(transpose)=
## transpose

### **Name**

**transpose**(3) - \[ARRAY:MANIPULATION\] Transpose an array of rank two

### **Synopsis**

```fortran
    result = transpose(matrix)
```

```fortran
     function transpose(matrix)

      type(TYPE(kind=KIND)            :: transpose(N,M)
      type(TYPE(kind=KIND),intent(in) :: matrix(M,N)
```

### **Characteristics**

- **matrix** is an array of any type with a rank of two.
- The result will be the same type and kind as **matrix** and the
  reversed shape of the input array

### **Description**

**transpose**(3) transposes an array of rank two.

An array is transposed by interchanging the rows and columns of the
given matrix. That is, element (i,j) of the result has the value of
element (j,i) of the input for all (i,j).

### **Options**

- **matrix**
  : The array to transpose

### **Result**

The transpose of the input array. The result has the same type as
**matrix**, and has shape \[ m, n \] if **matrix** has shape \[ n, m \].

### **Examples**

Sample program:

```fortran
program demo_transpose
implicit none
integer,save :: xx(3,5)= reshape([&
    1,  2,  3,  4,  5,    &
   10, 20, 30, 40, 50,    &
   11, 22, 33, 44, -1055  &
 ],shape(xx),order=[2,1])

call print_matrix_int('xx array:',xx)
call print_matrix_int('xx array transposed:',transpose(xx))

contains

subroutine print_matrix_int(title,arr)
! print small 2d integer arrays in row-column format
implicit none
character(len=*),intent(in)  :: title
integer,intent(in)           :: arr(:,:)
integer                      :: i
character(len=:),allocatable :: biggest
   write(*,*)trim(title)  ! print title
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
end subroutine print_matrix_int

end program demo_transpose
```

Results:

```
    xx array:
    > [     1,     2,     3,     4,     5 ]
    > [    10,    20,    30,    40,    50 ]
    > [    11,    22,    33,    44, -1055 ]
    xx array transposed:
    > [     1,    10,    11 ]
    > [     2,    20,    22 ]
    > [     3,    30,    33 ]
    > [     4,    40,    44 ]
    > [     5,    50, -1055 ]
```

### **Standard**

Fortran 95

### **See also**

- [**merge**(3)](#merge) - Merge variables
- [**pack**(3)](#pack) - Pack an array into an array of rank one
- [**spread**(3)](#spread) - Add a dimension and replicate data
- [**unpack**(3)](#unpack) - Scatter the elements of a vector

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
