(co_sum)=
## co_sum

### **Name**

**co_sum**(3) - \[COLLECTIVE\] Sum of values on the current set of images

### **Synopsis**

```fortran
    call co_sum(a, result_image [,stat] [,errmsg] )
```

```fortran

```

### **Characteristics**

### **Description**

**co_sum**(3) sums up the values of each element of **a** on all images
of the current team.

If result_image is present, the summed-up values are returned in **a**
on the specified image only and the value of **a** on the other images
become undefined.

If result_image is not present, the value is returned on all images. If
the execution was successful and **stat** is present, it is assigned the
value zero. If the execution failed, **stat** gets assigned a nonzero
value and, if present, **errmsg** gets assigned a value describing the
occurred error.

### **Options**

- **a**
  : shall be an integer, real or complex variable, which has the same
  type and type parameters on all images of the team.

- **result_image**
  : (optional) a scalar integer expression; if present, it shall have
  the same the same value on all images and refer to an image of the
  current team.

- **stat**
  : (optional) a scalar integer variable

- **errmsg**
  : (optional) a scalar character variable

### **Examples**

Sample program:

```fortran
program demo_co_sum
implicit none
integer :: val
   val = this_image()
   call co_sum(val, result_image=1)
   if (this_image() == 1) then
      ! prints (n**2 + n)/2, with n = num_images()
      write(*,*) "The sum is ", val
   endif
end program demo_co_sum
```

Results:

```text
    The sum is            1
```

### **Standard**

TS 18508

### **See Also**

[**co_max**(3)](#co_max),
[**co_min**(3)](#co_min),
[**co_reduce**(3)](#co_reduce),
[**co_broadcast**(3)](#co_broadcast)

_fortran-lang intrinsic descriptions_
