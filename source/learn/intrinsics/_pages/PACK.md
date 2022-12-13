## pack

### **Name**

**pack**(3) - \[ARRAY CONSTRUCTION\] Pack an array into an array of rank one

### **Syntax**

```fortran
result = pack(array, mask,vector)

   TYPE(kind=KIND) function pack(array,mask,vector)
   TYPE(kind=KIND),option(in) :: array(*)
   logical  :: mask(*)
   TYPE(kind=KIND),option(in),optional :: vector(*)
```

where TYPE(kind=KIND) may be any type, where **array** and **vector**
and the returned value must by of the same type. **mask** may be a
scalar as well an an array.

### **Description**

Stores the elements of ARRAY in an array of rank one.

The beginning of the resulting array is made up of elements whose **mask**
equals **.true.**. Afterwards, positions are filled with elements taken from
**vector**.

### **Arguments**

- **array**
  : Shall be an array of any type.

- **mask**
  : Shall be an array of type _logical_ and of the same size as **array**.
  Alternatively, it may be a _logical_ scalar.

- **vector**
  : (Optional) shall be an array of the same type as **array** and of rank
  one. If present, the number of elements in **vector** shall be equal to
  or greater than the number of true elements in **mask**. If **mask** is
  scalar, the number of elements in **vector** shall be equal to or
  greater than the number of elements in **array**.

### **Returns**

The result is an array of rank one and the same type as that of **array**.
If **vector** is present, the result size is that of **vector**, the number of
**.true.** values in **mask** otherwise.

### **Examples**

Sample program:

```fortran
program demo_pack
implicit none
   call test1()
   call test2()
   call test3()
contains
!
subroutine test1()
! gathering nonzero elements from an array:
integer :: m(6)

   m = [ 1, 0, 0, 0, 5, 0 ]
   write(*, fmt="(*(i0, ' '))") pack(m, m /= 0)  ! "1 5"

end subroutine test1
!
subroutine test2()
! Gathering nonzero elements from an array and appending elements
! from VECTOR till the size of the mask array (or array size if the
! mask is scalar):
integer :: m(4)

   m = [ 1, 0, 0, 2 ]
   write(*, fmt="(*(i0, ' '))") pack(m, m /= 0, [ 0, 0, 3, 4 ])

end subroutine test2
!
subroutine test3()
! select strings whose second character is "a"
character(len=10) :: m(4)

m = [ character(len=10) :: 'ape', 'bat', 'cat', 'dog']
   write(*, fmt="(*(g0, ' '))") pack(m, m(:)(2:2) == 'a' )

end subroutine test3
!
end program demo_pack
```

Results:

```text
   1 5
   1 2 3 4
   bat        cat
```

### **Standard**

Fortran 95 and later

### **See Also**

[**unpack**(3)](#unpack),
[**merge**(3)](#merge),
[**pack**(3)](#pack),
[**spread**(3)](#spread),
[**unpack**(3)](#unpack)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
