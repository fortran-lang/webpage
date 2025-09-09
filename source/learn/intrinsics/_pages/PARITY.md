(parity)=
## parity

### **Name**

**parity**(3) - \[ARRAY:REDUCTION\] Array reduction by .NEQV. operation

### **Synopsis**

```fortran
    result = parity( mask [,dim] )
```

```fortran
     logical(kind=KIND) function parity(mask, dim)

      type(logical(kind=KIND)),intent(in)        :: mask(..)
      type(integer(kind=**)),intent(in),optional :: dim
```

### **Characteristics**

- **mask** is a _logical_ array
- **dim** is an integer scalar
- the result is of type _logical_ with the same kind type parameter as **mask**.
  It is a scalar if **dim** does not appear; otherwise it is the rank and shape
  of **mask** with the dimension specified by **dim** removed.
- a kind designated as \*\* may be any supported kind for the type

### **Description**

**parity**(3) calculates the parity array (i.e. the reduction using .neqv.) of
**mask** along dimension **dim** if **dim** is present and not 1. Otherwise, it
returns the parity of the entire **mask** array as a scalar.

### **Options**

- **mask**
  : Shall be an array of type _logical_.

- **dim**
  : (Optional) shall be a scalar of type _integer_ with a value in the
  range from _1 to n_, where _n_ equals the rank of **mask**.

### **Result**

The result is of the same type as **mask**.

If **dim** is absent, a scalar with the parity of all elements in **mask**
is returned: _.true._ if an odd number of elements are _.true._
and _.false._ otherwise.

If MASK has rank one, PARITY (MASK, DIM) is equal to PARITY (MASK). Otherwise, the
result is an array of parity values with dimension **dim** dropped.

### **Examples**

Sample program:

```fortran
program demo_parity
implicit none
logical, parameter :: T=.true., F=.false.
logical :: x(3,4)
  ! basics
   print *, parity([T,F])
   print *, parity([T,F,F])
   print *, parity([T,F,F,T])
   print *, parity([T,F,F,T,T])
   x(1,:)=[T,T,T,T]
   x(2,:)=[T,T,T,T]
   x(3,:)=[T,T,T,T]
   print *, parity(x)
   print *, parity(x,dim=1)
   print *, parity(x,dim=2)
end program demo_parity
```

Results:

```text
 >  T
 >  T
 >  F
 >  T
 >  F
 >  T T T T
 >  F F F
```

### **Standard**

Fortran 2008

### **See also**

- [**all**(3)](#all) - Determines if all the values are true
- [**any**(3)](#any) - Determines if any of the values in the logical array are _.true._
- [**count**(3)](#count) - Count true values in an array
- [**sum**(3)](#sum) - Sum the elements of an array
- [**maxval**(3)](#maxval) - Determines the maximum value in an array or row
- [**minval**(3)](#minval) - Minimum value of an array
- [**product**(3)](#product) - Product of array elements
- [**reduce**(3)](#reduce) - General array reduction

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
