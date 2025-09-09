(max)=
## max

### **Name**

**max**(3) - \[NUMERIC\] Maximum value of an argument list

### **Synopsis**

```fortran
    result = max(a1, a2, a3, ...)
```

```fortran
     elemental TYPE(kind=KIND) function max(a1, a2, a3, ... )

      TYPE(kind=KIND,intent(in),optional :: a1
      TYPE(kind=KIND,intent(in),optional :: a2
      TYPE(kind=KIND,intent(in),optional :: a3
                :
                :
                :
```

### **Characteristics**

- **a3, a3, a4, ...** must be of the same type and kind as **a1**
- the arguments may (all) be _integer_, _real_ or _character_
- there must be at least two arguments
- the length of a character result is the length of the longest argument
- the type and kind of the result is the same as those of the arguments

### **Description**

**max**(3) returns the argument with the largest (most positive) value.

For arguments of character type, the result is as if the arguments had
been successively compared with the intrinsic operational operators,
taking into account the collating sequence of the _character_ kind.

If the selected _character_ argument is shorter than the longest
argument, the result is as all values were extended with blanks on
the right to the length of the longest argument.

It is unusual for a Fortran intrinsic to take an arbitrary number of
options, and in addition **max**(3) is elemental, meaning any number
of arguments may be arrays as long as they are of the same shape.
The examples have an extended description clarifying the resulting
behavior for those not familiar with calling a "scalar" function
elementally with arrays.

See maxval(3) for simply getting the max value of an array.

### **Options**

- **a1**
  : The first argument determines the type and kind of the returned
  value, and of any remaining arguments as well as being a member of
  the set of values to find the maximum (most positive) value of.

- **a2,a3,...**
  : the remaining arguments of which to find the maximum value(s) of.
  : There must be at least two arguments to **max(3)**.

### **Result**

The return value corresponds to an array of the same shape of any
array argument, or a scalar if all arguments are scalar.

The returned value when any argument is an array will be an array of
the same shape where each element is the maximum value occurring at
that location, treating all the scalar values as arrays of that same
shape with all elements set to the scalar value.

### **Examples**

Sample program

```fortran
program demo_max
implicit none
real :: arr1(4)= [10.0,11.0,30.0,-100.0]
real :: arr2(5)= [20.0,21.0,32.0,-200.0,2200.0]
integer :: box(3,4)= reshape([-6,-5,-4,-3,-2,-1,1,2,3,4,5,6],shape(box))

  ! basic usage
   ! this is simple enough when all arguments are scalar

   ! the most positive value is returned, not the one with the
   ! largest magnitude
   write(*,*)'scalars:',max(10.0,11.0,30.0,-100.0)
   write(*,*)'scalars:',max(-22222.0,-0.0001)

   ! strings do not need to be of the same length
   write(*,*)'characters:',max('the','words','order')

   ! leading spaces are significant; everyone is padded on the right
   ! to the length of the longest argument
   write(*,*)'characters:',max('c','bb','a')
   write(*,*)'characters:',max(' c','b','a')

  ! elemental
   ! there must be at least two arguments, so even if A1 is an array
   ! max(A1) is not valid. See MAXVAL(3) and/or MAXLOC(3) instead.

   ! strings in a single array do need to be of the same length
   ! but the different objects can still be of different lengths.
   write(*,"(*('""',a,'""':,1x))")MAX(['A','Z'],['BB','Y '])
   ! note the result is now an array with the max of every element
   ! position, as can be illustrated numerically as well:
   write(*,'(a,*(i3,1x))')'box=   ',box
   write(*,'(a,*(i3,1x))')'box**2=',sign(1,box)*box**2
   write(*,'(a,*(i3,1x))')'max    ',max(box,sign(1,box)*box**2)

   ! Remember if any argument is an array by the definition of an
   ! elemental function all the array arguments must be the same shape.

   ! to find the single largest value of arrays you could use something
   ! like MAXVAL([arr1, arr2]) or probably better (no large temp array),
   ! max(maxval(arr1),maxval(arr2)) instead

   ! so this returns an array of the same shape as any input array
   ! where each result is the maximum that occurs at that position.
   write(*,*)max(arr1,arr2(1:4))
   ! this returns an array just like arr1 except all values less than
   ! zero are set to zero:
   write(*,*)max(box,0)
   ! When mixing arrays and scalars you can think of the scalars
   ! as being a copy of one of the arrays with all values set to
   ! the scalar value.

end program demo_max
```

Results:

```text
    scalars:   30.00000
    scalars: -9.9999997E-05
    characters:words
    characters:c
    characters:b
   "BB" "Z "
   box=    -6  -5  -4  -3  -2  -1   1   2   3   4   5   6
   box**2=-36 -25 -16  -9  -4  -1   1   4   9  16  25  36
   max     -6  -5  -4  -3  -2  -1   1   4   9  16  25  36
   20.00000  21.00000  32.00000  -100.0000
   0  0  0  0  0  0
   1  2  3  4  5  6
```

### **Standard**

FORTRAN 77

### **See Also**

[**maxloc**(3)](#maxloc),
[**minloc**(3)](#minloc),
[**maxval**(3)](#maxval),
[**minval**(3)](#minval),
[**min**(3)](#min)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
