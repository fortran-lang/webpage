(co_reduce)=
## co_reduce

### **Name**

**co_reduce**(3) - \[COLLECTIVE\] Reduction of values on the current set of images

### **Synopsis**

```fortran
    call co_reduce(a, operation, result_image [,stat] [,errmsg] )
```

```fortran

```

### **Characteristics**

### **Description**

**co_reduce**(3) determines element-wise the reduction of the value of **a** on
all images of the current team. The pure function passed as **operation** is
used to pairwise reduce the values of **a** by passing either the value of **a**
of different images or the result values of such a reduction as
argument. If **a** is an array, the reduction is done element wise. If
result_image is present, the result values are returned in **a** on the
specified image only and the value of **a** on the other images become
undefined. If result_image is not present, the value is returned on all
images. If the execution was successful and **stat** is present, it is
assigned the value zero. If the execution failed, **stat** gets assigned a
nonzero value and, if present, **errmsg** gets assigned a value describing
the occurred error.

### **Options**

- **a**
  : is an **intent(inout)** argument and shall be nonpolymorphic. If it
  is allocatable, it shall be allocated; if it is a pointer, it shall
  be associated. **a** shall have the same type and type parameters on all
  images of the team; if it is an array, it shall have the same shape
  on all images.

- **operation**
  : pure function with two scalar nonallocatable arguments, which shall
  be nonpolymorphic and have the same type and type parameters as **a**.
  The function shall return a nonallocatable scalar of the same type
  and type parameters as **a**. The function shall be the same on all
  images and with regards to the arguments mathematically commutative
  and associative. Note that OPERATION may not be an elemental unless
  it is an intrinsic function.

- **result_image**

  : (optional) a scalar integer expression; if present, it shall
  have the same the same value on all images and refer to an image
  of the current team.

- **stat**
  : (optional) a scalar integer variable

- **errmsg**
  : (optional) a scalar character variable

### **Examples**

Sample program:

```fortran
program demo_co_reduce
implicit none
integer :: val

   val = this_image()
   call co_reduce(val, myprod, 1)
   if (this_image() == 1) then
      write(*,*) "Product value", val  ! prints num_images() factorial
   endif

contains

pure function myprod(a, b)
   integer, value :: a, b
   integer :: myprod
   myprod = a * b
end function myprod

end program demo_co_reduce
```

### **Note**

While the rules permit in principle an intrinsic function, none of the
intrinsics in the standard fulfill the criteria of having a specific
function, which takes two arguments of the same type and returning that
type as a result.

### **Standard**

TS 18508

### **See Also**

[**co_min**(3)](#co_min),
[**co_max**(3)](#co_max),
[**co_sum**(3)](#co_sum),
[**co_broadcast**(3)](#co_broadcast)

_fortran-lang intrinsic descriptions_
