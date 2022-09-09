## logical

### **Name**

**logical**(3) - \[TYPE:LOGICAL\] Converts one kind of _logical_ variable to another

### **Syntax**

```fortran
result = logical(l, kind)

 logical(kind=KIND) function logical(L,KIND)
  logical(kind=INK),intent(in) :: L
  integer,intent(in),optional :: KIND
```

### **Description**

Converts one kind of _logical_ variable to another.

### **Arguments**

- **l**
  : The type shall be _logical_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is a _logical_ value equal to **l**, with a kind
corresponding to **kind**, or of the default logical kind if **kind** is not
given.

### **Examples**

Sample program:

```fortran
program demo_logical
! Access array containing the kind type parameter values supported by this
! compiler for entities of logical type
use iso_fortran_env, only : logical_kinds

   ! list kind values supported on this platform, which generally vary
   ! in storage size
   do i =1, size(logical_kinds)
      write(*,*)logical_kinds(i)
   enddo

end program demo_logical
```
Results:

```text
              1
              2
              4
              8
             16
```
### **Standard**

Fortran 95 and later, related ISO_FORTRAN_ENV module - fortran 2009

### **See Also**

[**int**(3)](INT),
[**real**(3)](REAL),
[**cmplx**(3)](CMPLX)

###### fortran-lang intrinsic descriptions
