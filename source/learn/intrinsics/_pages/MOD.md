(mod)=
## mod

### **Name**

**mod**(3) - \[NUMERIC\] Remainder function

### **Synopsis**

```fortran
    result = mod(a, p)
```

```fortran
     elemental type(TYPE(kind=KIND)) function mod(a,p)

      type(TYPE(kind=KIND),intent(in) :: a
      type(TYPE(kind=KIND),intent(in) :: p
```

### **Characteristics**

- The result and arguments are all of the same type and kind.
- The type may be any kind of _real_ or _integer_.

### **Description**

**mod**(3) computes the remainder of the division of **a** by **p**.

In mathematics, the remainder is the amount "left over" after
performing some computation. In arithmetic, the remainder is the
integer "left over" after dividing one integer by another to produce
an integer quotient (integer division). In algebra of polynomials, the
remainder is the polynomial "left over" after dividing one polynomial
by another. The modulo operation is the operation that produces such
a remainder when given a dividend and divisor.

- (remainder). (2022, October 10). In Wikipedia.
  https://en.wikipedia.org/wiki/Remainder

### **Options**

- **a**
  : The dividend

- **p**
  : the divisor (not equal to zero).

### **Result**

The return value is the result of **a - (int(a/p) \* p)**.

As can be seen by the formula the sign of **p** is canceled out.
Therefore the returned value always has the sign of **a**.

Of course, the magnitude of the result will be less than the magnitude
of **p**, as the result has been reduced by all multiples of **p**.

### **Examples**

Sample program:

```fortran
program demo_mod
implicit none

   ! basics
    print *, mod( -17,  3 ), modulo( -17,  3 )
    print *, mod(  17, -3 ), modulo(  17, -3 )
    print *, mod(  17,  3 ), modulo(  17,  3 )
    print *, mod( -17, -3 ), modulo( -17, -3 )

    print *, mod(-17.5, 5.2), modulo(-17.5, 5.2)
    print *, mod( 17.5,-5.2), modulo( 17.5,-5.2)
    print *, mod( 17.5, 5.2), modulo( 17.5, 5.2)
    print *, mod(-17.5,-5.2), modulo(-17.5,-5.2)

  ! with a divisor of 1 the fractional part is returned
    print *, mod(-17.5, 1.0), modulo(-17.5, 1.0)
    print *, mod( 17.5,-1.0), modulo( 17.5,-1.0)
    print *, mod( 17.5, 1.0), modulo( 17.5, 1.0)
    print *, mod(-17.5,-1.0), modulo(-17.5,-1.0)

end program demo_mod
```

Results:

```text
             -2           1
              2          -1
              2           2
             -2          -2
     -1.900001       3.299999
      1.900001      -3.299999
      1.900001       1.900001
     -1.900001      -1.900001
    -0.5000000      0.5000000
     0.5000000     -0.5000000
     0.5000000      0.5000000
    -0.5000000     -0.5000000
```

### **Standard**

FORTRAN 77

### **See Also**

- [**modulo**(3)](#modulo) - Modulo function
- [**aint**(3)](#aint) - truncate toward zero to a whole _real_ number
- [**int**(3)](#int) - truncate toward zero to a whole _integer_ number
- [**anint**(3)](#anint) - _real_ nearest whole number
- [**nint**(3)](#nint) - _integer_ nearest whole number

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
