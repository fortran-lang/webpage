(norm2)=
## norm2

### **Name**

**norm2**(3) - \[MATHEMATICS\] Euclidean vector norm

### **Synopsis**

```fortran
    result = norm2(array, [dim])
```

```fortran
     real(kind=KIND) function norm2(array, dim)

      real(kind=KIND),intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
```

### **Characteristics**

- **array** shall be an array of type _real_.
- **dim** shall be a scalar of type _integer_
- The result is of the same type as **array**.

### **Description**

**norm2**(3) calculates the Euclidean vector norm (L_2 norm or
generalized L norm) of **array** along dimension **dim**.

### **Options**

- **array**
  : the array of input values for the L_2 norm computations

- **dim**
  : a value in the range from **1** to **rank(array)**.

### **Result**

If **dim** is absent, a scalar with the square root of the sum of squares
of the elements of **array** is returned.

Otherwise, an array of rank **n-1**, where **n** equals the rank of
**array**, and a shape similar to that of **array** with dimension DIM
dropped is returned.

      Case (i):     The result of NORM2 (X) has a value equal to a
                    processor-dependent approximation to the generalized
                    L norm of X, which is the square root of the sum of
                    the squares of the elements of X. If X has size zero,
                    the result has the value zero.

      Case (ii):    The result of NORM2 (X, DIM=DIM) has a value equal
                    to that of NORM2 (X) if X has rank one. Otherwise,
                    the resulting array is reduced in rank with dimension
                    **dim** removed, and each remaining elment is the
                    result of NORM2(X) for the values along dimension
                    **dim**.

It is recommended that the processor compute the result without undue
overflow or underflow.

### **Examples**

Sample program:

```fortran
program demo_norm2
implicit none
integer :: i
real :: x(2,3) = reshape([ &
   1, 2, 3, &
   4, 5, 6  &
   ],shape(x),order=[2,1])

  write(*,*) 'input in row-column order'
  write(*,*) 'x='
  write(*,'(4x,3f4.0)')transpose(x)
  write(*,*)
  write(*,*) 'norm2(x)=',norm2(x)
  write(*,*) 'which is equivalent to'
  write(*,*) 'sqrt(sum(x**2))=',sqrt(sum(x**2))
  write(*,*)
  write(*,*) 'for reference the array squared is'
  write(*,*) 'x**2='
  write(*,'(4x,3f4.0)')transpose(x**2)
  write(*,*)
  write(*,*) 'norm2(x,dim=1)=',norm2(x,dim=1)
  write(*,*) 'norm2(x,dim=2)=',norm2(x,dim=2)
  write(*,*) '(sqrt(sum(x(:,i)**2)),i=1,3)=',(sqrt(sum(x(:,i)**2)),i=1,3)
  write(*,*) '(sqrt(sum(x(i,:)**2)),i=1,2)=',(sqrt(sum(x(i,:)**2)),i=1,2)

end program demo_norm2
```

Results:

```text
 >  input in row-column order
 >  x=
 >       1.  2.  3.
 >       4.  5.  6.
 >
 >  norm2(x)=   9.539392
 >  which is equivalent to
 >  sqrt(sum(x**2))=   9.539392
 >
 >  for reference the array squared is
 >  x**2=
 >       1.  4.  9.
 >      16. 25. 36.
 >
 >  norm2(x,dim=1)=   4.123106       5.385165       6.708204
 >  norm2(x,dim=2)=   3.741657       8.774964
 >  (sqrt(sum(x(:,i)**2)),i=1,3)=   4.123106       5.385165       6.708204
 >  (sqrt(sum(x(i,:)**2)),i=1,2)=   3.741657       8.774964
```

### **Standard**

Fortran 2008

### **See Also**

[**product**(3)](#product),
[**sum**(3)](#sum),
[**hypot**(3)](#hypot)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
