(matmul)=
## matmul

### **Name**

**matmul**(3) - \[TRANSFORMATIONAL\] Numeric or logical matrix
multiplication

### **Synopsis**

```fortran
    result = matmul(matrix_a,matrix_b)
```

```fortran
     function matmul(matrix_a, matrix_b)

      type(TYPE1(kind=**)       :: matrix_a(..)
      type(TYPE2(kind=**)       :: matrix_b(..)
      type(TYPE(kind=PROMOTED)) :: matmul(..)
```

### **Characteristics**

- **matrix_a** is a numeric (_integer_, _real_, or _complex_ ) or
  _logical_ array of rank one two.
- **matrix_b** is a numeric (_integer_, _real_, or _complex_ ) or
  _logical_ array of rank one two.
- At least one argument must be rank two.
- the size of the first dimension of **matrix_b** must equal the size
  of the last dimension of **matrix_a**.
- the type of the result is the same as if an element of each argument
  had been multiplied as a RHS expression (that is, if the arguments
  are not of the same type the result follows the same rules of promotion
  as a simple scalar multiplication of the two types would produce)
- If one argument is _logical_, both must be _logical_. For logicals
  the resulting type is as if the _.and._ operator has been used on
  elements from the arrays.
- The shape of the result depends on the shapes of the arguments
  as described below.

### **Description**

**matmul**(3) performs a matrix multiplication on numeric or logical
arguments.

### **Options**

- **matrix_a**
  : A numeric or logical array with a rank of one or two.

- **matrix_b**
  : A numeric or logical array with a rank of one or two. The last
  dimension of **matrix_a** and the first dimension of **matrix_b**
  must be equal.

  Note that **matrix_a** and **matrix_b** may be different numeric
  types.

### **Result**

#### **Numeric Arguments**

If **matrix_a** and **matrix_b** are numeric the result is an
array containing the conventional matrix product of **matrix_a**
and **matrix_b**.

First, for the numeric expression **C=matmul(A,B)**

- Any vector **A(n)** is treated as a row vector **A(1,n)**.
- Any vector **B(n)** is treated as a column vector **B(n,1)**.

##### **Shape and Rank**

The shape of the result can then be determined as the number of rows
of the first matrix and the number of columns of the second; but if
any argument is of rank one (a vector) the result is also rank one.
Conversely when both arguments are of rank two, the result has a rank
of two. That is ...

- If **matrix_a** has shape [n,m] and **matrix_b** has shape [m,k],
  the result has shape [n,k].
- If **matrix_a** has shape [m] and **matrix_b** has shape [m,k],
  the result has shape [k].
- If **matrix_a** has shape [n,m] and **matrix_b** has shape [m],
  the result has shape [n].

##### **Values**

Then element **C(i,j)** of the product is obtained by multiplying
term-by-term the entries of the ith row of **A** and the jth column
of **B**, and summing these products. In other words, **C(i,j)**
is the dot product of the ith row of **A** and the jth column of **B**.

#### **Logical Arguments**

##### **Values**

If **matrix_a** and **matrix_b** are of type logical, the array elements
of the result are instead:

```fortran
  Value_of_Element (i,j) = &
  ANY( (row_i_of_MATRIX_A) .AND. (column_j_of_MATRIX_B) )
```

### **Examples**

Sample program:

```fortran
program demo_matmul
implicit none
integer :: a(2,3), b(3,2), c(2), d(3), e(2,2), f(3), g(2), v1(4),v2(4)
   a = reshape([1, 2, 3, 4, 5, 6], [2, 3])
   b = reshape([10, 20, 30, 40, 50, 60], [3, 2])
   c = [1, 2]
   d = [1, 2, 3]
   e = matmul(a, b)
   f = matmul(c,a)
   g = matmul(a,d)

   call print_matrix_int('A is ',a)
   call print_matrix_int('B is ',b)
   call print_vector_int('C is ',c)
   call print_vector_int('D is ',d)
   call print_matrix_int('E is matmul(A,B)',e)
   call print_vector_int('F is matmul(C,A)',f)
   call print_vector_int('G is matmul(A,D)',g)

   ! look at argument shapes when one is a vector
   write(*,'(" > shape")')
   ! at least one argument must be of rank two
   ! so for two vectors at least one must be reshaped
   v1=[11,22,33,44]
   v2=[10,20,30,40]

   ! these return a vector C(1:1)
   ! treat A(1:n) as A(1:1,1:n)
   call print_vector_int('Cd is a vector (not a scalar)',&
   & matmul(reshape(v1,[1,size(v1)]),v2))
   ! or treat B(1:m) as B(1:m,1:1)
   call print_vector_int('cD is a vector too',&
   & matmul(v1,reshape(v2,[size(v2),1])))

   ! or treat A(1:n) as A(1:1,1:n) and B(1:m) as B(1:m,1:1)
   ! but note this returns a matrix C(1:1,1:1) not a vector!
   call print_matrix_int('CD is a matrix',matmul(&
   & reshape(v1,[1,size(v1)]), &
   & reshape(v2,[size(v2),1])))

contains

! CONVENIENCE ROUTINES TO PRINT IN ROW-COLUMN ORDER
subroutine print_vector_int(title,arr)
character(len=*),intent(in)  :: title
integer,intent(in)           :: arr(:)
   call print_matrix_int(title,reshape(arr,[1,shape(arr)]))
end subroutine print_vector_int

subroutine print_matrix_int(title,arr)
!@(#) print small 2d integer arrays in row-column format
character(len=*),parameter :: all='(" > ",*(g0,1x))' ! a handy format
character(len=*),intent(in)  :: title
integer,intent(in)           :: arr(:,:)
integer                      :: i
character(len=:),allocatable :: biggest

   print all
   print all, trim(title)
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

end program demo_matmul
```

Results:

```text
    >
    > A is
    > [  1,  3,  5 ]
    > [  2,  4,  6 ]
    >
    > B is
    > [  10,  40 ]
    > [  20,  50 ]
    > [  30,  60 ]
    >
    > C is
    > [  1,  2 ]
    >
    > D is
    > [  1,  2,  3 ]
    >
    > E is matmul(A,B)
    > [  220,  490 ]
    > [  280,  640 ]
    >
    > F is matmul(C,A)
    > [   5,  11,  17 ]
    >
    > G is matmul(A,D)
    > [  22,  28 ]
    > shape
    >
    > Cd is a vector (not a scalar)
    > [  3300 ]
    >
    > cD is a vector too
    > [  3300 ]
    >
    > CD is a matrix
    > [  3300 ]
```

### **Standard**

Fortran 95

### **See Also**

[**product**(3)](#product),
[**transpose**(3)](#transpose)

### **Resources**

- [Matrix multiplication : Wikipedia](https://en.wikipedia.org/wiki/Matrix_multiplication)
- The Winograd variant of Strassen's matrix-matrix multiply algorithm may
  be of interest for optimizing multiplication of very large matrices. See

```text
    "GEMMW: A portable level 3 BLAS Winograd variant of Strassen's
    matrix-matrix multiply algorithm",

    Douglas, C. C., Heroux, M., Slishman, G., and Smith, R. M.,
    Journal of Computational Physics,
    Vol. 110, No. 1, January 1994, pages 1-10.

  The numerical instabilities of Strassen's method for matrix
  multiplication requires special processing.
```

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
