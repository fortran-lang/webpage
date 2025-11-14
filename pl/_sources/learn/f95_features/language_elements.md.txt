# Language elements

Fortran is
[case-insensitive](https://en.wikipedia.org/wiki/Case_sensitivity)
The convention of writing
Fortran keywords in upper case and all other names in lower case is
adopted in this article; except, by way of contrast, in the input/output
descriptions
([Data transfer](data_transfer)
and
[Operations on external files](operations_on_external_files)).

## Basics

The basic component of the Fortran language is its *character set*. Its
members are

- the letters A ... Z and a ... z (which are equivalent outside a
  character context)
- the numerals 0 ... 9
- the underscore \_
- the special characters
  `= : + blank - * / ( ) [ ] , . $ ' ! " % & ; < > ?`

[Tokens](https://en.wikipedia.org/wiki/Token_(parser))
that
have a syntactic meaning to the compiler are built from those
components. There are six classes of tokens:

```{csv-table}
Label, "`123`"
Constant, "`123.456789_long`"
Keyword, "`allocatable`"
Operator, "`.add.`"
Name, "`solve_equation` (up to 31 characters, including \_)"
Separator, "`/ ( ) (/ /) [ ] , = => : :: ; %`"
```

From the tokens,
[statements](https://en.wikipedia.org/wiki/Statement_(programming))
are built. These can be coded using the
new free *source form* which does not require positioning in a rigid
column structure:

```f90
function string_concat(s1, s2)  ! This is a comment
  type(string), intent(in) :: s1, s2
  type(string)             :: string_concat
  string_concat%string_data = s1%string_data(1:s1%length) // &
    s2%string_data(1:s2%length)  ! This is a continuation
  string_concat%length = s1%length + s2%length
end function string_concat
```

Note the trailing comments and the trailing continuation mark. There may
be 39 continuation lines, and 132 characters per line. Blanks are
significant. Where a token or character constant is split across two
lines:

```f90
               ...        start_of&
        &_name
               ...   'a very long &
        &string'
```

a leading `&` on the continued line is also required.

## Intrinsic data types

Fortran has five *intrinsic data types*: `integer`, `real`, `complex`,
`logical` and `character`. Each of those types can be additionally
characterized by a *kind*. Kind, basically, defines internal
representation of the type: for the three numeric types, it defines the
precision and range, and for the other two, the specifics of storage
representation. Thus, it is an abstract concept which models the limits
of data types' representation; it is expressed as a member of a set of
whole numbers (e.g. it may be {1, 2, 4, 8} for integers, denoting bytes
of storage), but those values are not specified by the Standard and not
portable. For every type, there is a *default kind*, which is used if no
kind is explicitly specified. For each intrinsic type, there is a
corresponding form of *literal constant*. The numeric types `integer`
and `real` can only be signed (there is no concept of sign for type
`complex`).

### Literal constants and kinds

#### `integer`

Integer literal constants of the default kind take the form

```f90
1   0   -999   32767   +10
```

`kind` can be defined as a named constant. If the desired range is
±10<sup>kind</sup>, the portable syntax for defining the appropriate
kind, `two_bytes` is

```f90
integer, parameter :: two_bytes = selected_int_kind(4)
```

that allows subsequent definition of constants of the form

```f90
-1234_two_bytes   +1_two_bytes
```

Here, `two_bytes` is the kind type parameter; it can also be an explicit
default integer literal constant, like `-1234_2` but such use is
non-portable.

The `kind` function supplies the value of a kind type parameter:

```f90
kind(1)            kind(1_two_bytes)
```

and the `range` function supplies the actual decimal range (so the user
must make the actual mapping to bytes):

```f90
range(1_two_bytes)
```

Also, in
[`data` (initialization) statements](data-statement),
binary (`B`), octal (`O`) and hexadecimal (`Z`) constants
may be used (often informally referred to as "BOZ constants"):

```f90
B'01010101'   O'01234567'   Z'10fa'
```

#### `real`

There are at least two real kinds - the default and one with greater
precision (this replaces `double precision`).  `selected_real_kind`
functions returns the kind number for desired range and precision; for
at least 9 decimal digits of precision and a range of 10<sup>−99</sup>
to 10<sup>99</sup>, it can be specified as:

```f90
integer, parameter :: long = selected_real_kind(9, 99)
```

and literals subsequently specified as `1.7_long`.

Also, there are the intrinsic functions

```f90
kind(1.7_long)   precision(1.7_long)   range(1.7_long)
```

that give in turn the kind type value, the actual precision (here at
least `9`), and the actual range (here at least `99`).

#### `complex`

`complex` data type is built of two integer or real components:

```f90
(1, 3.7_long)
```

#### `logical`

There are only two basic values of logical constants: `.true.` and
`.false.`. Here, there may also be different kinds. Logicals don't have
their own kind inquiry functions, but use the kinds specified for
`integer`s; default kind of `logical` is the same as of `integer`.

```f90
.false.   .true._one_byte
```

and the `kind` function operates as expected:

```f90
kind(.true.)
```

#### `character`

The forms of literal constants for `character` data type are

```f90
'A string'   "Another"   'A "quote"'   '''''''
```

(the last being an empty string). Different kinds are allowed (for
example, to distinguish
[ASCII](https://en.wikipedia.org/wiki/ASCII)
and
[UNICODE](https://en.wikipedia.org/wiki/UNICODE)
strings),
but not widely supported by compilers. Again, the kind value is given by
the `kind` function:

```f90
kind('ASCII')
```

### Number model and intrinsic functions

The numeric types are based on number models with associated inquiry
functions (whose values are independent of the values of their
arguments; arguments are used only to provide kind). These functions are
important for portable numerical software:

```{csv-table}
`digits(x)`, "Number of significant digits"
`epsilon(x)`, "Almost negligible compared to one (real)"
`huge(x)`, "Largest number"
`maxexponent(x)`, "Maximum model exponent (real)"
`minexponent(x)`, "Minimum model exponent (real)"
`precision(x)`, "Decimal precision (real, complex)"
`radix(x)`, "Base of the model"
`range(x)`, "Decimal exponent range"
`tiny(x)`, "Smallest positive number (real)"
```

## Scalar variables

Scalar
[variables](https://en.wikipedia.org/wiki/Variable_(programming))
corresponding to the five intrinsic
types are specified as follows:

```f90
integer(kind=2)   :: i
real(kind=long)   :: a
complex           :: current
logical           :: Pravda
character(len=20) :: word
character(len=2, kind=Kanji) :: kanji_word
```

where the optional `kind` parameter specifies a non-default kind, and
the `::` notation delimits the type and attributes from variable name(s)
and their optional initial values, allowing full variable specification
and initialization to be typed in one statement (in previous standards,
attributes and initializers had to be declared in several statements).
While it is not required in above examples (as there are no additional
attributes and initialization), most Fortran-90 programmers acquire the
habit to use it everywhere.

The `len=` specifier is applicable only to `character`s and specifies
the string length (replacing the older `*len` form). The explicit
`kind=` and `len=` specifiers are optional:

```f90
character(2, kanji) :: kanji_word
```

works just as well.

There are some other interesting character features. Just as a substring
as in

```f90
character(80) :: line
... = line(i:i)  ! substring
```

was previously possible, so now is the substring

```f90
'0123456789'(i:i)
```

Also, zero-length strings are allowed:

```f90
line(i:i-1)  ! zero-length string
```

Finally, there is a set of intrinsic character functions, examples being

```{csv-table}
`achar`, "`iachar` (for ASCII set)"
`adjustl`, "`adjustr`"
`len_trim`, "`index(s1, s2, back=.true.)`"
`repeat`, "`scan`(for one of a set)"
`trim`, "`verify`(for all of a set)"
```

## Derived data types

For derived data types, the form of the type must be defined first:

```f90
type person
  character(10) :: name
  real          :: age
end type person
```

and then, variables of that type can be defined:

```f90
type(person) :: you, me
```

To select components of a derived type, `%` qualifier is used:

```f90
you%age
```

Literal constants of derived types have the form
`TypeName(1stComponentLiteral, 2ndComponentLiteral, ...)`:

```f90
you = person("Smith", 23.5)
```

which is known as a *structure constructor*. Definitions may refer to a
previously defined type:

```f90
type point
  real :: x, y
end type point

type triangle
  type(point) :: a, b, c
end type triangle
```

and for a variable of `type triangle`, as in

```f90
type(triangle) :: t
```

each component of type `point` is accessed as

```f90
t%a   t%b   t%c
```

which, in turn, have ultimate components of `type real`:

```f90
t%a%x   t%a%y   t%b%x   t%b%y   t%c%x   t%c%y 
```

etc. (Note that the `%` qualifier was chosen rather than dot (`.`)
because of potential ambiguity with operator notation, like `.OR.`).

## Implicit and explicit typing

Unless specified otherwise, all variables starting with letters `i`,
`j`, `k`, `l`, `m` and `n` default to `integer`, and all others are
default `real`;
other data types must be explicitly declared. This is known as *implicit
typing* and is a heritage of early FORTRAN days. Those defaults can be
overridden by `implicit TypeName (CharacterRange)` statements, like:

```f90
implicit complex(z)
implicit character(a-b)
implicit real(c-h,n-y)
```

However, it is a good practice to explicitly type all variables, and
this can be forced by inserting the statement `implicit none` at the
beginning of each program unit.

## Arrays

Arrays are considered to be variables in their own right. Every array is
characterized by its
[type](https://en.wikipedia.org/wiki/Type_(computer_programming)),
[rank](https://en.wikipedia.org/wiki/Rank_(computer_programming)),
and *shape* (which defines the extents of each
dimension). Bounds of each dimension are by default `1` and *size*, but
arbitrary bounds can be explicitly specified. The `dimension` keyword is
optional and considered an attribute; if omitted, the array shape must
be specified after array-variable name. For example,

```f90
real :: a(10)
integer, dimension(0:100, -50:50) :: map
```

declares two arrays, `rank-1` and `rank-2`, whose elements are in
[column-major order](https://en.wikipedia.org/wiki/Column-major_order).
Elements are, for example,

```f90
a(1)  a(i*j)
```

and are scalars. The subscripts may be any scalar integer expression.

*Sections* are parts of the array variables, and are arrays themselves:

```f90
a(i:j)           ! rank one
map(i:j, k:l:m)  ! rank two
a(map(i, k:l))   ! vector subscript
a(3:2)           ! zero length
```

Whole arrays and array sections are array-valued objects. Array-valued
constants (constructors) are available, enclosed in `(/ ... /)`:

```f90
(/ 1, 2, 3, 4 /)
(/ ( (/ 1, 2, 3 /), i = 1, 4) /)
(/ (i, i = 1, 9, 2) /)
(/ (0, i = 1, 100) /)
(/ (0.1*i, i = 1, 10) /)
```

making use of an implied-`do loop` notation. Fortran 2003 allows the use
of brackets: `[1, 2, 3, 4]` and `[([1,2,3], i=1,4)]` instead of the
first two examples above, and many compilers support this now. A derived
data type may, of course, contain array components:

```f90
type triplet
  real, dimension(3) :: vertex
end type triplet
type(triplet), dimension(4) :: t
```

so that

- `t(2)` is a scalar (a structure)
- `t(2)%vertex` is an array component of a scalar

## Data initialization

Variables can be given initial values as specified in a specification
statement:

```f90
real, dimension(3) :: a = (/ 0.1, 0.2, 0.3 /)
```

and a default initial value can be given to the component of a derived
data type:

```f90
type triplet
  real, dimension(3) :: vertex = 0.0
end type triplet
```

When local variables are initialized within a procedure they implicitly
acquire the `save` attribute:

```f90
real, dimension(3) :: point = (/0.0, 1.0, -1.0/)
```

This declaration is equivalent to

```f90
real, dimension(3), save :: point = (/0.0, 1.0, -1.0/)
```

for local variables within a subroutine or function. The `save`
attribute causes local variables to retain their value after a procedure
call and then to initialize the variable to the saved value upon
returning to the procedure.

### `parameter` attribute

A named constant can be specified directly by adding the `parameter`
attribute and the constant values to a type statement:

```f90
real, dimension(3), parameter :: field = (/0., 1., 2./)
type(triplet), parameter      :: t = triplet((/0., 0., 0./))
```

### `data` statement

The `data` statement can be used for scalars and also for arrays and
variables of derived type. It is also the only way to initialise just
parts of such objects, as well as to initialise to binary, octal or
hexadecimal values:

```f90
type(triplet) :: t1, t2
data t1/triplet((/0., 1., 2./))/, t2%vertex(1)/123./
data array(1:64)/64*0/
data i, j, k/B'01010101', O'77', Z'ff'/
```

### Initialization expressions

The values used in `data` and `parameter` statements, or with these
attributes, are constant expressions that may include references to:
array and structure constructors, elemental intrinsic functions with
integer or character arguments and results, and the six transformational
functions `repeat`, `selected_int_kind`, `trim`, `selected_real_kind`,
`reshape`, and `transfer` (see
[Intrinsic procedures](intrinsic_procedures)):

```f90
integer, parameter :: long = selected_real_kind(12), &
                        array(3) = (/1, 2, 3/)
```

## Specification expressions

It is possible to specify details of variables using any non-constant,
scalar, integer expression that may also include inquiry function
references:

```f90
subroutine s(b, m, c)
  use mod  ! contains a
  real, dimension(:, :)             :: b
  real, dimension(ubound(b, 1) + 5) :: x
  integer                           :: m
  character(len=*)                  :: c
  character(len=m + len(c))         :: cc
  real(selected_real_kind(2*precision(a))) :: z
end subroutine
```
