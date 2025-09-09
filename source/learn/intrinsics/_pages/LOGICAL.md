(logical)=
## logical

### **Name**

**logical**(3) - \[TYPE:LOGICAL\] Conversion between kinds of logical values

### **Synopsis**

```fortran
    result = logical(l [,kind])
```

```fortran
     elemental logical(kind=KIND) function logical(l,KIND)

      logical(kind=**),intent(in) :: l
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **l** is of type logical
- **KIND** shall be a scalar integer constant expression.
  If **KIND** is present, the kind type parameter of the result is
  that specified by the value of **KIND**; otherwise, the kind type
  parameter is that of default logical.

### **Description**

**logical**(3) converts one kind of _logical_ variable to another.

### **Options**

- **l**
  : The _logical_ value to produce a copy of with kind **kind**

- **kind**
  : indicates the kind parameter of the result.
  If not present, the default kind is returned.

### **Result**

The return value is a _logical_ value equal to **l**, with a kind
corresponding to **kind**, or of the default logical kind if **kind**
is not given.

### **Examples**

Sample program:

```fortran
Linux
program demo_logical
! Access array containing the kind type parameter values supported by this
! compiler for entities of logical type
use iso_fortran_env, only : logical_kinds
implicit none
integer :: i

   ! list kind values supported on this platform, which generally vary
   ! in storage size as alias declarations
   do i =1, size(logical_kinds)
      write(*,'(*(g0))')'integer,parameter :: boolean', &
      & logical_kinds(i),'=', logical_kinds(i)
   enddo

end program demo_logical
```

Results:

```text
 > integer,parameter :: boolean1=1
 > integer,parameter :: boolean2=2
 > integer,parameter :: boolean4=4
 > integer,parameter :: boolean8=8
 > integer,parameter :: boolean16=16
```

### **Standard**

Fortran 95 , related ISO_FORTRAN_ENV module - fortran 2009

### **See Also**

[**int**(3)](#int),
[**real**(3)](#real),
[**cmplx**(3)](#cmplx)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
