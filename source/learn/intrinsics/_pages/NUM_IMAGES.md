(num_images)=
## num_images

### **Name**

**num_images**(3) - \[COLLECTIVE\] Number of images

### **Synopsis**

```fortran
    result = num_images([team|team_number])
```

```fortran
     integer function num_images (team)

      type(TEAM_TYPE),intent(in),optional    :: team
      integer(kind=KIND),intent(in),optional :: team_number
```

### **Characteristics**

- use of **team** and **team_number** is mutually exclusive
- **team** is is a scalar of of type **TEAM_TYPE** from the intrinsic module ISO_FORTRAN_ENV.
- **team_number** is an _integer_ scalar.
- the result is a default _integer_ scalar.

### **Description**

**num_images**(3) Returns the number of images.

### **Options**

- **team**
  : shall be a scalar of type TEAM_TYPE from the intrinsic module
  ISO_FORTRAN_ENV, with a value that identifies the current or an
  ancestor team.

- **team_number**
  : identifies the initial team or a team whose parent is the same as
  that of the current team.

### **Result**

The number of images in the specified team, or in the current team if
no team is specified.

### **Examples**

Sample program:

```fortran
program demo_num_images
implicit none
integer :: value[*]
real    :: p[*]
integer :: i

   value = this_image()
   sync all
   if (this_image() == 1) then
     do i = 1, num_images()
       write(*,'(2(a,i0))') 'value[', i, '] is ', value[i]
     end do
   endif

 ! The following code uses image 1 to read data and
 ! broadcast it to other images.
   if (this_image()==1) then
      p=1234.5678
      do i = 2, num_images()
         p[i] = p
      end do
   end if
   sync all

end program demo_num_images
```

### **Standard**

Fortran 2008 . With DISTANCE or FAILED argument, TS 18508

### **See Also**

[**this_image**(3)](#this_image),
[**image_index**(3)](#this_index)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
