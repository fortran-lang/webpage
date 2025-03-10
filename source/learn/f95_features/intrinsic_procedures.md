# Intrinsic procedures

Most of the intrinsic functions have already been mentioned. Here, we
deal only with their general classification and with those that have so
far been omitted. All intrinsic procedures can be used with keyword
arguments:

```f90
call date_and_time(TIME=t)
```

and many have optional arguments.

The intrinsic procedures are grouped into four categories:

1. elemental - work on scalars or arrays, e.g. `abs(a)`;
1. inquiry - independent of value of argument (which may be undefined),
   e.g. `precision(a)`;
1. transformational - array argument with array result of different
   shape, e.g. `reshape(a, b)`;
1. subroutines, e.g. `system_clock`.

The procedures not already introduced are

Bit inquiry

```{csv-table}
`bit_size`, "Number of bits in the model"
```

Bit manipulation

```{csv-table}
`btest`, "Bit testing"
`iand`, "Logical AND"
`ibclr`, "Clear bit"
`ibits`, "Bit extraction"
`ibset`, "Set bit"
`ieor`, "Exclusive OR"
`ior`, "Inclusive OR"
`ishft`, "Logical shift"
`ishftc`, "Circular shift"
`not`, "Logical complement"
```

Transfer function, as in

```f90
integer :: i = transfer('abcd', 0)
```

(replaces part of `equivalence`)

Subroutines

```{csv-table}
`date_and_time`, "Obtain date and/or time"
`mvbits`, "Copies bits"
`random_number`, "Returns pseudorandom numbers"
`random_seed`, "Access to seed"
`system_clock`, "Access to system clock"
`cpu_time`, "Returns processor time in seconds"
```
