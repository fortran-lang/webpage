(minval)=
## minval

### **Name**

**minval**(3) - \[ARRAY:REDUCTION\] Minimum value of an array

### **Synopsis**

```fortran
    result = minval(array, [mask]) | minval(array [,dim] [,mask])
```

```fortran
     NUMERIC function minval(array, dim, mask)

      NUMERIC,intent(in) :: array(..)
      integer(kind=**),intent(in),optional :: dim
      logical(kind=**),intent(in),optional :: mask(..)
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **NUMERIC** is any numeric type and kind.

### **Description**

**minval**(3) determines the minimum value of the elements in an array
value, or, if the **dim** argument is supplied, determines the minimum
value along each row of the array in the **dim** direction.

If **mask** is present, only the elements for which **mask** is
_.true._ are considered.

If the array has zero size, or all of the elements of **mask**
are _.false._, then the result is **huge(array)** if **array** is
numeric, or a string of **char(len=255)** characters if **array**
is of character type.

### **Options**

- **array**
  : Shall be an array of type _integer_, _real_, or _character_.

- **dim**
  : (Optional) Shall be a scalar of type _integer_, with a value between
  one and the rank of ARRAY, inclusive. It may not be an optional
  dummy argument.

- **mask**
  : Shall be an array of type _logical_, and conformable with **array**.

### **Result**

If **dim** is absent, or if **array** has a rank of one, the result is a scalar.

If **dim** is present, the result is an array with a rank one less than the
rank of **array**, and a size corresponding to the size of **array** with the
**dim** dimension removed. In all cases, the result is of the same type and
kind as **array**.

### **Examples**

sample program:

```fortran
program demo_minval
implicit none
integer :: i
character(len=*),parameter :: g='(3x,*(g0,1x))'

integer,save :: ints(3,5)= reshape([&
       1,  -2,   3,   4,   5,  &
      10,  20, -30,  40,  50,  &
      11,  22,  33, -44,  55  &
],shape(ints),order=[2,1])

integer,save :: box(3,5,2)

   box(:,:,1)=ints
   box(:,:,2)=-ints

   write(*,*)'Given the array'
   write(*,'(1x,*(g4.4,1x))') &
   & (ints(i,:),new_line('a'),i=1,size(ints,dim=1))

   write(*,*)'What is the smallest element in the array?'
   write(*,g) minval(ints),'at <',minloc(ints),'>'

   write(*,*)'What is the smallest element in each column?'
   write(*,g) minval(ints,dim=1)

   write(*,*)'What is the smallest element in each row?'
   write(*,g) minval(ints,dim=2)

   ! notice the shape of the output has less columns
   ! than the input in this case
   write(*,*)'What is the smallest element in each column,'
   write(*,*)'considering only those elements that are'
   write(*,*)'greater than zero?'
   write(*,g) minval(ints, dim=1, mask = ints > 0)

   write(*,*)&
   & 'if everything is false a zero-sized array is NOT returned'
   write(*,*) minval(ints, dim=1, mask = .false.)
   write(*,*)'even for a zero-sized input'
   write(*,g) minval([integer ::], dim=1, mask = .false.)

   write(*,*)'a scalar answer for everything false is huge()'
   write(*,g) minval(ints, mask = .false.)
   write(*,g) minval([integer ::], mask = .false.)

   write(*,*)'some calls with three dimensions'
   write(*,g) minval(box, mask = .true. )
   write(*,g) minval(box, dim=1, mask = .true. )

   write(*,g) minval(box, dim=2, mask = .true. )
   write(*,g) 'shape of answer is ', &
   & shape(minval(box, dim=2, mask = .true. ))

end program demo_minval
```

Results:

```text
 > Given the array
 >    1   -2    3    4    5
 >   10   20  -30   40   50
 >   11   22   33  -44   55
 >
 > What is the smallest element in the array?
 >   -44 at < 3 4 >
 > What is the smallest element in each column?
 >   1 -2 -30 -44 5
 > What is the smallest element in each row?
 >   -2 -30 -44
 > What is the smallest element in each column,
 > considering only those elements that are
 > greater than zero?
 >   1 20 3 4 5
 > if everything is false a zero-sized array is NOT returned
 >  2147483647  2147483647  2147483647  2147483647  2147483647
 > even for a zero-sized input
 >   2147483647
 > a scalar answer for everything false is huge()
 >   2147483647
 >   2147483647
 > some calls with three dimensions
 >   -55
 >   1 -2 -30 -44 5 -11 -22 -33 -40 -55
 >   -2 -30 -44 -5 -50 -55
 >   shape of answer is  3 2
```

### **Standard**

Fortran 95

### **See Also**

[**min**(3)](#min),
[**minloc**(3)](#minloc)
[**maxloc**(3)](#maxloc),
[**maxval**(3)](#maxval),
[**min**(3)](#min)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
