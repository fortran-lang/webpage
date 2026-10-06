# Performance and ease of use

## Functions with parameters

### A type definition for invocation of a general function

In scientific applications, a commonly occurring requirement is the need
to evaluate functions that depend on additional parameters, apart from
their real-valued argument. For example, an application might need the
value of spherical Bessel function $x \mapsto j_l(q \, x)$ for
independently specified integer values of $l$ and real values of $q$.
More generally, one can consider a real-valued mapping

$\Re \ni x \mapsto f_\lambda(x) \quad (\lambda \in \Omega)$,

where the parameter value $\lambda$ can be from some arbitrary set. This
section presents a way for handling this programmatically, using the
object-oriented features of Fortran. We start with the outline for a
type definition of sufficient generality:

```f90
type, public :: pfunc_type
  private
  procedure(pfunc), pointer, nopass :: fp => null()
  : ! shown later
  class(*), allocatable :: param
contains
  : ! shown later
end type pfunc_type

abstract interface
  pure real function pfunc(x, param)
    real, intent(in) :: x
    class(*), intent(in), optional :: param
  end function pfunc
end interface
```

It supplies

- a **procedure pointer** component with an abstract interface that
  reflects the above mapping;
- an unlimited polymorphic parameter component, to keep all things in
  one place.

Notionally, one could invoke a properly set up `pfunc_type` object
through

```f90
type(pfunc_type) :: pfunc_obj
real :: x

pfunc_obj = pfunc_type(psin, 2)
! definitions of procedure and data object discussed further below
x = ...

write(*,*) 'function value is ', pfunc_obj%fp(x, pfunc_obj%param)
```

Use of a procedure pointer reflects the fact that each `pfunc_type`
object will want to associate its individual target function; this is
sometimes also referred to as an **object-bound procedure**. The
`nopass` attribute in the type definition is needed because otherwise
(analogous to what we saw for the earlier type-bound procedure
examples), the object through which the invocation is done would be
obliged to appear as a first argument in the abstract interface `pfunc`;
this would constitute an additional imposition on the implementation of
the supplied functions. On the other hand, the invocation needs to
explicitly specify the `param` component, making it a bit unwieldy; the
use of `pfunc_type` objects will be simplified as we go on.

### Performance issues arising from object-oriented programming

Let us look at a target function implementation, in form of a trivial
example $\sin(\lambda x)$:

```f90
pure real function psin(x, param)
  real, intent(in) :: x
  class(*), intent(in), optional :: param
  real :: factor
  factor = 1.
  if ( present(param) ) then
    select type ( param )
     type is (real)
      factor = param
     type is (integer)
      factor = real(param)
    end select
  end if
  psin = sin(factor*x)
end function psin
```

Given that an application is likely to request a large number of
function values, the following effects would ensue once for each
invocation:

- function call overhead, and
- overhead of run-time type resolution.

The resulting performance impact is typical for object-oriented designs
that operate in multitudes on small objects. Making use of an
array-based version of the function

```f90
pure function psin_array(x, param) result(r)
  real, intent(in) :: x(:)
  real :: r(size(x))
  class(*), intent(in), optional :: param
  real :: factor
  factor = 1.
  if ( present(param) ) then
    select type ( param )
     type is (real)
      factor = param
     type is (integer)
      factor = real(param)
    end select
  end if
  r = sin(factor*x)  ! kernel
end function psin_array
```

is desirable, since the overheads specified above only arise _once_, and
the actual calculational code (marked "kernel" in the above box) is
amenable to array-related compiler optimizations (the specifics of which
depend on both hardware architecture and working set size).

### Completing the function type definition

The aim now is to proceed to a framework that permits to use both the
scalar and the array versions in a uniform way, thereby making life for
the clients that use the framework easy, while enabling performance
where it is needed.

The full definition of `pfunc_type`, including its referenced abstract
interfaces, reads

```f90
type, public :: pfunc_type
  private
  procedure(pfunc), pointer, nopass :: fp => null()
  procedure(pfunc_array), pointer, nopass :: fp_array => null()
  class(*), allocatable :: param
contains
  procedure, pass, private, non_overridable :: f_scalar, f_array
  generic :: f => f_scalar, f_array
end type pfunc_type

abstract interface
  pure real function pfunc(x, param)
    real, intent(in) :: x
    class(*), intent(in), optional :: param
  end function pfunc
  pure function pfunc_array(x, param) result(r)
    real, intent(in) :: x(:)
    real :: r(size(x))
    class(*), intent(in), optional :: param
  end function pfunc_array
end interface
```

Because we now have two procedure pointers in the type (only one of
which is used in each given object), it is advantageous to provide a
generic type-bound procedure `f` as a front end for ease of use. The
specifics `f_scalar` and `f_array` for this read

```f90
real function f_scalar(this, x)
  class(pfunc_type), intent(in) :: this
  real, intent(in) :: x

  if ( associated(this%fp) ) then
    f_scalar = this%fp(x, this%param)
  else if ( associated(this%fp_array) ) then
    associate ( f_array => this%fp_array([x], this%param) )
      f_scalar = f_array(1)
    end associate
  else
    error stop 'pfunc_type callback: uninitialized object'
  end if
end function f_scalar
function f_array(this, x) result(r)
  class(pfunc_type), intent(in) :: this
  real, intent(in) :: x(:)
  real :: r(size(x))

  ! note that support for the scalar version is omitted here, since
  ! the procedure call overhead, including type resolution, would
  ! significantly impact performance.
  if ( associated(this%fp_array) ) then
    r = this%fp_array(x, this%param)
  else
    error stop 'pfunc_type callback: uninitialized object'
  end if
end function f_array
```

The only way to invoke one of these (in a use association context) is
via the generic name, since the specific type-bound procedures have the
`private` attribute; note that `pfunc_type` is not designed for being
extended. Disambiguation is by rank of `x`.

The structure constructor for the type is overloaded

```f90
interface pfunc_type
  module procedure create_pfunc_type
  module procedure create_pfunc_type_array
end interface pfunc_type
```

with the following specific functions:

```f90
type(pfunc_type) function create_pfunc_type(fp, param)
  procedure(pfunc) :: fp
  class(*), intent(in), optional :: param
  create_pfunc_type%fp => fp
  if ( present(param) ) then
    allocate(create_pfunc_type%param, source=param)
  end if
end function create_pfunc_type
type(pfunc_type) function create_pfunc_type_array(fp_array, param)
  procedure(pfunc_array) :: fp_array
  class(*), intent(in), optional :: param
  create_pfunc_type_array%fp_array => fp_array
  if ( present(param) ) then
    allocate(create_pfunc_type_array%param, source=param)
  end if
end function create_pfunc_type_array
```

Disambiguation is possible due to the sufficiently different interfaces
of the procedure arguments.[^richardson_comment01]

### Using the function type

With the already-shown implementations for the target functions `psin`
and `psin_array`, using this framework is illustrated by the following:

```f90
type(pfunc_type) :: pfunc_obj
real, parameter :: piby4 = atan(1.0), &
  piby4_arr(4) = [ piby4, 2.*piby4, 3.*piby4, 4.*piby4 ]

pfunc_obj = pfunc_type(psin, 2.)
write(*,*) pfunc_obj%f(piby4)

pfunc_obj = pfunc_type(psin)
write(*,*) pfunc_obj%f(piby4)

pfunc_obj = pfunc_type(psin_array, 2.)
write(*,*) pfunc_obj%f(piby4_arr)
```

Omitting a `param` in a constructor is fine, as long as the target
functions cater for the dummy argument's non-presence.

::::{tip}
The framework's implementation makes use of the fact that an
unallocated actual argument associated with an `optional` dummy argument
is considered not present. Once conditional expressions are implemented
in compilers, the code will be appropriately reworked, since use of this
feature is recommended against.
::::

## Arrays of structures versus structures of arrays

Returning to our earlier example type body, the next idea would be to
simulate the dynamics of a large ensemble of bodies. A procedure

```f90
subroutine propagate(bodies, delta_t, force_field)
  type(body), intent(inout) :: bodies(:)
  real, intent(in) :: delta_t
  type(field_type), intent(in) :: force_field
  :
end subroutine
```

might be supplied that modifies the components of all ensemble members,
for example as follows:

- `%pos` $\longrightarrow$ `%pos + delta_t * %vel`
- `%vel` $\longrightarrow$ `%vel + delta_t * force / %mass`

where `force` results from evaluating `force_field` at the position of
the ensemble member.

## Comments on further language features

### Variations on the passed object

All examples for type-bound procedures given up to now have the property
that the invoking object itself is passed as the first argument to the
bound procedure. However, this default behaviour can be modified by the
programmer

- either declaring the binding with a `pass` attribute that references
  the specific (and of course appropriately declared) procedure argument
  the object of the bound type should be passed to,
- or declaring the binding with a `nopass` attribute, in which case the
  object is not (implicitly) passed to the procedure at all in a TBP
  invocation.

[^richardson_comment01]:
    Brad Richardson
    [comments](https://fortran-lang.discourse.group/t/baders-draft-about-oop-and-fortran-bader-intended-for-wikipedia/8539/3)
    the two functions are _sufficiently different_ only because their results
    differ in rank. This pattern does not necessarily work in the general case,
    i.e. that the procedures are not both functions with different type, kind or
    rank of their results.

    More generally, referring to section 15.4.3.4.5 _Restrictions on generic
    declarations_ of the current Fortran 2023 standard (see for instance
    [draft 23-007r1.pdf](https://j3-fortran.org/doc/year/23/23-007r1.pdf),
    page 316)

    > Two dummy arguments are distinguishable if
    >
    > - one is a procedure and the other is a data object,
    > - they are both data objects or known to be functions, and neither is TKR
    >   compatible with the other,
    >   one has the ALLOCATABLE attribute and the other has the POINTER
    >   attribute and not the INTENT (IN) attribute, or
    > - one is a function with nonzero rank and the other is not known to be
    >   a function.
