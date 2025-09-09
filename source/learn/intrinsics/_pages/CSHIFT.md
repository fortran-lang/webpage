(cshift)=
## cshift

### **Name**

**cshift**(3) - \[TRANSFORMATIONAL\] Circular shift elements of an array

### **Synopsis**

```fortran
   result = cshift(array, shift [,dim])
```

```fortran
    type(TYPE, kind=KIND) function cshift(array, shift, dim )

     type(TYPE,kind=KIND),intent(in) :: array(..)
     integer(kind=**),intent(in)  :: shift
     integer(kind=**),intent(in)  :: dim
```

### **Characteristics**

- **array** may be any type and rank
- **shift** an _integer_ scalar if **array** has rank one.
  Otherwise, it shall be scalar or of rank n-1 and of shape [d1, d2,
  ..., dDIM-1, dDIM+1, ..., dn] where [d1, d2, ..., dn] is the shape
  of **array**.
- **dim** is an _integer_ scalar with a value in the range 1 <= **dim**
  <= n, where n is the rank of **array**.
  If **dim** is absent, it is as if it were present with the value 1.
- the result will automatically be of the same type, kind and shape as **array**.

NOTE:
:a kind designated as \*\* may be any supported kind for the type

### **Description**

**cshift**(3) performs a circular shift on elements
of **array** along the dimension of **dim**. If **dim** is omitted it is
taken to be **1**. **dim** is a scalar of type _integer_ in the range of
**1 \<= dim \<= n**, where "n" is the rank of **array**.

If the rank of
**array** is one, then all elements of **array** are shifted by **shift**
places. If rank is greater than one, then all complete rank one sections
of **array** along the given dimension are shifted. Elements shifted
out one end of each rank one section are shifted back in the other end.

### **Options**

- **array**
  : An array of any type which is to be shifted

- **shift**
  : the number of positions to circularly shift. A negative value produces
  a right shift, a positive value produces a left shift.

- **dim**
  : the dimension along which to shift a multi-rank **array**. Defaults
  to 1.

### **Result**

Returns an array of same type and rank as the **array** argument.

The rows of an array of rank two may all be shifted by the same amount
or by different amounts.

### **Examples**

Sample program:

```fortran
program demo_cshift
implicit none
integer, dimension(5)   :: i1,i2,i3
integer, dimension(3,4) :: a, b
   !basics
    i1=[10,20,30,40,50]
    print *,'start with:'
    print '(1x,5i3)', i1
    print *,'shift -2'
    print '(1x,5i3)', cshift(i1,-2)
    print *,'shift +2'
    print '(1x,5i3)', cshift(i1,+2)

    print *,'start with a matrix'
    a = reshape( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ], [ 3, 4 ])
    print '(4i3)', a(1,:)
    print '(4i3)', a(2,:)
    print '(4i3)', a(3,:)
    print *,'matrix shifted along rows, each by its own amount [-1,0,1]'
    b = cshift(a, SHIFT=[1, 0, -1], DIM=2)
    print *
    print '(4i3)', b(1,:)
    print '(4i3)', b(2,:)
    print '(4i3)', b(3,:)
end program demo_cshift
```

Results:

```text
 >  start with:
 >   10 20 30 40 50
 >  shift -2
 >   40 50 10 20 30
 >  shift +2
 >   30 40 50 10 20
 >  start with a matrix
 >   1  4  7 10
 >   2  5  8 11
 >   3  6  9 12
 >  matrix shifted along rows, each by its own amount
 >
 >   4  7 10  1
 >   2  5  8 11
 >  12  3  6  9
```

### **Standard**

Fortran 95

### **See Also**

- [**eoshift**(3)](#eoshift) - End-off shift elements of an array
<!--
- [**cshift**(3)](#cshift) - Circular shift elements of an array
  -->
- [**sum**(3)](#sum) - sum the elements of an array
- [**product**(3)](#product) - Product of array elements
- [**findloc**(3)](#findloc) - Location of first element of ARRAY identified by MASK along dimension DIM having a value
- [**maxloc**(3)](#maxloc) - Location of the maximum value within an array

_fortran-lang intrinsic descriptions_
