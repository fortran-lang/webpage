## shape

### **Name**

**shape**(3) - \[ARRAY INQUIRY\] Determine the shape of an array

### **Syntax**

```fortran
result = shape(source, kind)
```

### **Description**

Determines the shape of an array.

### **Arguments**

- **source**
  : Shall be an array or scalar of any type. If **source** is a pointer it
  must be associated and allocatable arrays must be allocated.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

An _integer_ array of rank one with as many elements as **source** has
dimensions. The elements of the resulting array correspond to the extend
of **source** along the respective dimensions. If **source** is a scalar, the
result is the rank one array of size zero. If **kind** is absent, the return
value has the default integer kind otherwise the specified kind.

### **Examples**

Sample program:

```fortran
program demo_shape
implicit none
character(len=*),parameter :: all='(*(g0,1x))'
integer, dimension(-1:1, -1:2) :: a
   print all, 'shape of array=',shape(a)
   print all, 'shape of constant=',shape(42)
   print all, 'size of shape of constant=',size(shape(42))
   print all, 'ubound of array=',ubound(a)
   print all, 'lbound of array=',lbound(a)
end program demo_shape
```

Results:

```text
   shape of array= 3 4
   shape of constant=
   size of shape of constant= 0
   ubound of array= 1 2
   lbound of array= -1 -1
```

### **Standard**

Fortran 95 and later; with KIND argument Fortran 2003 and later

### **See Also**

[**reshape**(3)](RESHAPE),
[**size**(3)](SIZE)

_fortran-lang intrinsic descriptions_
