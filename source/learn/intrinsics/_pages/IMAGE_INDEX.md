(image_index)=
## image_index

### **Name**

**image_index**(3) - \[COLLECTIVE\] Cosubscript to image index conversion

### **Synopsis**

```fortran
    result = image_index(coarray, sub)
```

```fortran

```

### **Characteristics**

### **Description**

**image_index**(3) returns the image index belonging to a cosubscript.

### **Options**

- **coarray**
  : Coarray of any type.

- **sub**
  : default integer rank-1 array of a size equal to the corank of
  **coarray**.

### **Result**

Scalar default integer with the value of the image index which
corresponds to the cosubscripts. For invalid cosubscripts the result is
zero.

### **Examples**

Sample program:

```fortran
program demo image_index
implicit none
integer :: array[2,-1:4,8,*]
   ! Writes  28 (or 0 if there are fewer than 28 images)
   write (*,*) image_index(array, [2,0,3,1])
end demo image_index
```

### **Standard**

Fortran 2008

### **See Also**

[**this_image**(3)](#this_image),
[**num_images**(3)](#num_images)

_fortran-lang intrinsic descriptions_
