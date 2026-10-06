# Object-based programming techniques

## Introduction: Container-like types

The word "Container-like" is not a Fortran term, but used in the context
of this article to designate types with components whose size (or type,
to be discussed later) is not known when the type is declared. For
deferred sizing of array objects, this can be achieved by using either
the `pointer` or the `allocatable` attribute for the component's
specification.

The language features and programming techniques will be shown using two
examples introduced in the following section. The demonstration codes
for this chapter can be found in the `object_based` folder of the
[Github repository](https://github.com/reinh-bader/object_fortran).

## Examples for definitions of container-like types

### Allocatable components

As an example for the type definition of a **value container** (not a
Fortran term) with an `allocatable` component consider

```f90
type :: polynomial
  private
  real, allocatable :: a(:)
end type
```

An object declared to be of this type

```f90
type(polynomial) :: p
```

is suitable for characterization of a polynomial

$p(x) = \sum_{k=0}^{\text{degree}} a_{k} \cdot x^k \quad (x \in \Re)$

once it has been created and subsequently supplied with values of the
coefficients:

```f90
degree = ... ! integer value known at run time only
allocate( p%a(0:degree) )
p%a(0:) = ...
```

### Pointer components

As an example for the type definition of a **reference container** (not
a Fortran term) with a `pointer` component consider

```f90
type :: sorted_list
  private
  type(sortable) :: data
  type(sorted_list), pointer :: next => null()
end type
```

Note that referencing the type itself when declaring a component is
permitted if that component has the `pointer` or `allocatable`
attribute; such types are generally known as **recursive**. They are
used to represent information structures (lists, trees, ...), often with
specific relationships between the individual data entries stored in
each node. In this example, the assumption is that entries of type
`data` in subsequent list items fulfill an ordering condition, based on
the functionality supplied with that type:

```f90
type, public :: sortable
  character(len=:), allocatable :: string
end type

interface operator(<)         ! compare two objects of type sortable
  module procedure less_than  ! implementation not shown here
end interface
```

::::{tip}
Given that Fortran supports arrays, use of simple linked lists is
in most cases inappropriate. The example is presented here as being the
simplest that permits illustrating the language features of
interest.
:::::

An object declared to be

```f90
type(sorted_list) :: my_list
```

is suitable as starting point for building a linked list with node
entries of type `data`. In the simplest case, inserting a data item into
the object is done by executing the following statements:

```f90
type(sortable) :: my_data
:
my_data = ...
my_list%data = my_data  ! only compiles if type definition is accessible in host
```

However, as we shall see below, setting up a complete and valid
`sorted_list` object in a reliable manner needs additional work.

## Constructing objects of container-like type

The semantics of the default structure constructor for container-like
objects needs to account for any additional `pointer` or `allocatable`
attribute specified for type components.

For the first example type from the last section, the executable
statements in

```f90
type(polynomial) :: q, r
:
q = polynomial( [2., 3., 1.] )
r = polynomial( null() )
```

result in an object `q` auto-allocated to the value
`q%a(1:3) == [2., 3., 1.]`, and an object `r` with `r%a` unallocated.

For the second example type from the last section, the executable
statements in

```f90
type(sorted_list) :: sl1
type(sorted_list), target :: sl2
type(sortable) :: d1, d2
:
sl1 = sorted_list( data=d1, next=sl2 )  ! use keyword notation
sl2 = sorted_list( d2, null() )
```

result in an object `sl1` with `sl1%next` pointer associated with `sl2`,
and an object `sl2` with `sl2%next` disassociated; the `data` components
of both objects have values, `d1` and `d2`, respectively. Note that an
argument that matches with a `pointer` component must have either the
`pointer` or the `target` attribute. Also, **keyword notation** can
be used in structure constructors in the same manner as for procedure
arguments.

The default constructor's behaviour has some properties that one needs
to be aware of:

1. If all type components have the `private` attribute i.e., the type
   is **opaque** (not a Fortran term), it can only be used if the type
   declaration is accessed by host association (this is the same as for
   nonallocatable/nonpointer components).
2. Especially for container-like types, its semantics may be
   incompatible with the programmer's intentions for how the objects
   should be used.

Item 2 is illustrated by the above object setups, specifically:

- In the `polynomial` example given above, the lower bound of `q%a` is
  set to 1, contrary to the expectation that it should be 0. One could
  account for this by calculating index offsets in any module procedures
  that process `polynomial` objects, but this makes the code harder to
  understand and maintain. Also, the degree of the polynomial should be
  determined by the last nonzero entry of the coefficient array, but the
  language can of course not be aware of this.
- In the `sorted_list` example given above, the ordering requirement for
  entries in subsequent nodes is not checked, so will usually be not
  fulfilled. Also, if `sl2` goes out of scope before `sl1` does, the
  list structure is torn to bits.

The programmer can enforce appropriate semantics by overloading the
structure constructor. In this case, it is usually a good idea to
declare the types as being opaque.

Overloading the structure constructor is done by

- creating a named interface (i.e., a generic function) with the same
  name as the type of interest;
- creating at least one specific function (a subroutine is not
  permitted), usually returning a scalar result of the type of interest.

For the `polynomial` type the interface block (placed in the
specification section of the module containing the type definition)
might read

```f90
interface polynomial
! overload to assure correct lower bound when creating a polynomial object
  module procedure :: create_polynomial
  ... ! further specifics as needed
end interface
```

and the implementation of `create_polynomial` (in the `contains` part of
the module) might read

```f90
pure type(polynomial) function create_polynomial(a)
  real, intent(in) :: a(0:)
  integer :: degree(1)

  degree = findloc( a /= 0.0, value=.true., back=.true. ) - 1
  allocate( create_polynomial%a(0:degree(1)) )
  create_polynomial%a(0:) = a(0:degree(1))
end function
```

Because its signature matches the default structure constructor's, the
function actually overrides the default constructor, making it generally
unavailable.

For the `sorted_list` type the interface block might read

```f90
interface sorted_list
! the default constructor is unavailable because the type is opaque
! the specific has a different signature than the structure constructor
  module procedure :: create_sorted_list
  ... ! further specifics as needed
end interface
```

with the implementation of `create_sorted_list` as follows:

```f90
pure function create_sorted_list(item_array) result(head)
  type(sortable), intent(in) :: item_array(:)
  type(sorted_list) :: head
  integer :: i

  do i = 1, size(item_array)
    call add_to_sorted_list(head, item_array(i))
    ! handles tedious details of pointer fiddling
  end do
end function
```

The constructor has a signature that differs from that of the default
one, but the latter is unavailable outside the host scope of the type
definition anyway, due to the opacity of `sorted_list`.

## Copying objects of container-like type

Default assignment extends to container-like objects. For objects
declared as

```f90
type(polynomial) :: p, q
type(sorted_list) :: slp, slq

... ! code that defines p, slp
```

and after defining values for prospective right-hand sides, execution of
the statement

```f90
q = p
```

produces the same result as

```f90
if ( allocated(q%a) ) deallocate( q%a )
q%a = p%a  ! performs auto-allocation using the RHS's bounds, then copies the value
```

and execution of the statement

```f90
slq = slp
```

produces the same result as

```f90
slq%data = slp%data
slq%next => slp%next  ! creates a reference between list objects without copying any value
```

The terms **deep copy** and **shallow copy** (neither are Fortran terms)
are sometimes used to describe the above behaviour for `allocatable` and
`pointer` components, respectively. Note that - different from the
default structure constructor - having `private` components does not
affect the use of default assigment. However, the semantics of default
assignment might not be what is needed from the programmer's point of
view.

Specifically, consider the case where the object `slq` above has
previously been set up by invoking the overloaded constructor. The
assignment above would then have the following effects:

1. The list elements of the original `slq`, beginning with `slq%next`,
   would become inaccessible ("orphaned"), effectively causing a memory
   leak;
2. after the assignment statement, `slq%next` references into
   `slp%next`, resulting in aliasing.

To avoid 2., it is possible to [**overload** the assignment
operator](https://en.wikipedia.org/wiki/Fortran_95_language_features#Derived-data_types)
for reference containers to create a deep copy. Note that in the case
where defined unary or binary operations are introduced, the functions
that define these need to create deep copies to create the result
variable anyway, otherwise things simply don't work. The downside of
this is that in code like

```f90
slq = slp // slq
```

-- with the overloaded concatenation operator meaning that the argument
lists are joined -- multiple deep copies need to be done (the
implementation of the module procedure `join_lists` that supplies the
necessary specific for `//` is not shown here; see the source
`code sorted_list.f90` for details). It turns out that some of these
exist only intermediately.

Here an implementation of the specific procedure for the overloaded
assignment of `sorted_list` objects:

```f90
subroutine assign_sorted_list(to, from)
  type(sorted_list), intent(in), target :: from
  type(sorted_list), intent(out), target :: to  ! finalizer is executed on entry,
                                                ! see below for discussion of this.
  type(sorted_list), pointer :: p, q

  p => from; q => to

  deep_copy : do
    if ( associated(p) ) then
      q%data = p%data
    else
      exit deep_copy
    end if
    p => p%next
    if ( associated(p) ) allocate( q%next )
    q => q%next
  end do deep_copy
end subroutine
```

Avoiding 1. is usually done by means of finalizers, to be discussed in
the next section. This is because assignment is not the only possible
cause for orphaning of `pointer`-related memory (or indeed other
resource leaks).

## Finalization and conclusions

To deal with resource leaks that are otherwise not within the
programmer's means to avoid, a type definition can be connected with a
user-defined **final procedure** that is automatically invoked in
certain situations. For the `sorted_list` type, this would look like

```f90
type :: sorted_list
  private
  type(sortable) :: data
  type(sorted_list), pointer :: next => null()
contains
  final :: delete_sorted_list
end type
```

Note that the `final` statement appears after a `contains` statement in
the type definition; this implies that `delete_sorted_list` is not a
regular type component. The module procedure's implementation might then
be as follows:

```f90
pure recursive subroutine delete_sorted_list(list)
  type(sorted_list), intent(inout) :: list

  if ( associated(list%next) ) then
    deallocate( list%next )  ! invokes the finalizer recursively
  end if
end subroutine
```

It must be a subroutine that takes a single argument of the type to be
finalized. Most additional attributes are not permitted for that dummy
argument; for the case of finalizing array arguments it is possible to
have a set of finalizers (all listed in the type definition), each of
which declares the dummy argument with an appropriate rank.

::::{tip}
The `pure` and `recursive` properties specified above reflect the
specific needs for the `sorted_list` type and its associated procedures.
The `recursive` specification is optional (i.e., procedures can be
called recursively by default), but a `non_recursive` specification can
be supplied if the implementation's semantics does not permit correct
behaviour in recursive calls.
::::

The finalizer will be automatically invoked on an object if

1. it appears on the left-hand side of an intrinsic assignment
   statement (before the assignment is performed),
2. on invocation of a procedure call where it is argument associated
   with an `intent(out)` dummy,
3. it is a non-saved variable and program execution ends its scope, or
4. it is deallocated.

Nonpointer nonallocatable function results fall into the third category
above; however, finalization does not apply for the default structure
constructor.

Note that if a finalizer is defined and the constructor is overloaded,
but the assignment operator is _not_, then the assignment statement
`slq = sorted_list(...)` (which then translates into a single function
call to the `create_sorted_list()` function shown earlier) will result
in a mutilated left-hand side, because the finalizer will be executed on
the function that overloads the constructor, resulting in `slq%next`
being disassociated. For this reason, the following guideline applies:

> Recommendation: \
> Finalizers, overloads for the default constructor, and overload of the
> assignment operation should usually be jointly implemented.

See also the article "[Rule of
three](<https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)>)"
for the analogous situation in C++.

## Further language features useful for object-based programming

### Extended semantics for allocatable objects

Scalars can have the `allocatable` attribute:

```f90
character(len=:), allocatable :: my_string
type(sorted_list), allocatable :: my_list
```

Allocation then can be done explicitly; the following examples
illustrate applications of the `allocate` statement that are useful or
even necessary in this context:

```f90
allocate( character(len=13) :: my_string )                  ! typed allocation
allocate( my_list, source=sorted_list(array_of_sortable) )  ! sourced allocation
```

**Typed allocation** is necessary for the string variable, because the
length parameter of a string is part of its type; we will later see that
derived types can also appear in the type specification. **Sourced
allocation** permits the creation of an allocated object that is a clone
of the specified source object or expression.

Alternatively, allocatable objects (be they scalar or arrays) can be
auto-allocated by appearing on the left-hand side of an _intrinsic_
assignment statement:

```f90
my_string = "anything goes"  ! auto-allocated to RHS length before value is transferred
! my_list = sorted_list(array_of_sortable)
! the above statement would fail for an unallocated object, because the assignment
! has been overloaded using a nonallocatable first dummy argument
```

A caveat is that for _overloaded_ assignment, this will usually not
work - either one needs to explicitly allocate the object before
assigning to it, or sourced allocation must be used, which bypasses the
overloaded assignment.

Note that for allocatable objects with deferred-size entries (e.g.,
strings, arrays) a non-conformable left-hand side in an assignment
statement will be deallocated before being allocated to the right length
or shape, respectively.

::::{tip}
The features discussed in this subsection are also useful for
object-oriented programming, with additional semantics applying for the
case of polymorphic objects.
::::

### Implementing move semantics

Sometimes it may be necessary to make use of move instead of copy
semantics i.e., create a copy of an object and then get rid of the
original. The simplest way of doing this is to make use of allocatable
(scalar or array) objects,

```f90
type(sorted_list), allocatable :: my_list, your_list
```

After `your_list` has been set up, the object's content can then be
transferred to `my_list` by using the `move_alloc` intrinsic,

```f90
call move_alloc(your_list, my_list)
```

which will deallocate `my_list` if necessary, before doing the transfer.
After the invocation, `my_list` will have the value formerly stored in
`your_list`, and `your_list` will end up in the deallocated state. Note
that the latter does not involve a regular object deallocation
(effectively, a descriptor for the object is moved), so any existing
finalizer will not be invoked.

### The `block` construct

The above rules on finalization imply that variables declared in the
specification part of the main program are not finalizable, since they
by default have the `save` attribute. One could argue this is not
necessary since all assigned memory is reclaimed when program execution
ends. However, excessive memory consumption or the use of other
resources may cause issues for reliable program execution. To work
around these, the `block` construct can be used:

```f90
program test_sorted_list
  use mod_sortable
  use mod_sorted_list
  implicit none
  :
  work : block
    type(sortable) :: array(items)
    type(sorted_list) :: my_list, ...
    : ! initialize array

    my_list = sorted_list(array)
    :
  end block work  ! finalizer is executed on my_list, ...
  :
end program
```

The construct (as the only one in Fortran) permits declaration of
non-saved variables in its specification part. Their lifetime ends when
program execution reaches the `end block` statement, and they therefore
are finalized at this point, if applicable. Named variables declared
outside the construct are accessible inside it, unless a block-local
declaration with the same name exists.

::::{tip}
Note that the construct's execution flow can be modified by
executing an `exit` statement in its body; this can, for example, be
used for structured error handling and finally permits sending `go to`
to retirement.
::::

### The `associate` construct

With the introduction of deeply nested derived types, code that needs
access to ultimate components can become quite hard to read. An
`associate` block construct that enables the use of auto-typed aliases
can be used. This is illustrated by a procedure that is used to
implement the multiplication of two polynomials:

```f90
pure type(polynomial) function multiply_polynomial(p1, p2)
  type(polynomial), intent(in) :: p1, p2
  integer :: j, l, lmax

  lmax = ubound(p1%a,1) + ubound(p2%a,1)
  allocate( multiply_polynomial%a(0:lmax) )

  associate( a => p1%a, b => p2%a, c => multiply_polynomial%a, &
    jmax => ubound(p1%a,1), kmax => ubound(p2%a,1) )  ! association list
    do l = 0, lmax
      c(l) = 0
      do j = max(0, l-kmax), min(jmax, l)
        c(l) = c(l) + a(j) * b(l-j)
      end do
    end do
  end associate
end function
```

For the duration of execution of the construct, the associate names can
be used to refer to their selectors (i.e., the right-hand sides in the
association list). If the selectors are variables, so are the associate
names (`a`, `b`, `c` in the above example), and can be assigned to. If
the selectors are expressions, so are the associate names (`jmax`,
`kmax` in the above example).

Associated entities that refer to variables inherit the `dimension`,
`codimension`, `target`, `asynchronous` and `volatile` attributes from
their selectors, but no others. An associate name can only refer to an
`optional` dummy argument if the latter is present. Associate names can
also appear in other block constructs (`select type`, `change team`),
which will be discussed where appropriate.

## Performing I/O with objects of container-like type

For objects of container-like type, a data transfer statement

```f90
type(sorted_list) :: my_list
: ! set up my_list
write(*, *) my_list
```

would fail to compile, since the run-time library is incapable of
dealing with the irregular structures that are hiding behind the
innocuous variable. Language features for user-defined derived type I/O
(**UDDTIO**) permit the programmer to control the data transfer in an
appropriate manner. This is achieved by binding an I/O statement on a
derived-type object to a user-defined procedure, for example through a
suitably written named interface:

```f90
interface write(formatted)
  module procedure write_fmt_list
end interface
```

Note that this also applies to data types for which the above
stand-alone statement is permitted, and then overloads the default I/O
mechanism.

Once the binding is properly defined, the above I/O statement is
accepted by the compiler, and its execution causes the user-defined
procedure to be invoked. Therefore it is called the **parent** I/O
statement. The actual data transfer statements that are issued inside
the user-defined procedure are called **child** I/O statements.

The following interface variants are permitted, with the obvious
interpretation:

- `write(formatted)`
- `read(formatted)`
- `write(unformatted)`
- `read(unformatted)`

The self-defined procedure is restricted with respect to its interfaces'
characteristics, which are described in the following:

```f90
subroutine <formatted_io>   (dtv, unit, iotype, v_list, iostat, iomsg)
subroutine <unformatted_io> (dtv, unit,                 iostat, iomsg)
```

The placeholders `<formatted_io>` and `<unformatted_io>` must be replaced by
a specific procedure name referenced in the generic interface.

The dummy arguments' declarations and meaning are:

- `dtv`: Must be declared to be a nonpointer nonallocatable scalar
  of the type in question. If the type is extensible (to be explained
  later), the declaration must be polymorphic (i.e. using `class`),
  otherwise non-polymorphic (using `type`). Its `intent` must be `in`
  for `write(...)`, and "`out`" or "`inout`" for `read(...)`. It
  represents the object on which data transfer statements are to be
  executed.

  ::::{tip}
  Note: For the examples in this chapter, we need to
  use `class`, but the behaviour is as if `type` were used, as long as
  the actual arguments are non-polymorphic and the procedure-based
  interface is used for the invocation.
  ::::

- `unit`: An `integer` scalar with `intent(in)`. Its value is that
  of the unit used for data transfer statements. Use of other unit
  values is not permitted (except, perhaps, `error_unit` for debugging
  purposes).
- `iotype`: A `character(len=*)` string with `intent(in)`. This can
  only appear in procedures for formatted I/O. The following table
  describes how the incoming value relates to the parent I/O transfer
  statement:

| Value                 | Caused by parent I/O statement                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"LISTDIRECTED"`      | `write(unit, fmt=*) my_list`                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `"NAMELIST"`          | `write(unit, nml=my_namelist)` **Note:** Referring to the example, at least one `sorted_list` object must be a member of `my_namelist`.                                                                                                                                                                                                                                                                                                         |
| `"DTsorted_list_fmt"` | `write(unit, fmt='(DT"sorted_list_fmt"(10,2))') my_list` **Note:** `DT` is the "derived type" edit descriptor that is needed in format-driven editing to trigger execution of the UDDTIO routine. The string following the `DT` edit descriptor can be freely chosen (even to be zero length); it is recommended that the UDDTIO procedure pay attention to any possible values supplied in the parent I/O statement if it supports DT editing. |

- `v_list`: A rank-1 assumed-shape `integer` array with `intent(in)`
  . This can only appear in procedures for formatted I/O. The incoming
  value is taken from the final part of the `DT` edit descriptor; in the
  example from the table above it would have the value `[10,2]`. Free
  use can be made of the value for the disposition (formatting,
  controlling) of I/O transfer statements inside the procedure. The
  array's size may be zero; specifically, it will be of size zero for
  the listdirected or namelist cases.
- `iostat`: An `integer` scalar with `intent(out)`. It must be given
  a value consistent with those produced by non-UDTTIO statements in
  case of an error. Successful execution of the I/O must result in a
  zero value. Unsuccessful execution must result in either a positive
  value, or one of the values `iostat_end` or `iostat_eor` from the
  `iso_fortran_env` intrinsic module.
- `iomsg`: A `character(len=*)` string with `intent(inout)`. It must
  be given a value if a non-zero `iostat` is returned.

Additional properties and restrictions for UDDTIO are:

- All data transfers are executed in non-advancing mode. Any `advance=`
  specifier will be ignored;
- asynchronous I/O is not supported;
- Inside the user-defined routine, no file positioning statements are
  permitted.

The following demonstrates a partial implementation of formatted writing
on `sorted_list` objects:

```f90
recursive subroutine write_fmt_list(dtv, unit, iotype, v_list, iostat, iomsg)
  class(sorted_list), intent(in) :: dtv
  integer, intent(in) :: unit, v_list(:)
  character(len=*), intent(in) :: iotype
  integer, intent(out) :: iostat
  character(len=*), intent(inout) :: iomsg
  character(len=2) :: next_component

  if ( associated(dtv%next) ) then
    write(next_component, fmt='("t,")')
  else
    write(next_component, fmt='("f")')
  end if
  select case (iotype)
  case ('listdirected')
    write(unit, fmt=*, delim='quote', iostat=iostat, iomsg=iomsg) &
      dtv%data%string
  case ('namelist')
    write(unit, fmt=*, iostat=iostat, iomsg=iomsg) '"', &
      dtv%data%string, '",', trim(next_component)
  case default
    iostat = 129
    iomsg = 'iotype ' // trim(iotype) // ' not implemented'
    return
  end select
  if ( associated(dtv%next) ) then
    call write_fmt_list(dtv%next, unit, iotype, v_list, iostat, iomsg)
  end if
end subroutine
```

**Notes:**

- The namelist itself is inaccessible from the procedure; it is not
  needed since the procedure only needs to write the list values in a
  suitably formatted way. Termination of the list is indicated by a
  final logical value of `F` in the list entry of the namelist file; the
  termination information must be appropriately processed in the
  corresponding namelist case of the read procedure.
- The example implementation does not support `DT` editing; invoking the
  parent I/O statement from the above table would therefore cause error
  termination unless an `iostat=` argument is added to it.
