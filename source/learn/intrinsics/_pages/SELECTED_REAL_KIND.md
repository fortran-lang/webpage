(selected_real_kind)=
## selected_real_kind

### **Name**

**selected_real_kind**(3) - \[KIND\] Choose real kind

### **Synopsis**

```fortran
    result = selected_real_kind([p] [,r] [,radix] )
```

```fortran
    integer function selected_int_kind(r)

     real(kind=KIND),intent(in),optional :: p
     real(kind=KIND),intent(in),optional :: r
     real(kind=KIND),intent(in),optional :: radix
```

### **Characteristics**

- **p** is an _integer_ scalar
- **r** is an _integer_ scalar
- **radix** is an _integer_ scalar
- the result is an default _integer_ scalar

### **Description**

**selected_real_kind**(3) return the kind value of a _real_ data type with
decimal precision of at least **p** digits, exponent range of at least
**r**, and with a radix of **radix**. That is, if such a kind exists

    + it has the decimal precision as returned by **precision**(3) of at
      least **p** digits.
    + a decimal exponent range, as returned by the function **range**(3)
      of at least **r**
    + a radix, as returned by the function **radix**(3) , of **radix**,

If the requested kind does not exist, -1 is returned.

At least one argument shall be present.

### **Options**

- **p**
  : the requested precision

- **r**
  : the requested range

- **radix**
  : the desired radix

  Before **Fortran 2008**, at least one of the arguments **r** or **p** shall
  be present; since **Fortran 2008**, they are assumed to be zero if
  absent.

### **Result**

selected_real_kind returns the value of the kind type parameter of
a real data type with decimal precision of at least **p** digits,
a decimal exponent range of at least R, and with the requested
**radix**.

If **p** or **r** is absent, the result value is the same as if it
were present with the value zero.

If the **radix** parameter is absent, there is no requirement on
the radix of the selected kind and real kinds with any radix can be
returned.

If more than one real data type meet the criteria, the kind
of the data type with the smallest decimal precision is returned. If
no real data type matches the criteria, the result is

- **-1**
  : if the processor does not support a real data type with a
  precision greater than or equal to **p**, but the **r** and **radix**
  requirements can be fulfilled

- **-2**
  : if the processor does not support a real type with an
  exponent range greater than or equal to **r**, but **p** and **radix** are
  fulfillable

- **-3**
  : if **radix** but not **p** and **r** requirements are fulfillable

- **-4**
  : if **radix** and either **p** or **r** requirements are fulfillable

- **-5**
  : if there is no real type with the given **radix**

### **Examples**

Sample program:

```fortran
program demo_selected_real_kind
implicit none
integer,parameter :: p6 = selected_real_kind(6)
integer,parameter :: p10r100 = selected_real_kind(10,100)
integer,parameter :: r400 = selected_real_kind(r=400)
real(kind=p6) :: x
real(kind=p10r100) :: y
real(kind=r400) :: z

   print *, precision(x), range(x)
   print *, precision(y), range(y)
   print *, precision(z), range(z)
end program demo_selected_real_kind
```

Results:

```text
  >            6          37
  >           15         307
  >           18        4931
```

### **Standard**

Fortran 95 ; with RADIX - Fortran 2008

### **See Also**

[**precision**(3)](#precision),
[**range**(3)](#range),
[**radix**(3)](#radix)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
