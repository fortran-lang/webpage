## this_image

### **Name**

**this_image**(3) - \[COLLECTIVE\] Cosubscript index of this image

### **Syntax**

```fortran
result = this_image()
```
or
```
```fortran
result = this_image(distance)
```
or
```fortran
result = this_image(coarray, dim)
```

### **Description**

Returns the cosubscript for this image.

### **Arguments**

- **distance**
  : (optional, **intent(in)**) Nonnegative scalar integer (not permitted
  together with **coarray**).

- **coarray**
  : Coarray of any type (optional; if **dim** present, required).

- **dim**
  : default integer scalar (optional). If present, **dim** shall be between
  one and the corank of **coarray**.

### **Returns**

Default integer. If **coarray** is not present, it is scalar; if **distance** is
not present or has value **0**, its value is the image index on the invoking
image for the current team, for values smaller or equal distance to the
initial team, it returns the image index on the ancestor team which has
a distance of **distance** from the invoking team. If **distance** is larger
than the distance to the initial team, the image index of the initial
team is returned. Otherwise when the **coarray** is present, if **dim** is not
present, a rank-1 array with corank elements is returned, containing the
cosubscripts for **coarray** specifying the invoking image. If **dim** is
present, a scalar is returned, with the value of the **dim** element of
**this_image(coarray)**.

### **Examples**

Sample program:

```fortran
program demo_this_image
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
end program demo_this_image
```

Results:

```text
   value[1] is 1
```

### **Standard**

Fortran 2008 and later. With DISTANCE argument, TS 18508
or later

### **See Also**

[**num\_images**(3)](NUM_IMAGES),
[**image\_index**(3)](IMAGE_INDEX)

_fortran-lang intrinsic descriptions_
```
