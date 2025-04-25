(dble)=
## dble

### **Name**

**dble**(3) - \[TYPE:NUMERIC\] Converstion to double precision real

### **Synopsis**

```fortran
    result = dble(a)
```

```fortran
     elemental doubleprecision function dble(a)

      doubleprecision :: dble
      TYPE(kind=KIND),intent(in) :: a
```

### **Characteristics**

- **a** my be _integer_, _real_, _complex_, or a BOZ-literal-constant
- the result is a doubleprecision _real_.

### **Description**

**dble**(3) Converts **a** to double precision _real_ type.

### **Options**

- **a**
  : a value to convert to a doubleprecision _real_.

### **Result**

The return value is of type _doubleprecision_. For _complex_ input,
the returned value has the magnitude and sign of the real component
of the input value.

### **Examples**

Sample program:

```fortran
program demo_dble
implicit none
real:: x = 2.18
integer :: i = 5
complex :: z = (2.3,1.14)
   print *, dble(x), dble(i), dble(z)
end program demo_dble
```

Results:

```text
  2.1800000667572021  5.0000000000000000   2.2999999523162842
```

### **Standard**

FORTRAN 77

### **See also**

- [**aimag**(3)](#aimag) - Imaginary part of complex number
- [**cmplx**(3)](#cmplx) - Convert values to a complex type
- [**int**(3)](#int) - Truncate towards zero and convert to integer
- [**nint**(3)](#nint) - Nearest whole number
- [**out_of_range**(3)](#out_of_range) - Whether a value cannot be converted safely.
- [**real**(3)](#real) - Convert to real type

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
