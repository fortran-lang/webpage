## dble

### **Name**

**dble**(3) - \[TYPE:NUMERIC\] Double conversion function

### **Syntax**

```fortran
result = dble(a)

    elemental function dble(a)
    type(real(kind=kind(0.0d0)))     :: dble
    type(TYPE(kind=KIND)),intent(in) :: a
```

where TYPE may be _integer_, _real_, or _complex_ and KIND any kind
supported by the TYPE.

### **Description**

**dble(a)** Converts **a** to double precision _real_ type.

### **Arguments**

- **a**
  : The type shall be _integer_, _real_, or _complex_.

### **Returns**

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

FORTRAN 77 and later

### **See Also**

[**float**(3)](#float),
[**real**(3)](#real)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
