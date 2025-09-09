(minloc)=
## minloc

### **Name**

**minloc**(3) - \[ARRAY:LOCATION\] Location of the minimum value within an array

### **Synopsis**

```fortran
    result = minloc(array [,mask]) | minloc(array [,dim] [,mask])
```

```fortran
     NUMERIC function minloc(array, dim, mask)

      NUMERIC,intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **NUMERIC** is any numeric type and kind.

### **Description**

**minloc**(3) determines the location of the element in the array with
the minimum value, or, if the **dim** argument is supplied, determines
the locations of the minimum element along each row of the array in
the **dim** direction.

If **mask** is present, only the elements for which **mask** is _true._
are considered.

If more than one element in the array has the minimum value, the
location returned is that of the first such element in array element
order.

If the array has zero size, or all of the elements of **mask** are
_.false._, then the result is an array of zeroes. Similarly, if **dim**
is supplied and all of the elements of **mask** along a given row are
zero, the result value for that row is zero.

### **Options**

- **array**
  : Shall be an array of type _integer_, _real_, or _character_.

- **dim**
  : (Optional) Shall be a scalar of type _integer_, with a value between
  one and the rank of **array**, inclusive. It may not be an optional
  dummy argument.

- **mask**
  : Shall be an array of type _logical_, and conformable with **array**.

### **Result**

If **dim** is absent, the result is a rank-one array with a length equal
to the rank of **array**. If **dim** is present, the result is an array
with a rank one less than the rank of **array**, and a size corresponding
to the size of **array** with the **dim** dimension removed. If **dim**
is present and **array** has a rank of one, the result is a scalar. In
all cases, the result is of default _integer_ type.

### **Examples**

sample program:

```fortran
program demo_minloc
implicit none
integer,save :: ints(3,5)= reshape([&
   4, 10,  1,  7, 13, &
   9, 15,  6, 12,  3, &
  14,  5, 11,  2,  8  &
],shape(ints),order=[2,1])
   write(*,*) minloc(ints)
   write(*,*) minloc(ints,dim=1)
   write(*,*) minloc(ints,dim=2)
   ! where in each column is the smallest number .gt. 10 ?
   write(*,*) minloc(ints,dim=2,mask=ints.gt.10)
   ! a one-dimensional array with dim=1 explicitly listed returns a scalar
   write(*,*) minloc(pack(ints,.true.),dim=1) ! scalar
end program demo_minloc
```

Results:

```text
 >        1       3
 >        1       3       1       3       2
 >        3       5       4
 >        5       4       3
 >        7
```

### **Standard**

Fortran 95

### **See Also**

- [**findloc**(3)](#findloc) - Location of first element of ARRAY
  identified by MASK along dimension DIM matching a target
- [**maxloc**(3)](#maxloc) - Location of the maximum value within an array
- [**minloc**(3)](#minloc) - Location of the minimum value within an array
- [**min**(3)](#min)
- [**minval**(3)](#minval)
- [**maxval**(3)](#maxval)
- [**max**(3)](#max)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
