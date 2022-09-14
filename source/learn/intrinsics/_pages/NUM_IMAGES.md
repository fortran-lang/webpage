## num_images

### **Name**

**num_images**(3) - \[COLLECTIVE\] Number of images

### **Syntax**

```fortran
result = num_images(distance, failed)
```

### **Description**

Returns the number of images.

### **Arguments**

- **distance**
  : (optional, **intent(in)**) Nonnegative scalar integer

- **failed**
  : (optional, **intent(in)**) Scalar logical expression

### **Returns**

Scalar default-kind _integer_. If **distance** is not present or has value 0,
the number of images in the current team is returned. For values smaller
or equal distance to the initial team, it returns the number of images
index on the ancestor team which has a distance of **distance** from the
invoking team. If **distance** is larger than the distance to the initial
team, the number of images of the initial team is returned. If **failed** is
not present the total number of images is returned; if it has the value
.true., the number of failed images is returned, otherwise, the number
of images which do have not the failed status.

### **Examples**

Sample program:

```fortran
program demo_num_images
implicit none
integer :: value[*]
integer :: i

   value = this_image()
   sync all
   if (this_image() == 1) then
     do i = 1, num_images()
       write(*,'(2(a,i0))') 'value[', i, '] is ', value[i]
     end do
   endif

end program demo_num_images
```

### **Standard**

Fortran 2008 and later. With DISTANCE or FAILED argument, TS 18508 or later

### **See Also**

[**this_image**(3)](THIS_IMAGE),
[**image_index**(3)](THIS_INDEX)

_fortran-lang intrinsic descriptions_
