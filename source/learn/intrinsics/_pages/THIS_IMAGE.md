(this_image)=
## this_image

### **Name**

**this_image**(3) - \[COLLECTIVE\] Cosubscript index of this image

### **Synopsis**

```fortran
result = this_image() | = this_image(distance) | = this_image(coarray,dim)
```

```fortran
   integer function this_image( distance ,coarray, dim )

    type(TYPE(kind=**),optional :: coarray[*]
    integer,intent(in),optional :: distance
    integer,intent(in),optional :: dim
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **coarray** can be of any type. If **dim** is present it is required.
- **distance** is not permitted together with **coarray**
- if **dim** if present, coarray is required.

### **Description**

**this_image**(3) returns the cosubscript for this image.

### **Options**

- **distance**
  : Nonnegative scalar _integer_ (not permitted together with **coarray**).

- **coarray**
  : if **dim** present, required).

- **dim**
  : If present, **dim** shall be between one and the corank of **coarray**.

### **Result**

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

Fortran 2008. With DISTANCE argument, TS 18508

### **See Also**

[**num_images**(3)](#num_images),
[**image_index**(3)](#image_index)

_fortran-lang intrinsic descriptions_
