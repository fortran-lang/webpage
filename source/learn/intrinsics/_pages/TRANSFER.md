(transfer)=
## transfer

### **Name**

**transfer**(3) - \[TYPE:MOLD\] Transfer bit patterns

### **Synopsis**

```fortran
    result = transfer(source, mold [,size] )
```

```fortran
     type(TYPE(kind=KIND)) function transfer(source,mold,size)

      type(TYPE(kind=KIND)),intent(in) :: source(..)
      type(TYPE(kind=KIND)),intent(in) :: mold(..)
      integer(kind=**),intent(in),optional :: size
```

### **Characteristics**

- **source** shall be a scalar or an array of any type.
- **mold** shall be a scalar or an array of any type.
- **size** shall be a scalar of type _integer_.
- **result** has the same type as **mold**

### **Description**

**transfer**(3) copies the bitwise representation of **source** in memory
into a variable or array of the same type and type parameters as **mold**.

This is approximately equivalent to the C concept of "casting" one type
to another.

### **Options**

- **source**
  : Holds the bit pattern to be copied

- **mold**
  : the type of **mold** is used to define the type of the returned
  value. In addition, if it is an array the returned value is a
  one-dimensional array. If it is a scalar the returned value is a scalar.

- **size**
  : If **size** is present, the result is a one-dimensional array of
  length **size**.

If **size** is absent but **mold** is an array (of any size or
shape), the result is a one-dimensional array of the minimum length
needed to contain the entirety of the bitwise representation of **source**.

If **size** is absent and **mold** is a scalar, the result is a scalar.

### **Result**

The result has the bit level representation of **source**.

If the bitwise representation of the result is longer than that of
**source**, then the leading bits of the result correspond to those of
**source** but any trailing bits are filled arbitrarily.

When the resulting bit representation does not correspond to a valid
representation of a variable of the same type as **mold**, the results are
undefined, and subsequent operations on the result cannot be guaranteed to
produce sensible behavior. For example, it is possible to create _logical_
variables for which **var** and .not. var both appear to be true.

### **Examples**

Sample program:

```fortran
program demo_transfer
use,intrinsic :: iso_fortran_env, only : int32, real32
integer(kind=int32) :: i = 2143289344
real(kind=real32)   :: x
character(len=10)   :: string
character(len=1)    :: chars(10)
   x=transfer(i, 1.0)    ! prints "nan" on i686
   ! the bit patterns are the same
   write(*,'(b0,1x,g0)')x,x ! create a NaN
   write(*,'(b0,1x,g0)')i,i

   ! a string to an array of characters
   string='abcdefghij'
   chars=transfer(string,chars)
   write(*,'(*("[",a,"]":,1x))')string
   write(*,'(*("[",a,"]":,1x))')chars
end program demo_transfer
```

Results:

```text
   1111111110000000000000000000000 NaN
   1111111110000000000000000000000 2143289344
   [abcdefghij]
   [a] [b] [c] [d] [e] [f] [g] [h] [i] [j]
```

### **Comments**

_Joe Krahn_: Fortran uses **molding** rather than **casting**.

Casting, as in C, is an in-place reinterpretation. A cast is a device
that is built around an object to change its shape.

Fortran **transfer**(3) reinterprets data out-of-place. It can be
considered **molding** rather than casting. A **mold** is a device that
confers a shape onto an object placed into it.

The advantage of molding is that data is always valid in the context
of the variable that holds it. For many cases, a decent compiler should
optimize **transfer**(3) into a simple assignment.

There are disadvantages of this approach. It is problematic to define a
union of data types because you must know the largest data object, which
can vary by compiler or compile options. In many cases, an _EQUIVALENCE_
would be far more effective, but Fortran Standards committees seem
oblivious to the benefits of _EQUIVALENCE_ when used sparingly.

### **Standard**

Fortran 90

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions_
