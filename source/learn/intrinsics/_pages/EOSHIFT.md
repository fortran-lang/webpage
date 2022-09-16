## eoshift

### **Name**

**eoshift**(3) - \[TRANSFORMATIONAL\] End-off shift elements of an array

### **Syntax**

```fortran
result = eoshift(array, shift, boundary, dim)
```

### **Description**

**eoshift(array, shift\[, boundary, dim\])** performs an end-off shift
on elements of **array** along the dimension of **dim**. If **dim** is omitted it is
taken to be **1**. **dim** is a scalar of type _integer_ in the range of **1 \<= DIM
\<= n** where **"n"** is the rank of **array**. If the rank of **array** is one, then
all elements of **array** are shifted by **shift** places. If rank is greater
than one, then all complete rank one sections of **array** along the given
dimension are shifted. Elements shifted out one end of each rank one
section are dropped. If **boundary** is present then the corresponding value
from **boundary** is copied back in the other end. If **boundary** is not
present then the following are copied in depending on the type of **array**.

    Array Type     | Boundary Value
    -----------------------------------------------------
    Numeric        | 0 of the type and kind of **array**
    Logical        | .false.
    Character(len) |  LEN blanks

### **Arguments**

- **array**
  : May be any type, not scalar.

- **shift**
  : The type shall be _integer_.

- **boundary**
  : Same type as ARRAY.

- **dim**
  : The type shall be _integer_.

### **Returns**

Returns an array of same type and rank as the **array** argument.

### **Examples**

Sample program:

```fortran
program demo_eoshift
implicit none
integer, dimension(3,3) :: a
integer :: i

    a = reshape( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [ 3, 3 ])
    print '(3i3)', (a(i,:),i=1,3)

    print *

    ! shift it
    a = eoshift(a, SHIFT=[1, 2, 1], BOUNDARY=-5, DIM=2)
    print '(3i3)', (a(i,:),i=1,3)

end program demo_eoshift
```

Results:

```text
     1  4  7
     2  5  8
     3  6  9

     4  7 -5
     8 -5 -5
     6  9 -5
```

### **Standard**

Fortran 95 and later

 _fortran-lang intrinsic descriptions_
