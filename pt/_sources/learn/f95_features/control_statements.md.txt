# Control statements

## Branching and conditions

The simple `go to` *label* exists, but is usually avoided in most cases,
a more specific branching construct will accomplish the same logic with
more clarity.

The simple conditional test is the `if` statement:

```f90
if (a > b) x = y
```

A full-blown `if` construct is illustrated by

```f90
if (i < 0) then
  if (j < 0) then
    x = 0.
  else
    z = 0.
  end if
else if (k < 0) then
  z = 1.
else
  x = 1.
end if
```

## `case` construct

The `case` construct is a replacement for the computed `goto`, but is
better structured and does not require the use of statement labels:

```f90
select case (number)  ! number of type integer
case (:-1)  ! all values below 0
  n_sign = -1
case (0)    ! only 0
  n_sign = 0
case (1:)   ! all values above 0
  n_sign = 1
end select
```

Each `case` selector list may contain a list and/or range of integers,
character or logical constants, whose values may not overlap within or
between selectors:

```f90
case (1, 2, 7, 10:17, 23)
```

A default is available:

```f90
case default
```

There is only one evaluation, and only one match.

## `do` construct

A simplified but sufficient form of the `do` construct is illustrated by

```f90
outer: do
  inner: do i = j, k, l  ! from j to k in steps of l (l is optional)
    :
    if (...) cycle
    :
    if (...) exit outer
    :
  end do inner
end do outer
```

where we note that loops may be optionally named so that any `exit` or
`cycle` statement may specify which loop is meant.

Many, but not all, simple loops can be replaced by array expressions and
assignments, or by new intrinsic functions. For instance

```f90
tot = 0.

do i = m, n
  tot = tot + a(i)
end do
```

becomes simply

```f90
tot = sum(a(m:n))
```
