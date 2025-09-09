(maxval)=
## maxval

### **Name**

**maxval**(3) - \[ARRAY:REDUCTION\] Determines the maximum value in an array or row

### **Synopsis**

```fortran
    result = maxval(array [,mask]) | maxval(array [,dim] [,mask])
```

```fortran
     NUMERIC function maxval(array ,dim, mask)

      NUMERIC,intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **NUMERIC** designates any numeric type and kind.

### **Description**

**maxval**(3) determines the maximum value of the elements in an
array value, or, if the **dim** argument is supplied, determines the
maximum value along each row of the array in the **dim** direction. If
**mask** is present, only the elements for which **mask** is _.true._
are considered. If the array has zero size, or all of the elements of
**mask** are _.false._, then the result is the most negative number
of the type and kind of **array** if **array** is numeric, or a string
of nulls if **array** is of character type.

### **Options**

- **array**
  : Shall be an array of type _integer_, _real_, or _character_.

- **dim**
  : (Optional) Shall be a scalar of type _integer_, with a value between
  one and the rank of **array**, inclusive. It may not be an optional
  dummy argument.

- **mask**
  : (Optional) Shall be an array of type _logical_, and conformable with
  **array**.

### **Result**

If **dim** is absent, or if **array** has a rank of one, the result is a scalar.
If **dim** is present, the result is an array with a rank one less than the
rank of **array**, and a size corresponding to the size of **array** with the
**dim** dimension removed. In all cases, the result is of the same type and
kind as **array**.

### **Examples**

sample program:

```fortran
program demo_maxval
implicit none
integer,save :: ints(3,5)= reshape([&
   1,  2,  3,  4,  5, &
  10, 20, 30, 40, 50, &
  11, 22, 33, 44, 55  &
],shape(ints),order=[2,1])

   write(*,*) maxval(ints)
   write(*,*) maxval(ints,dim=1)
   write(*,*) maxval(ints,dim=2)
   ! find biggest number less than 30 with mask
   write(*,*) maxval(ints,mask=ints.lt.30)
end program demo_maxval
```

Results:

```
 >  55
 >  11     22     33     44     55
 >   5     50     55
 >  22
```

### **Standard**

Fortran 95

### **See Also**

[**maxloc**(3)](#maxloc),
[**minloc**(3)](#minloc),
[**minval**(3)](#minval),
[**max**(3)](#max),
[**min**(3)](#min)

_fortran-lang intrinsic descriptions_
