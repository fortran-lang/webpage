(anint)=
## anint

### **Name**

**anint**(3) - \[NUMERIC\] Real nearest whole number

### **Synopsis**

```fortran
    result = anint(a [,kind])
```

```fortran
     elemental real(kind=KIND) function anint(x,KIND)

      real(kind=**),intent(in)   :: x
      integer,intent(in),optional :: KIND
```

### **Characteristics**

- **a** is type _real_ of any kind
- **KIND** is a scalar integer constant expression.
- the result is type _real_. The kind of the result is the same as **x**
  unless specified by **kind**.

### **Description**

**anint**(3) rounds its argument to the nearest whole number.

Unlike **nint**(3) which returns an _integer_ the full range or real
values can be returned (_integer_ types typically have a smaller range
of values than _real_ types).

### **Options**

- **a**
  : the value to round

- **kind**
  : specifies the kind of the result. The default is the kind of **a**.

### **Result**

The return value is the real whole number nearest **a**.

If **a** is greater than zero, **anint(a)**(3) returns **aint(a + 0.5)**.

If **a** is less than or equal to zero then it returns **aint(a - 0.5)**,
except **aint** specifies that for |**a**| < 1 the result is zero (0).

It is processor-dependent whether anint(a) returns negative zero when
-0.5 < a <= -0.0. Compiler switches are often available which enable
or disable support of negative zero.

### **Examples**

Sample program:

```fortran
program demo_anint
use, intrinsic :: iso_fortran_env, only : real32, real64, real128
implicit none
real,allocatable :: arr(:)

  ! basics
   print *, 'ANINT (2.783) has the value 3.0 =>', anint(2.783)
   print *, 'ANINT (-2.783) has the value -3.0 =>', anint(-2.783)

   print *, 'by default the kind of the output is the kind of the input'
   print *, anint(1234567890.1234567890e0)
   print *, anint(1234567890.1234567890d0)

   print *, 'sometimes specifying the result kind is useful when passing'
   print *, 'results as an argument, for example.'
   print *, 'do you know why the results are different?'
   print *, anint(1234567890.1234567890,kind=real64)
   print *, anint(1234567890.1234567890d0,kind=real64)

  ! elemental
   print *, 'numbers on a cusp are always the most troublesome'
   print *, anint([ -2.7, -2.5, -2.2, -2.0, -1.5, -1.0, -0.5, 0.0 ])

   print *, 'negative zero is processor dependent'
   arr=[ 0.0, 0.1, 0.5, 1.0, 1.5, 2.0, 2.2, 2.5, 2.7 ]
   print *, anint(arr)
   arr=[ -0.0, -0.1, -0.5, -1.0, -1.5, -2.0, -2.2, -2.5, -2.7 ]
   print *, anint(arr)

end program demo_anint
```

Results:

```text
 >  ANINT (2.783) has the value 3.0 =>   3.000000
 >  ANINT (-2.783) has the value -3.0 =>  -3.000000
 >  by default the kind of the output is the kind of the input
 >   1.2345679E+09
 >    1234567890.00000
 >  sometimes specifying the result kind is useful when passing
 >  results as an argument, for example.
 >  do you know why the results are different?
 >    1234567936.00000
 >    1234567890.00000
 >  numbers on a cusp are always the most troublesome
 >   -3.000000      -3.000000      -2.000000      -2.000000      -2.000000
 >   -1.000000      -1.000000      0.0000000E+00
 >  negative zero is processor dependent
 >   0.0000000E+00  0.0000000E+00   1.000000       1.000000       2.000000
 >    2.000000       2.000000       3.000000       3.000000
 >   0.0000000E+00  0.0000000E+00  -1.000000      -1.000000      -2.000000
 >   -2.000000      -2.000000      -3.000000      -3.000000
```

### **Standard**

FORTRAN 77

### **See Also**

[**aint**(3)](#aint),
[**int**(3)](#int),
[**nint**(3)](#nint),
[**selected_int_kind**(3)](#selected_int_kind),
[**ceiling**(3)](#ceiling),
[**floor**(3)](#floor)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
