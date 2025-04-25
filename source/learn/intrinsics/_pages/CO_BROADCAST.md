(co_broadcast)=
## co_broadcast

### **Name**

**co_broadcast**(3) - \[COLLECTIVE\] Copy a value to all images the current set of images

### **Synopsis**

```fortran
    call co_broadcast(a, source_image [,stat] [,errmsg] )
```

```fortran

```

### **Characteristics**

### **Description**

**co_broadcast**(3) copies the value of argument **a** on the image with image
index source_image to all images in the current team. **a** becomes defined
as if by intrinsic assignment. If the execution was successful and **stat**
is present, it is assigned the value zero. If the execution failed, **stat**
gets assigned a nonzero value and, if present, **errmsg** gets assigned a
value describing the occurred error.

### **Options**

- **a**
  : **intent(inout)** argument; shall have the same dynamic type and
  type parameters on all images of the current team. If it is an
  array, it shall have the same shape on all images.

- **source_image**
  : a scalar integer expression. It shall have the same the same value
  on all images and refer to an image of the current team.

- **stat**
  : (optional) a scalar integer variable

- **errmsg**
  : (optional) a scalar character variable

### **Examples**

Sample program:

```fortran
program demo_co_broadcast
implicit none
integer :: val(3)
   if (this_image() == 1) then
      val = [1, 5, 3]
   endif
   call co_broadcast (val, source_image=1)
   print *, this_image(), ":", val
end program demo_co_broadcast
```

### **Standard**

Fortran xx

### **See Also**

[**co_max**(3)](#co_max),
[**co_min**(3)](#co_min),
[**co_sum**(3)](#co_sum),
[**co_reduce**(3)](#co_reduce)

_fortran-lang intrinsic descriptions_
