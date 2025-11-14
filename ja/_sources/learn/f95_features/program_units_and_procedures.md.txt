# Program units and procedures

## Definitions

In order to discuss this topic we need some definitions. In logical
terms, an executable program consists of one *main program* and zero or
more *subprograms* (or *procedures*) - these do something. Subprograms
are either *functions* or *subroutines*, which are either *external,
internal* or *module* subroutines. (External subroutines are what we
knew from FORTRAN 77.)

From an organizational point of view, however, a complete program
consists of *program units*. These are either *main programs, external
subprograms* or *modules* and can be separately compiled.

An example of a main (and complete) program is

```f90
program test
  print*,'Hello world!'
end program test
```

An example of a main program and an external subprogram, forming an
executable program, is

```f90
program test
  call print_message
end program test

subroutine print_message
  print*,'Hello world!'
end subroutine print_message
```

The form of a function is

```f90
function name(arg1, arg2)  ! zero or more arguments
  :
  name = ...
  :
end function name
```

The form of reference of a function is `x = name(a, b)`.

## Internal procedures

An internal subprogram is one *contained* in another (at a maximum of
one level of nesting) and provides a replacement for the statement
function:

```f90
subroutine outer
  real x, y
  :
contains
  subroutine inner
    real y
    y = x + 1.
    :
  end subroutine inner  ! subroutine mandatory
end subroutine outer
```

We say that `outer` is the *host* of `inner`, and that `inner` obtains
access to entities in `outer` by *host association* (e.g. to `x`),
whereas `y` is a *local* variable to `inner`.

The *scope* of a named entity is a *scoping unit*, here `outer` less
`inner`, and `inner`.

The names of program units and external procedures are *global*, and the
names of implied-DO variables have a scope of the statement that
contains them.

## Modules

Modules are used to package

- global data (replaces `COMMON` and `BLOCK DATA` from FORTRAN 77);
- type definitions (themselves a scoping unit);
- subprograms (which among other things replaces the use of `ENTRY` from
  FORTRAN 77);
- interface blocks (another scoping unit, see
  [Interface blocks](interface-blocks));
- namelist groups (see any textbook).

An example of a module containing a type definition, interface block and
function subprogram is

```f90
module interval_arithmetic
  type interval
    real lower, upper
  end type interval
  interface operator(+)
    module procedure add_intervals
  end interface
  :
contains
  function add_intervals(a, b)
    type(interval), intent(IN) :: a, b
    type(interval) add_intervals
    add_intervals%lower = a%lower + b%lower
    add_intervals%upper = a%upper + b%upper
  end function add_intervals  ! function mandatory
  :
end module interval_arithmetic
```

and the simple statement

```f90

use interval_arithmetic
```

provides *use association* to all the module's entities. Module
subprograms may, in turn, contain internal subprograms.

## Controlling accessibility

The `public` and `private` attributes are used in specifications in
modules to limit the scope of entities. The attribute form is

```f90
real, public     :: x, y, z  ! default
integer, private :: u, v, w
```

and the statement form is

```f90
public  :: x, y, z, operator(.add.)
private :: u, v, w, assignment(=), operator(*)
```

The statement form has to be used to limit access to operators, and can
also be used to change the overall default:

```f90
private  ! sets default for module
public  :: only_this
```

For derived types there are three possibilities: the type and its
components are all `public`, the type is `public` and its components
`private` (the type only is visible and one can change its details
easily), or all of it is `private` (for internal use in the module
only):

```f90
module mine
  private
  type, public :: list
    real x, y
    type(list), pointer :: next
  end type list
  type(list) :: tree
  :
end module mine
```

The `use` statement's purpose is to gain access to entities in a module.
It has options to resolve name clashes if an imported name is the same
as a local one:

```f90
use mine, local_list => list
```

or to restrict the used entities to a specified set:

```f90
use mine, only : list
```

These may be combined:

```f90
use mine, only : local_list => list
```

## Arguments

We may specify the intent of dummy arguments:

```f90
subroutine shuffle(ncards, cards)
  integer, intent(in) :: ncards
  integer, intent(out), dimension(ncards) :: cards
```

Also, `inout` is possible: here the actual argument must be a variable
(unlike the default case where it may be a constant).

Arguments may be optional:

```f90
subroutine mincon(n, f, x, upper, lower, equalities, inequalities, &
  convex, xstart)
  real, optional, dimension :: upper, lower
  :
  if (present(lower)) then  ! test for presence of actual argument
    :
```

allows us to call `mincon` by

```f90
call mincon(n, f, x, upper)
```

Arguments may be keyword rather than positional (which come first):

```f90
call mincon(n, f, x, equalities=0, xstart=x0)
```

Optional and keyword arguments are handled by explicit interfaces, that
is with internal or module procedures or with interface blocks.

## Interface blocks

Any reference to an internal or module subprogram is through an
interface that is 'explicit' (that is, the compiler can see all the
details). A reference to an external (or dummy) procedure is usually
'implicit' (the compiler assumes the details). However, we can provide
an explicit interface in this case too. It is a copy of the header,
specifications and `end` statement of the procedure concerned, either
placed in a module or inserted directly:

```f90
real function minimum(a, b, func)
  ! returns the minimum value of the function func(x)
  ! in the interval (a,b)
  real, intent(in) :: a, b
  interface
    real function func(x)
      real, intent(in) :: x
    end function func
  end interface
  real f, x
  :
  f = func(x)  ! invocation of the user function.
  :
end function minimum
```

An explicit interface is obligatory for

- optional and keyword arguments;
- `pointer` and `target` arguments (see
  [Pointers](pointers.md));
- `pointer` function result;
- new-style array arguments and array functions
  ([Array handling](array_handling.md)).

It allows full checks at compile time between actual and dummy
arguments.

**In general, the best way to ensure that a procedure interface is
explicit is either to place the procedure concerned in a module or to
use it as an internal procedure.**

## Overloading and generic interfaces

Interface blocks provide the mechanism by which we are able to define
generic names for specific procedures:

```f90
interface gamma  ! generic name
  function sgamma(X)  ! specific name
    real(selected_real_kind(6)) sgamma, x
  end
  function dgamma(X)  ! specific name
    real(selected_real_kind(12)) dgamma, x
  end
end interface gamma
```

where a given set of specific names corresponding to a generic name must
all be of functions or all of subroutines. If this interface is within a
module, then it is simply

```f90
interface gamma
  module procedure sgamma, dgamma
end interface
```

We can use existing names, e.g. `sin`, and the compiler sorts out the
correct association.

We have already seen the use of interface blocks for defined operators
and assignment (see
[Modules](modules)).

## Recursion

Indirect recursion is useful for multi-dimensional integration. For

```f90
volume = integrate(fy, ybounds)
```

We might have

```f90
recursive function integrate(f, bounds)
  ! Integrate f(x) from bounds(1) to bounds(2)
  real integrate
  interface
    function f(x)
      real f, x
    end function f
  end interface
  real, dimension(2), intent(in) :: bounds
  :
end function integrate
```

and to integrate `f(x, y)` over a rectangle:

```f90
function fy(y)
  use func  ! module func contains function f
  real fy, y
  yval = y
  fy = integrate(f, xbounds)
end
```

Direct recursion is when a procedure calls itself, as in

```f90
recursive function factorial(n) result(res)
  integer res, n
  if (n .eq. 0) then
    res = 1
  else
    res = n * factorial(n - 1)
  end if
end
```

Here, we note the `result` clause and termination test.

## Pure procedures

This is a feature for parallel computing.

In
[the `forall` statement and construct](array_handling.md#the-forall-statement-and-construct),
any side effects in a function can impede optimization on
a parallel processor the order of execution of the assignments could
affect the results. To control this situation, we add the `pure` keyword
to the `subroutine` or `function` statement an assertion that the
procedure (expressed simply):

- alters no global variable,
- performs no I/O,
- has no saved variables (variables with the `save` attribute that
  retains values between invocations), and
- for functions, does not alter any of its arguments.

A compiler can check that this is the case, as in

```f90
pure function calculate(x)
```

All the intrinsic functions are `pure`.
