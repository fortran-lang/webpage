# Operations on external files

Once again, this is an overview only.

## File positioning statements

## The `open` statement

The statement is used to connect an external file to a unit, create a
file that is preconnected, or create a file and connect it to a unit.
The syntax is

```f90
open (unit=u, status=st, action=act[, olist])
```

where `olist` is a list of optional specifiers. The specifiers may
appear in any order.

```f90
open (unit=2, iostat=ios, file="cities", status="new", access="direct", &
      action="readwrite", recl=100)
```

Other specifiers are `form` and `position`.

## The `close` statement

This is used to disconnect a file from a unit.

```f90
close (unit=u[, iostat=ios] [, status=st])
```

as in

```f90
close (unit=2, iostat=ios, status="delete")
```

## The `inquire` statement

At any time during the execution of a program it is possible to inquire
about the status and attributes of a file using this statement.

Using a variant of this statement, it is similarly possible to determine
the status of a unit, for instance whether the unit number exists for
that system.

Another variant permits an inquiry about the length of an output list
when used to write an unformatted record.

For inquire by unit

```f90
inquire (unit=u, ilist)
```

or for inquire by file

```f90
inquire (file=fln, ilist)
```

or for inquire by I/O list

```f90
inquire (iolength=length) olist
```

As an example

```f90
logical            :: ex, op
character(len=11)  :: nam, acc, seq, frm
integer            :: irec, nr
inquire (unit=2, exist=ex, opened=op, name=nam, access=acc, sequential=seq, &
         form=frm, recl=irec, nextrec=nr)
```

yields

```f90
ex      .true.
op      .true.
nam      cities
acc      direct
seq      no
frm      unformatted
irec     100
nr       1
```

(assuming no intervening read or write operations).

Other specifiers are
`iostat`, `opened`, `number`, `named`, `formatted`, `position`, `action`,
`read`, `write`, `readwrite`.
