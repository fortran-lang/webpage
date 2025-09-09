(reduce)=
## reduce

### **Name**

**reduce**(3) - \[TRANSFORMATIONAL\] General reduction of an array

### **Synopsis**

There are two forms to this function:

```fortran
   result = reduce(array, operation [,mask]  [,identity]  [,ordered] )
```

or

```fortran
   result = reduce (array, operation, dim  &
   & [,mask] [,identity] [,ordered] )
```

```fortran
    type(TYPE(kind=KIND)) function reduce &
    & (array, operation, dim, mask, identity, ordered )

     type(TYPE(kind=KIND)),intent(in) :: array
     pure function                  :: operation
     integer,intent(in),optional    :: dim
     logical,optional               :: mask
     type(TYPE),intent(in),optional :: identity
     logical,intent(in),optional    :: ordered
```

### **Characteristics**

- **array** is an array of any type
- **operation** is a pure function with exactly two arguments
  - each argument is scalar, non-allocatable, a nonpointer,
    nonpolymorphic and nonoptional with the same type and kind as array.
  - if one argument has the asynchronous, target, or value attribute so
    shall the other.
- **dim** is an _integer_ scalar
- **mask** is a logical conformable with **array**
- **identity** is a scalar with the same type and type parameters as **array**
- **ordered** is a logical scalar
- the result is of the same type and type parameters as **array**.

### **Description**

**reduce**(3) reduces a list of conditionally selected values from
an array to a single value by iteratively applying a binary function.

Common in functional programming, a **reduce** function applies a
binary operator (a pure function with two arguments) to all elements
cumulatively.

**reduce** is a "higher-order" function; ie. it is a function that
receives other functions as arguments.

The **reduce** function receives a binary operator (a function with
two arguments, just like the basic arithmetic operators). It is first
applied to two unused values in the list to generate an accumulator
value which is subsequently used as the first argument to the function
as the function is recursively applied to all the remaining selected
values in the input array.

### **Options**

- **array**
  : An array of any type and allowed rank to select values from.

- **operation**
  : shall be a pure function with exactly two arguments;
  each argument shall be a scalar, nonallocatable,
  nonpointer, nonpolymorphic, nonoptional dummy data object
  with the same type and type parameters as **array**. If
  one argument has the ASYNCHRONOUS, TARGET, or VALUE
  attribute, the other shall have that attribute. Its result
  shall be a nonpolymorphic scalar and have the same type
  and type parameters as **array**. **operation** should
  implement a mathematically associative operation. It
  need not be commutative.

  NOTE

  If **operation** is not computationally associative, REDUCE
  without ORDERED=.TRUE. with the same argument values
  might not always produce the same result, as the processor
  can apply the associative law to the evaluation.

  Many operations that mathematically are associative are
  not when applied to floating-point numbers. The order
  you sum values in may affect the result, for example.

- **dim**
  : An integer scalar with a value in the range
  1<= **dim** <= n, where n is the rank of **array**.

- **mask**
  : (optional) shall be of type logical and shall be
  conformable with **array**.

  When present only those elements of **array** are passed
  to **operation** for which the corresponding elements
  of **mask** are true, as if **array\* was filtered with
  **pack(3)\*\*.

- **identity**
  : shall be scalar with the same type and type parameters as **array**.
  If the initial sequence is empty, the result has the value **identify**
  if **identify** is present, and otherwise, error termination is
  initiated.

- **ordered**
  : shall be a logical scalar. If **ordered** is present with the value
  _.true._, the calls to the **operator** function begins with the first
  two elements of **array** and the process continues in row-column
  order until the sequence has only one element which is the value of the
  reduction. Otherwise, the compiler is free to assume that the operation
  is commutative and may evaluate the reduction in the most optimal way.

### **Result**

The result is of the same type and type parameters as **array**. It is
scalar if **dim** does not appear.

If **dim** is present, it indicates the one dimension along which to
perform the reduction, and the resultant array has a rank reduced by
one relative to the input array.

### **Examples**

The following examples all use the function MY_MULT, which returns
the product of its two real arguments.

```fortran
   program demo_reduce
   implicit none
   character(len=*),parameter :: f='("[",*(g0,",",1x),"]")'
   integer,allocatable :: arr(:), b(:,:)

   ! Basic usage:
      ! the product of the elements of an array
      arr=[1, 2, 3, 4 ]
      write(*,*) arr
      write(*,*) 'product=', reduce(arr, my_mult)
      write(*,*) 'sum=', reduce(arr, my_sum)

   ! Examples of masking:
      ! the product of only the positive elements of an array
      arr=[1, -1, 2, -2, 3, -3 ]
      write(*,*)'positive value product=',reduce(arr, my_mult, mask=arr>0)
   ! sum values ignoring negative values
      write(*,*)'sum positive values=',reduce(arr, my_sum, mask=arr>0)

   ! a single-valued array returns the single value as the
   ! calls to the operator stop when only one element remains
      arr=[ 1234 ]
      write(*,*)'single value sum',reduce(arr, my_sum )
      write(*,*)'single value product',reduce(arr, my_mult )

   ! Example of operations along a dimension:
   !  If B is the array   1 3 5
   !                      2 4 6
      b=reshape([1,2,3,4,5,6],[2,3])
      write(*,f) REDUCE(B, MY_MULT),'should be [720]'
      write(*,f) REDUCE(B, MY_MULT, DIM=1),'should be [2,12,30]'
      write(*,f) REDUCE(B, MY_MULT, DIM=2),'should be [15, 48]'

   contains

   pure function my_mult(a,b) result(c)
   integer,intent(in) :: a, b
   integer            :: c
      c=a*b
   end function my_mult

   pure function my_sum(a,b) result(c)
   integer,intent(in) :: a, b
   integer            :: c
      c=a+b
   end function my_sum

   end program demo_reduce
```

Results:

```text
     >  1 2 3 4
     >  product= 24
     >  sum=     10
     >  positive value sum= 6
     >  sum positive values= 6
     >  single value sum     1234
     >  single value product 1234
     > [720, should be [720],
     > [2, 12, 30, should be [2,12,30],
     > [15, 48, should be [15, 48],
```

### **Standard**

Fortran 2018

### **See Also**

- [co_reduce(3)](#co_reduce)

### **Resources**

- [associative:wikipedia](https://en.wikipedia.org/wiki/Associative_property)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
