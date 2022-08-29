## reshape

### **Name**

**reshape**(3) - \[ARRAY RESHAPE\] Function to reshape an array

### **Syntax**

```fortran
result = reshape(source, shape, pad, order)
```

### **Description**

Reshapes array **source** to correspond to **shape**. If necessary, the new
array may be padded with elements from **pad** or permuted as defined by
**order**.

### **Arguments**

- **source**
  : an array of any type.

- **shape**
  : an array of rank one and type _integer_. Its values must be positive
  or zero.

- **pad**
  : (Optional) an array of the same type as **source**.

- **order**
  : (Optional) an array of type _integer_ and the same shape as **shape**. Its
  values shall be a permutation of the numbers from 1 to n, where n is
  the size of **shape**. If **order** is absent, the natural ordering shall be
  assumed.

### **Returns**

The result is an array of shape **shape** with the same type as **source**.

### **Examples**

Sample program:

```fortran
program demo_reshape
implicit none
integer :: i
integer, dimension(4) :: x=[(i,i=10,40,10)]
real :: xx(3,4)
real,allocatable :: v(:)
    ! x is originally a vector with four elements
    write(*,*) shape(x) ! what is the current shape of the array?
    write(*,*) shape(reshape(x, [2, 2]))    ! prints "2 2"

    ! pack any array into a vector
    xx=1.0
    v=reshape(xx,[size(xx)])
    write(*,*)shape(v),ubound(v)
end program demo_reshape
```

Results:

```text
              4
              2           2
             12          12
```

### **Standard**

Fortran 95 and later

### **See Also**

[**shape**(3)](SHAPE)

###### fortran-lang intrinsic descriptions
