(maxloc)=
## maxloc

### **Name**

**maxloc**(3) - \[ARRAY:LOCATION\] Location of the maximum value within an array

### **Synopsis**

```fortran
    result = maxloc(array [,mask]) | maxloc(array [,dim] [,mask])
```

```fortran
     NUMERIC function maxloc(array, dim, mask)

      NUMERIC,intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **NUMERIC** designates any intrinsic numeric type and kind.

### **Description**

**maxloc**(3) determines the location of the element in the array with
the maximum value, or, if the **dim** argument is supplied, determines
the locations of the maximum element along each row of the array in the
**dim** direction.

If **mask** is present, only the elements for which **mask**
is _.true._ are considered. If more than one element in the array has
the maximum value, the location returned is that of the first such element
in array element order.

If the array has zero size, or all of the elements
of **mask** are .false., then the result is an array of zeroes. Similarly,
if **dim** is supplied and all of the elements of **mask** along a given
row are zero, the result value for that row is zero.

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

The value returned is reference to the offset from the beginning of the
array, not necessarily the subscript value if the array subscripts do
not start with one.

### **Examples**

sample program

```fortran
program demo_maxloc
implicit none
integer      :: ii
integer,save :: i(-3:3)=[(abs(abs(ii)-50),ii=-3,3)]
integer,save :: ints(3,5)= reshape([&
   1,  2,  3,  4,  5, &
   10, 20, 30, 40, 50, &
   11, 22, 33, 44, 55  &
],shape(ints),order=[2,1])

    write(*,*) maxloc(ints)
    write(*,*) maxloc(ints,dim=1)
    write(*,*) maxloc(ints,dim=2)
    ! when array bounds do not start with one remember MAXLOC(3) returns
    ! the offset relative to the lower bound-1 of the location of the
    ! maximum value, not the subscript of the maximum value. When the
    ! lower bound of the array is one, these values are the same. In
    ! other words, MAXLOC(3) returns the subscript of the value assuming
    ! the first subscript of the array is one no matter what the lower
    ! bound of the subscript actually is.
    write(*,'(g0,1x,g0)') (ii,i(ii),ii=lbound(i,dim=1),ubound(i,dim=1))
    write(*,*)maxloc(i)

end program demo_maxloc
```

Results:

```text
 >     3       5
 >     3       3       3       3       3
 >     5       5       5
 >  -3 47
 >  -2 48
 >  -1 49
 >  0 50
 >  1 49
 >  2 48
 >  3 47
```

### **Standard**

Fortran 95

### **See Also**

- [**findloc**(3)](#findloc) - Location of first element of ARRAY
  identified by MASK along dimension DIM matching a target
- [**minloc**(3)](#minloc) - Location of the minimum value within an array
- [**maxval**(3)](#maxval)
- [**minval**(3)](#minval)
- [**max**(3)](#max)

_fortran-lang intrinsic descriptions_
