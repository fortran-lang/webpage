## Data transfer

### Formatted input/output

These examples illustrate various forms of I/O lists with some simple
formats (see
<a href="#Edit_descriptors" class="wikilink" title="below">below</a>):

```f90
INTEGER             :: i
REAL, DIMENSION(10) :: a
CHARACTER(len=20)   :: word
PRINT "(i10)",     i
PRINT "(10f10.3)", a
PRINT "(3f10.3)",  a(1),a(2),a(3)
PRINT "(a10)",     word(5:14)
PRINT "(3f10.3)",  a(1)*a(2)+i, SQRT(a(3:4))
```

Variables, but not expressions, are equally valid in input statements
using the `READ` statement:

```f90
READ "(i10)", i
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
READ "(8f10.5)", p%x, p%y, t%a%x, t%a%y, t%b%x, &
                           t%b%y, t%c%x, t%c%y
```

An object in an I/O list is not permitted to be of a derived type that
has a pointer component at any level of component selection.

Note that a zero-sized array may occur as an item in an I/O list. Such
an item corresponds to no actual data transfer.

The format specification may also be given in the form of a character
expression:

```f90
CHARACTER(len=*), parameter :: form = "(f10.3)"
:
PRINT form, q
```

or as an asterisk this is a type of I/O known as *list-directed* I/O
(see
<a href="#List-directed_I/O" class="wikilink" title="below">below</a>),
in which the format is defined by the computer system:

```f90
PRINT *, "Square-root of q = ", SQRT(q)
```

Input/output operations are used to transfer data between the storage of
an executing program and an external medium, specified by a *unit
number*. However, two I/O statements, `PRINT` and a variant of `READ`,
do not reference any unit number: this is referred to as terminal I/O.
Otherwise the form is:

```f90
READ (UNIT=4,     FMT="(f10.3)") q
READ (UNIT=nunit, FMT="(f10.3)") q
READ (UNIT=4*i+j, FMT="(f10.3)") a
```

where `UNIT=` is optional. The value may be any nonnegative integer
allowed by the system for this purpose (but 0, 5 and 6 often denote the
error, keyboard and terminal, respectively).

An asterisk is a variantagain from the keyboard:

```f90
READ (UNIT=*, FMT="(f10.3)") q
```

A read with a unit specifier allows
<a href="exception_handling" class="wikilink"
title="exception handling">exception handling</a>:

```f90
READ (UNIT=NUNIT, FMT="(3f10.3)", IOSTAT=ios) a,b,c
IF (ios == 0) THEN
!     Successful read - continue execution.
   :
ELSE
!     Error condition - take appropriate action.
   CALL error (ios)
END IF
```

There a second type of formatted output statement, the `WRITE`
statement:

```f90
WRITE (UNIT=nout, FMT="(10f10.3)", IOSTAT=ios) a
```

### Internal files

These allow format conversion between various representations to be
carried out by the program in a storage area defined within the program
itself.

```f90
INTEGER, DIMENSION(30)         :: ival
INTEGER                        :: key
CHARACTER(LEN=30)              :: buffer
CHARACTER(LEN=6), DIMENSION(3), PARAMETER :: form = (/ "(30i1)", "(15i2)","(10i3)" /)
READ (UNIT=*, FMT="(a30,i1)")      buffer, key
READ (UNIT=buffer, FMT=form(key)) ival(1:30/key)
```

If an internal file is a scalar, it has a single record whose length is
that of the scalar.

If it is an array, its elements, in array element order, are treated as
successive records of the file and each has length that of an array
element.

An example using a `WRITE` statement is

```f90
INTEGER           :: day
REAL              :: cash
CHARACTER(LEN=50) :: line
:
!   write into line
WRITE (UNIT=line, FMT="(a, i2, a, f8.2, a)") "Takings for day ", day, " are ", cash, " dollars"
```

that might write

     Takings for day  3 are  4329.15 dollars

### List-directed I/O

An example of a read without a specified format for input is

```f90
INTEGER               :: i
REAL                  :: a
COMPLEX, DIMENSION(2) :: field
LOGICAL               :: flag
CHARACTER(LEN=12)     :: title
CHARACTER(LEN=4)      :: word
:
READ *, i, a, field, flag, title, word
```

If this reads the input record

```f90
10 6.4 (1.0,0.0) (2.0,0.0) t test/
```

(in which blanks are used as separators), then `i`, `a`, `field`,
`flag`, and `title` will acquire the values 10, 6.4, (1.0,0.0) and
(2.0,0.0), `.true.` and `test` respectively, while `word` remains
unchanged.

Quotation marks or apostrophes are required as delimiters for a string
that contains a blank.

### Non-advancing I/O

This is a form of reading and writing without always advancing the file
position to ahead of the next record. Whereas an advancing I/O statement
always repositions the file after the last record accessed, a
non-advancing I/O statement performs no such repositioning and may
therefore leave the file positioned within a record.

```f90
CHARACTER(LEN=3)  :: key
INTEGER           :: u, s, ios
:
READ(UNIT=u, FMT="(a3)", ADVANCE="no", SIZE=s, IOSTAT=ios) key
IF (ios == 0) THEN
   :
ELSE
!    key is not in one record
   key(s+1:) = ""
   :
END IF
```

A non-advancing read might read the first few characters of a record and
a normal read the remainder.

In order to write a prompt to a terminal screen and to read from the
next character position on the screen without an intervening line-feed,
we can write

```f90
WRITE (UNIT=*, FMT="(a)", ADVANCE="no") "enter next prime number:"
READ  (UNIT=*, FMT="(i10)") prime_number
```

Non-advancing I/O is for external files, and is not available for
list-directed I/O.

### Edit descriptors

It is possible to specify that an edit descriptor be repeated a
specified number of times, using a *repeat count*: `10f12.3`

The slash edit descriptor (see
<a href="#Control_edit_descriptors" class="wikilink"
title="below">below</a>) may have a repeat count, and a repeat count can
also apply to a group of edit descriptors, enclosed in parentheses, with
nesting:

```f90
PRINT "(2(2i5,2f8.2))", i(1),i(2),a(1),a(2), i(3),i(4),a(3),a(4)
```

Entire format specifications can be repeated:

```f90
PRINT "(10i8)", (/ (i(j), j=1,200) /)
```

writes 10 integers, each occupying 8 character positions, on each of 20
lines (repeating the format specification advances to the next line).

#### Data edit descriptors

#### Control edit descriptors

*Control edit descriptors setting conditions*: *Control edit descriptors
for immediate processing*:

### Unformatted I/O

This type of I/O should be used only in cases where the records are
generated by a program on one computer, to be read back on the same
computer or another computer using the same internal number
representations:

```f90
OPEN(UNIT=4, FILE='test', FORM='unformatted')
READ(UNIT=4) q
WRITE(UNIT=nout, IOSTAT=ios) a  ! no fmt=
```

### Direct-access files

This form of I/O is also known as random access or indexed I/O. Here,
all the records have the same length, and each record is identified by
an index number. It is possible to write, read, or re-write any
specified record without regard to position.

```f90
INTEGER, PARAMETER :: nunit=2, length=100
REAL, DIMENSION(length)            :: a
REAL, DIMENSION(length+1:2*length) :: b
INTEGER                            :: i, rec_length
:
INQUIRE (IOLENGTH=rec_length) a
OPEN (UNIT=nunit, ACCESS="direct", RECL=rec_length, STATUS="scratch", ACTION="readwrite")
:
!   Write array b to direct-access file in record 14
WRITE (UNIT=nunit, REC=14) b
:
!
!   Read the array back into array a
READ (UNIT=nunit, REC=14) a
:
DO i = 1, length/2
   a(i) = i
END DO
!
!   Replace modified record
WRITE (UNIT=nunit, REC=14) a
```

The file must be an external file and list-directed formatting and
non-advancing I/O are unavailable.


## Operations on external files

Once again, this is an overview only.

### File positioning statements

### The `OPEN` statement

The statement is used to connect an external file to a unit, create a
file that is preconnected, or create a file and connect it to a unit.
The syntax is

```f90
OPEN (UNIT=u, STATUS=st, ACTION=act [,olist])
```

where `olist` is a list of optional specifiers. The specifiers may
appear in any order.

```f90
OPEN (UNIT=2, IOSTAT=ios, FILE="cities", STATUS="new", ACCESS="direct",  &
      ACTION="readwrite", RECL=100)
```

Other specifiers are `FORM` and `POSITION`.

### The `CLOSE` statement

This is used to disconnect a file from a unit.

```f90
CLOSE (UNIT=u [, IOSTAT=ios] [, STATUS=st])
```

as in

```f90
CLOSE (UNIT=2, IOSTAT=ios, STATUS="delete")
```

### The `inquire` statement

At any time during the execution of a program it is possible to inquire
about the status and attributes of a file using this statement.

Using a variant of this statement, it is similarly possible to determine
the status of a unit, for instance whether the unit number exists for
that system.

Another variant permits an inquiry about the length of an output list
when used to write an unformatted record.

For inquire by unit

```f90
INQUIRE (UNIT=u, ilist)
```

or for inquire by file

```f90
INQUIRE (FILE=fln, ilist)
```

or for inquire by I/O list

```f90
INQUIRE (IOLENGTH=length) olist
```

As an example

```f90
LOGICAL            :: ex, op
CHARACTER (LEN=11) :: nam, acc, seq, frm
INTEGER            :: irec, nr
INQUIRE (UNIT=2, EXIST=ex, OPENED=op, NAME=nam, ACCESS=acc, SEQUENTIAL=seq, &
         FORM=frm, RECL=irec, NEXTREC=nr)
```

yields

```f90
ex      .true.
op      .true.
nam      cities
acc      DIRECT
seq      NO
frm      UNFORMATTED
irec     100
nr       1
```

(assuming no intervening read or write operations).

Other specifiers are
`IOSTAT, OPENED, NUMBER, NAMED, FORMATTED, POSITION, ACTION, READ, WRITE, READWRITE`.

```mediawiki
==References==
{{Reflist}}
=== Bibliography ===
{{refbegin}}
* {{Citation |last=Metcalf |first=Michael |title=Whence Fortran? |date=2004-06-17 |work=Fortran 95/2003 Explained |pages=1–8 |url=https://doi.org/10.1093/oso/9780198526926.003.0001 |access-date=2025-02-25 |publisher=Oxford University PressOxford |isbn=978-0-19-852692-6 |last2=Reid |first2=John |last3=Cohen |first3=Malcolm}}
* {{Citation |title=Introduction to Modern Fortran |work=Statistics and Computing |pages=13–53 |url=https://doi.org/10.1007/0-387-28123-1_2 |access-date=2025-02-25 |place=New York |publisher=Springer-Verlag |isbn=0-387-23817-4}}
* {{Cite journal |last=Gehrke |first=Wilhelm |date=1996 |title=Fortran 95 Language Guide |url=https://doi.org/10.1007/978-1-4471-1025-5 |doi=10.1007/978-1-4471-1025-5}}
* {{Citation |last=Chivers |first=Ian |title=Fortran 2000 and Various Fortran Dialects |date=2000 |work=Introducing Fortran 95 |pages=377–388 |url=https://doi.org/10.1007/978-1-4471-0403-2_29 |access-date=2025-02-25 |place=London |publisher=Springer London |isbn=978-1-85233-276-1 |last2=Sleightholme |first2=Jane}}
* {{cite book|title=Fortran 95|author1-first=Martin|author1-last=Counihan|edition=2nd|publisher=CRC Press|year=2006|isbn=9780203978467}}
* {{cite book|title=Computer programming in FORTRAN 90 and 95|author1-first=V.|author1-last=Ramaraman|publisher=PHI Learning Pvt. Ltd.|year=1997|isbn=9788120311817}}
* {{cite book|title=Modern Fortran Explained: Incorporating Fortran 2023|author1-first=Michael|author1-last=Metcalf|author2-first=John|author2-last=Reid|author3-first=Malcolm|author3-last=Cohen|author4-first=Reinhold|author4-last=Bader|edition=6th|publisher=Oxford University Press|year=2024|isbn=9780198876595}}
* {{cite book|title=An Introduction to Fortran 90/95: Syntax and Programming|author1-first=Yogendra Prasad|author1-last=Joshi|publisher=Allied Publishers|isbn=9788177644746}}
{{refend}}
{{Authority control}}

{{DEFAULTSORT:Fortran Language Features}}
[[Category:Fortran|Features]]
```
