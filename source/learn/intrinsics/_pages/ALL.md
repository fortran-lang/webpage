(all)=
## all

### **Name**

**all**(3) - \[ARRAY:REDUCTION\] Determines if all the values are true

### **Synopsis**

```fortran
   result = all(mask [,dim])
```

```fortran
     function all(mask ,dim)

      logical(kind=KIND),intent(in) :: mask(..)
      integer,intent(in),optional   :: dim
      logical(kind=KIND)            :: all(..)
```

### **Characteristics**

- **mask** is a _logical_ array
- **dim** is an _integer_
- the result is a logical array if **dim** is supplied,
  otherwise it is a logical scalar. It has the same characteristics
  as **mask**

### **Description**

**all**(3) determines if all the values are true in **mask** in the
array along dimension **dim** if **dim** is specified; otherwise all
elements are tested together.

This testing type is called a logical conjunction of elements of
**mask** along dimension **dim**.

The mask is generally a _logical_ expression, allowing for comparing
arrays and many other common operations.

### **Options**

- **mask**
  : the logical array to be tested for all elements being _.true_.

- **dim**
  : **dim** indicates the direction through the elements of **mask**
  to group elements for testing.
  : **dim** has a value that lies between one and the rank of **mask**.
  : The corresponding actual argument shall not be an optional dummy
  argument.
  : If **dim** is not present all elements are tested and a single
  scalar value is returned.

### **Result**

1.  If **dim** is not present **all(mask)** is _.true._ if all elements
    of **mask** are _.true._. It also is _.true._ if **mask** has zero size;
    otherwise, it is _.false._ .

2.  If the rank of **mask** is one, then **all(mask, dim)** is equivalent
    to **all(mask)**.

3.  If the rank of **mask** is greater than one and **dim** is present then
    **all(mask,dim)** returns an array with the rank (number of
    dimensions) of **mask** minus 1. The shape is determined from the
    shape of **mask** where the **dim** dimension is elided. A value is
    returned for each set of elements along the **dim** dimension.

### **Examples**

Sample program:

```fortran
program demo_all
implicit none
logical,parameter :: T=.true., F=.false.
logical bool
  ! basic usage
   ! is everything true?
   bool = all([ T,T,T ])
   bool = all([ T,F,T ])
   print *, bool

  ! by a dimension
   ARRAYS: block
   integer :: a(2,3), b(2,3)
    ! set everything to one except one value in b
    a = 1
    b = 1
    b(2,2) = 2
    ! now compare those two arrays
    print *,'entire array :', all(a ==  b )
    print *,'compare columns:', all(a ==  b, dim=1)
    print *,'compare rows:', all(a ==  b, dim=2)
  end block ARRAYS

end program demo_all
```

Results:

```text
 >  T
 >  F
 >  entire array : F
 >  compare columns: T F T
 >  compare rows: T F
```

### **Standard**

Fortran 95

### **See Also**

[**any**(3)](#any)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
