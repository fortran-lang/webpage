# Data transfer

## Formatted input/output

These examples illustrate various forms of I/O lists with some simple
formats (see
[Edit descriptors](edit_descriptors)
below):

```f90
integer             :: i
real, dimension(10) :: a
character(len=20)   :: word
print "(i10)", i
print "(10f10.3)", a
print "(3f10.3)", a(1), a(2), a(3)
print "(a10)", word(5:14)
print "(3f10.3)", a(1) * a(2) + i, sqrt(a(3:4))
```

Variables, but not expressions, are equally valid in input statements
using the `read` statement:

```f90
read "(i10)", i
```

If an array appears as an item, it is treated as if the elements were
specified in array element order.

Any pointers in an I/O list must be associated with a target, and
transfer takes place between the file and the targets.

An item of derived type is treated as if the components were specified
in the same order as in the type declaration, so

```f90
read "(8f10.5)", p, t  ! types point and triangle
```

has the same effect as the statement

```f90
read "(8f10.5)", p%x, p%y, t%a%x, t%a%y, t%b%x, &
                           t%b%y, t%c%x, t%c%y
```

An object in an I/O list is not permitted to be of a derived type that
has a pointer component at any level of component selection.

Note that a zero-sized array may occur as an item in an I/O list. Such
an item corresponds to no actual data transfer.

The format specification may also be given in the form of a character
expression:

```f90
character(len=*), parameter :: form = "(f10.3)"
:
print form, q
```

or as an asterisk this is a type of I/O known as *list-directed* I/O
(see
[below](list-directed-i-o)),
in which the format is defined by the computer system:

```f90
print *, "Square-root of q = ", sqrt(q)
```

Input/output operations are used to transfer data between the storage of
an executing program and an external medium, specified by a *unit
number*. However, two I/O statements, `print` and a variant of `read`,
do not reference any unit number: this is referred to as terminal I/O.
Otherwise the form is:

```f90
read (unit=4, fmt="(f10.3)") q
read (unit=newunit, fmt="(f10.3)") q
read (unit=4 * i + j, fmt="(f10.3)") a
```

where `unit=` is optional. The value may be any nonnegative integer
allowed by the system for this purpose (but `0`, `5` and `6` often
denote the error, keyboard and terminal, respectively).

An asterisk is a variant again from the keyboard:

```f90
read (unit=*, fmt="(f10.3)") q
```

A read with a unit specifier allows
[exception handling](https://en.wikipedia.org/wiki/Exception_handling):

```f90
read (unit=nunit, fmt="(3f10.3)", iostat=ios) a, b, c
if (ios == 0) then
  ! Successful read - continue execution.
  :
else
  ! Error condition - take appropriate action.
  call error(ios)
end if
```

There is a second type of formatted output statement, the `write`
statement:

```f90
write (unit=nout, fmt="(10f10.3)", iostat=ios) a
```

## Internal files

These allow format conversion between various representations to be
carried out by the program in a storage area defined within the program
itself.

```f90
integer, dimension(30)         :: ival
integer                        :: key
character(len=30)              :: buffer
character(len=6), dimension(3), parameter :: form = (/"(30i1)", &
                                                    "(15i2)", "(10i3)"/)

read (unit=*, fmt="(a30,i1)") buffer, key
read (unit=buffer, fmt=form(key)) ival(1:30 / key)
```

If an internal file is a scalar, it has a single record whose length is
that of the scalar.

If it is an array, its elements, in array element order, are treated as
successive records of the file and each has length that of an array
element.

An example using a `write` statement is

```f90
integer           :: day
real              :: cash
character(len=50) :: line
:
! write into line
write (unit=line, fmt="(a, i2, a, f8.2, a)") "Takings for day ", day, &
  " are ", cash, " dollars"
```

that might write

```shell
Takings for day  3 are  4329.15 dollars
```

## List-directed I/O

An example of a read without a specified format for input is

```f90
integer               :: i
real                  :: a
complex, dimension(2) :: field
logical               :: flag
character(len=12)     :: title
character(len=4)      :: word
:
read *,i, a, field, flag, title, word
```

If this reads the input record

```f90
10 6.4(1.0, 0.0) (2.0, 0.0) t test /
```

(in which blanks are used as separators), then `i`, `a`, `field`,
`flag`, and `title` will acquire the values 10, 6.4, (1.0,0.0) and
(2.0,0.0), `.true.` and `test` respectively, while `word` remains
unchanged.

Quotation marks or apostrophes are required as delimiters for a string
that contains a blank.

## Non-advancing I/O

This is a form of reading and writing without always advancing the file
position to ahead of the next record. Whereas an advancing I/O statement
always repositions the file after the last record accessed, a
non-advancing I/O statement performs no such repositioning and may
therefore leave the file positioned within a record.

```f90
character(len=3)  :: key
integer           :: u, s, ios
:
read (unit=u, fmt="(a3)", advance="no", size=s, iostat=ios) key
if (ios == 0) then
  :
else
  ! key is not in one record
  key(s + 1:) = ""
  :
end if
```

A non-advancing read might read the first few characters of a record and
a normal read the remainder.

In order to write a prompt to a terminal screen and to read from the
next character position on the screen without an intervening line-feed,
we can write

```f90
write (unit=*, fmt="(a)", advance="no") "enter next prime number:"
read (unit=*, fmt="(i10)") prime_number
```

Non-advancing I/O is for external files, and is not available for
list-directed I/O.

## Edit descriptors

It is possible to specify that an edit descriptor be repeated a
specified number of times, using a *repeat count*: `10f12.3`

The slash edit descriptor (see
[Control edit descriptors](control-edit-descriptors)
below) may have a great count, and
a repeat count can also apply to a group of edit descriptors,
enclosed in parentheses, with nesting:

```f90
print "(2(2i5,2f8.2))", i(1),i(2),a(1),a(2), i(3),i(4),a(3),a(4)
```

Entire format specifications can be repeated:

```f90
print "(10i8)", (/ (i(j), j=1,200) /)
```

writes 10 integers, each occupying 8 character positions, on each of 20
lines (repeating the format specification advances to the next line).

### Data edit descriptors

### Control edit descriptors

*Control edit descriptors setting conditions*: *Control edit descriptors
for immediate processing*:

## Unformatted I/O

This type of I/O should be used only in cases where the records are
generated by a program on one computer, to be read back on the same
computer or another computer using the same internal number
representations:

```f90
open (unit=4, file='test', form='unformatted')
read (unit=4) q
write (unit=nout, iostat=ios) a  ! no fmt=
```

## Direct-access files

This form of I/O is also known as random access or indexed I/O. Here,
all the records have the same length, and each record is identified by
an index number. It is possible to write, read, or re-write any
specified record without regard to position.

```f90
integer, parameter :: nunit = 2, length = 100
real, dimension(length)              :: a
real, dimension(length + 1:2*length) :: b
integer                              :: i, rec_length
:
inquire (iolength=rec_length) a
open (unit=nunit, access="direct", recl=rec_length, status="scratch", &
      action="readwrite")
:
! Write array b to direct-access file in record 14
write (unit=nunit, rec=14) b
:
! Read the array back into array a
read (unit=nunit, rec=14) a

do i = 1, length / 2
  a(i) = i
end do

! Replace modified record
write (unit=nunit, rec=14) a
```

The file must be an external file and list-directed formatting and
non-advancing I/O are unavailable.
