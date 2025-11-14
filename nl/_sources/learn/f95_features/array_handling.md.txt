# Array handling

Array handling is included in Fortran for two main reasons:

- the notational convenience it provides, bringing the code closer to
  the underlying mathematical form;
- for the additional optimization opportunities it gives compilers
  (although there are plenty of opportunities for degrading
  optimization too!).

At the same time, major extensions of the functionality in this area
have been added. We have already met whole arrays above
(see corresponding sections in
[Language elements](language_elements.md#arrays)
and
[Expressions and assignments](expressions_and_assignments.md#arrays))
and continue to develop the theme.

## Zero-sized arrays

A zero-sized array is handled by Fortran as a legitimate object, without
special coding by the programmer. Thus, in

```f90
do i = 1, n
  x(i) = b(i) / a(i, i)
  b(i + 1:n) = b(i + 1:n) - a(i + 1:n, i) * x(i)
end do
```

no special code is required for the final iteration where `i = n`. We
note that a zero-sized array is regarded as being defined; however, an
array of shape `(0,2)` is not conformable with one of shape `(0,3)`,
whereas

```f90
x(1:0) = 3
```

is a valid 'do nothing' statement.

## Assumed-shape arrays

These are an extension and replacement for assumed-size arrays. Given an
actual argument like:

```f90
real, dimension(0:10, 0:20) :: a
:
call sub(a)
```

the corresponding dummy argument specification defines only the type and
rank of the array, not its shape. This information has to be made
available by an explicit interface, often using an interface block (see
[Interface blocks](program_units_and_procedures.md#interface-blocks)).
Thus we write just

```f90
subroutine sub(da)
  real, dimension(:, :) :: da
```

and this is as if `da` were dimensioned `(11,21)`. However, we can
specify any lower bound and the array maps accordingly.

```f90
real, dimension(0:, 0:) :: da
```

The shape, not bounds, is passed, where the default lower bound is 1 and
the default upper bound is the corresponding extent.

## Automatic arrays

A partial replacement for the uses to which `equivalence` was put is
provided by this facility, useful for local, temporary arrays, as in

```f90
subroutine swap(a, b)
  real, dimension(:)       :: a, b
  real, dimension(size(a)) :: work
  work = a
  a = b
  b = work
end subroutine swap
```

The actual storage is typically maintained on a stack.

## `allocatable` and `allocate`

Fortran provides dynamic allocation of storage; it relies on a heap
storage mechanism (and replaces another use of `equivalence`). An
example for establishing a work array for a whole program is

```f90
module work_array
  integer n
  real, dimension(:, :, :), allocatable :: work
end module

program main
  use work_array
  read (input, *) n
  allocate (work(n, 2 * n, 3 * n), stat=status)
  :
  deallocate (work)
```

The work array can be propagated through the whole program via a `use`
statement in each program unit. We may specify an explicit lower bound
and allocate several entities in one statement. To free dead storage we
write, for instance,

```f90
deallocate(a, b)
```

Deallocation of arrays is automatic when they go out of scope.

## Elemental operations, assignments and procedures

We have already met whole array assignments and operations:

```f90
real, dimension(10) :: a, b
a = 0.       ! scalar broadcast; elemental assignment
b = sqrt(a)  ! intrinsic function result as array object
```

In the second assignment, an intrinsic function returns an array-valued
result for an array-valued argument. We can write array-valued functions
ourselves (they require an explicit interface):

```f90
program test
  real, dimension(3) :: a = (/1., 2., 3./), &
                        b = (/2., 2., 2./), r
  r = f(a, b)
  print*,r
contains
  function f(c, d)
    real, dimension(:) :: c, d
    real, dimension(size(c)) :: f
    f = c * d  ! (or some more useful function of c and d)
  end function f
end program test
```

Elemental procedures are specified with scalar dummy arguments that may
be called with array actual arguments. In the case of a function, the
shape of the result is the shape of the array arguments.

Most intrinsic functions are elemental and Fortran 95 extends this
feature to non-intrinsic procedures, thus providing the effect of
writing, in Fortran 90, 22 different versions, for ranks 0-0, 0-1, 1-0,
1-1, 0-2, 2-0, 2-2, ... 7-7, and is further an aid to optimization on
parallel processors. An elemental procedure must be pure.

```f90
elemental subroutine swap(a, b)
  real, intent(inout)  :: a, b
  real                 :: work
  work = a
  a = b
  b = work
end subroutine swap
```

The dummy arguments cannot be used in specification expressions (see
[Specification expressions](language_elements.md#specification-expressions)
mentioned earlier in Language elements)
except as arguments to certain intrinsic
functions (`bit_size`, `kind`, `len`, and the numeric inquiry ones (see
[Intrinsic data types](language_elements.md#intrinsic-data-types),
and below).

## `where`

Often, we need to mask an assignment. This we can do using the `where`,
either as a statement:

```f90
where (a /= 0.0) a = 1.0 / a  ! avoid division by 0
```

(note: the test is element-by-element, not on whole array), or as a
construct:

```f90
where (a /= 0.0)
  a = 1.0 / a
  b = a  ! all arrays same shape
end where
```

or

```f90
where (a /= 0.0)
  a = 1.0 / a
elsewhere
  a = huge(a)
end where
```

Further:

- it is permitted to mask not only the `where` statement of the
  `where` construct, but also any `elsewhere` statement that it
  contains;
- a `where` construct may contain any number of masked `elsewhere`
  statements but at most one `elsewhere` statement without a mask, and
  that must be the final one;
- `where` constructs may be nested within one another, just like `forall`
  constructs;
- a `where` assignment statement is permitted to be a defined
  assignment, provided that it is elemental;
- a `where` construct may be named in the same way as other
  constructs.

## The `forall` statement and construct

When a `do` construct is executed, each successive iteration is
performed in order and one after the other is an impediment to optimization
on a parallel processor.

```f90
forall (i=1:n) a(i, i) = x(i)
```

where the individual assignments may be carried out in any order, and
even simultaneously. The `forall` may be considered to be an array
assignment expressed with the help of indices.

```f90
forall (i=1:n, j=1:n, y(i, j) /= 0.) x(j, i) = 1.0 / y(i, j)
```

with masking condition.

The `forall` construct allows several assignment statements to be
executed in order.

```f90
a(2:n - 1, 2:n - 1) = a(2:n - 1, 1:n - 2) + a(2:n - 1, 3:n) + &
                        & a(1:n - 2, 2:n - 1) + a(3:n, 2:n - 1)
b(2:n - 1, 2:n - 1) = a(2:n - 1, 2:n - 1)
```

is equivalent to the array assignments

```f90
forall (i=2:n - 1, j=2:n - 1)
  a(i, j) = a(i, j - 1) + a(i, j + 1) + a(i - 1, j) + a(i + 1, j)
  b(i, j) = a(i, j)
end forall
```

The `forall` version is more readable.

Assignment in a `forall` is like an array assignment: as if all the
expressions were evaluated in any order, held in temporary storage, then
all the assignments performed in any order. The first statement must
fully complete before the second can begin.

A `forall` may be nested, and may include a `where`. Procedures
referenced within a `forall` must be pure.

## Array elements

For a simple case, given

```f90
real, dimension(100, 100) :: a
```

we can reference a single element as, for instance, `a(1, 1)`. For a
derived-data type like

```f90
type fun_del
  real               :: u
  real, dimension(3) :: du
end type fun_del
```

we can declare an array of that type:

```f90
type(fun_del), dimension(10, 20) :: tar
```

A reference like `tar(n, 2)` is an element (a scalar!) of type
`fun_del`, but `tar(n, 2)%du` is an array of type `real`, and
`tar(n, 2)%du(2)` is an element of it.  The basic rule to remember
is that an array element always has a subscript or subscripts
qualifying at least the last name.

## Array subobjects (sections)

The general form of subscript for an array section is
`[lower]:[upper][:stride]`
(where `[...]` indicates an optional item) as in

```f90
real a(10, 10)
a(i, 1:n)                ! part of one row
a(1:m, j)                ! part of one column
a(i, :)                  ! whole row
a(i, 1:n:3)              ! every third element of row
a(i, 10:1:-1)            ! row in reverse order
a( (/ 1, 7, 3, 2 /), 1)  ! vector subscript
a(1, 2:11:2)             ! 11 is legal as not referenced
a(:, 1:7)                ! rank two section
```

Note that a vector subscript with duplicate values cannot appear on the
left-hand side of an assignment as it would be ambiguous. Thus,

```f90
b( (/ 1, 7, 3, 7 /) ) = (/ 1, 2, 3, 4 /)
```

is illegal. Also, a section with a vector subscript must not be supplied
as an actual argument to an `out` or `inout` dummy argument. Arrays of
arrays are not allowed:

```f90
tar%du  ! illegal
```

We note that a given value in an array can be referenced both as an
element and as a section:

```f90
a(1, 1)    !  scalar (rank zero)
a(1:1, 1)  !  array section (rank one)
```

depending on the circumstances or requirements. By qualifying objects of
derived type, we obtain elements or sections depending on the rule
stated earlier:

```f90
tar%u        !  array section (structure component)
tar(1, 1)%u  !  component of an array element
```

## Arrays intrinsic functions

### Vector and matrix multiply

```{csv-table}
`dot_product`, "Dot product of 2 rank-one arrays"
`matmul`, "Matrix multiplication"
```

### Array reduction

```{csv-table}
`all`, "True if all values are true"
`any`, "True if any value is true. Example: `if (any( a > b)) then`"
`count`, "Number of true elements in array"
`maxval`, "Maximum value in an array"
`minval`, "Minimum value in an array"
`product`, "Product of array elements"
`sum`, "Sum of array elements"
```

### Array inquiry

```{csv-table}
`allocated`, "Array allocation status"
`lbound`, "Lower dimension bounds of an array"
`shape`, "Shape of an array (or scalar)"
`size`, "Total number of elements in an array"
`ubound`, "Upper dimension bounds of an array"
```

### Array construction

```{csv-table}
`merge`, "Merge under mask"
`pack`, "Pack an array into an array of rank one under a mask"
`spread`, "Replicate array by adding a dimension"
`unpack`, "Unpack an array of rank one into an array under mask"
```

### Array reshape

```{csv-table}
`reshape`, "Reshape an array"
```

### Array manipulation

```{csv-table}
`cshift`, "Circular shift"
`eoshift`, "End-off shift"
`transpose`, "Transpose of an array of rank two"
```

### Array location

```{csv-table}
`maxloc`, "Location of first maximum value in an array"
`minloc`, "Location of first minimum value in an array"
```
