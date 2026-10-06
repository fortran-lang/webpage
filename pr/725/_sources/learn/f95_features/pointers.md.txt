# Pointers

## Basics

Pointers are variables with the `pointer` attribute; they are not a
distinct data type (and so no 'pointer arithmetic' is possible).

```f90
real, pointer :: var
```

They are conceptually a descriptor listing the attributes of the objects
(targets) that the pointer may point to, and the address, if any, of a
target. They have no associated storage until it is allocated or
otherwise associated (by pointer assignment, see
[Pointers in expressions and assignments](pointers-in-expressions-and-assignments)
below):

```f90
allocate (var)
```

and they are dereferenced automatically, so no special symbol required.
In

```f90
var = var + 2.3
```

the value of the target of var is used and modified. Pointers cannot be
transferred via I/O. The statement

```f90
write *, var
```

writes the value of the target of var and not the pointer descriptor
itself.

A pointer can point to another pointer, and hence to its target, or to a
static object that has the `target` attribute:

```f90
real, pointer :: object
real, target  :: target_obj
var => object  ! pointer assignment
var => target_obj
```

but they are strongly typed:

```f90
integer, pointer :: int_var
var => int_var  ! illegal - types must match
```

and, similarly, for arrays the ranks as well as the type must agree.

A pointer can be a component of a derived type:

```f90
type entry  ! type for sparse matrix
  real    :: value
  integer :: index
  type(entry), pointer :: next  ! note recursion
end type entry
```

and we can define the beginning of a linked chain of such entries:

```f90
type(entry), pointer :: chain
```

After suitable allocations and definitions, the first two entries could
be addressed as

```f90
chain%value           chain%next%value
chain%index           chain%next%index
chain%next            chain%next%next
```

but we would normally define additional pointers to point at, for
instance, the first and current entries in the list.

## Association

A pointer's association status is one of: associated, disassociated (nullified), or undefined. Some care has to be taken not
to leave a pointer 'dangling' by use of `deallocate` on its target
without nullifying any other pointer referring to it.

The intrinsic function `associated` can test the association status of a
defined pointer:

```f90
if (associated(ptr)) then
```

or between a defined pointer and a defined target (which may, itself, be
a pointer):

```f90
if (associated(ptr, target)) then
```

An alternative way to initialize a pointer, also in a specification
statement, is to use the `null` function:

```f90
real, pointer, dimension(:) :: vector => null()  ! compile time
vector => null()                                 ! run time
```

## Pointers in expressions and assignments

For intrinsic types we can 'sweep' pointers over different sets of
target data using the same code without any data movement. Given the
matrix manipulation *y = B C z*, we can write the following code
(although, in this case, the same result could be achieved more simply
by other means):

```f90
real, target  :: b(10, 10), c(10, 10), r(10), s(10), z(10)
real, pointer :: a(:, :), x(:), y(:)
integer       :: mult
:
do mult = 1, 2
  if (mult == 1) then
    y => r          ! no data movement
    a => c
    x => z
  else
    y => s          ! no data movement
    a => b
    x => r
  end if
  y = matmul(a, x)  ! common calculation
end do
```

For objects of derived type we have to distinguish between pointer and
normal assignment. In

```f90
type(entry), pointer :: first, current
:
first => current
```

the assignment causes first to point at current, whereas

```f90
first =  current
```

causes current to overwrite first and is equivalent to

```f90
first%value = current%value
first%index = current%index
first%next => current%next
```

## Pointer arguments

If an actual argument is a pointer then, if the dummy argument is also a
pointer,

- it must have same rank,
- it receives its association status from the actual argument,
- it returns its final association status to the actual argument
  (note: the target may be undefined!),
- it may not have the `intent` attribute (it would be ambiguous),
- it requires an interface block.

If the dummy argument is not a pointer, it becomes associated with the
target of the actual argument:

```f90
real, pointer :: a(:, :)
:
allocate (a(80, 80))
:
call sub(a)
:
subroutine sub(c)
  real c(:, :)
```

## Pointer functions

Function results may also have the `pointer` attribute; this is useful
if the result size depends on calculations performed in the function, as
in

```f90
use data_handler
real          :: x(100)
real, pointer :: y(:)
:
y => compact(x)
```

where the module `data_handler` contains

```f90
function compact(x)
  real, pointer :: compact(:)
  real          :: x(:)
  ! A procedure to remove duplicates from the array x
  integer n
  :  ! Find the number of distinct values, n
  allocate (compact(n))
  :  ! Copy the distinct values into compact
end function compact
```

The result can be used in an expression (but must be associated with a
defined target).

## Arrays of pointers

These do not exist as such: given

```f90
type(entry) :: rows(n)
```

then

```f90
rows%next  ! illegal
```

would be such an object, but with an irregular storage pattern. For this
reason they are not allowed. However, we can achieve the same effect by
defining a derived data type with a pointer as its sole component:

```f90
type row
  real, pointer :: r(:)
end type
```

and then defining arrays of this data type

```f90
type(row) :: s(n), t(n)
```

where the storage for the rows can be allocated by, for instance,

```f90
do i = 1, n
  allocate (t(i)%r(1:i)) ! Allocate row i of length i
end do
```

The array assignment `s = t` is then equivalent to the pointer
assignments

```f90
s(i)%r => t(i)%r
```

for all components.

## Pointers as dynamic aliases

Given an array

```f90
real, target :: table(100, 100)
```

that is frequently referenced with the fixed subscripts

```f90
table(m:n, p:q)
```

these references may be replaced by

```f90
real, dimension(:, :), pointer :: window
   :
window => table(m:n, p:q)
```

The subscripts of window are `1:n - m + 1, 1:q - p + 1`.
Similarly, for `tar%u` (as defined in
[Array elements](array_handling.md#array-elements)
of section Array handling),
we can use, say, `taru => tar%u`
to point at all the u components of tar, and subscript it as
`taru(1, 2)`.
The subscripts are as those of tar itself. (This replaces yet more of
`equivalence`.)

In the pointer association `pointer => array_expression`
the lower bounds for `pointer` are determined as if `lbound` was applied
to `array_expression`. Thus, when a pointer is assigned to a whole array
variable, it inherits the lower bounds of the variable, otherwise, the
lower bounds default to `1`.

[Fortran 2003](https://en.wikipedia.org/wiki/Fortran#Fortran_2003)
allows specifying arbitrary lower bounds on pointer
association, like

```f90
window(r:, s:) => table(m:n, p:q)
```

so that the bounds of `window` become `r:r + n - m, s:s + q - p`.
[Fortran 95](https://en.wikipedia.org/wiki/Fortran_95)
does not have this feature; however, it can be simulated using the
following trick (based on the pointer association rules for assumed
shape array dummy arguments):

```f90
function remap_bounds2(lb1, lb2, array) result(ptr)
  integer, intent(in)                             :: lb1, lb2
  real, dimension(lb1:, lb2:), intent(in), target :: array
  real, dimension(:, :), pointer                  :: ptr
  ptr => array
end function
:
window => remap_bounds2(r, s, table(m:n, p:q))
```

The source code of an extended example of the use of pointers to support
a data structure is in
[pointer.f90](ftp://ftp.numerical.rl.ac.uk/pub/MRandC/pointer.f90).
