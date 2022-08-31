## is_iostat_end

### **Name**

**is_iostat_end**(3) - \[STATE\] Test for end-of-file value

### **Syntax**

```fortran
function is_iostat_end(i)

    logical function   :: is_iostat_end (i) result(yesno)
    integer,intent(in) :: i
```

### **Description**

is_iostat_end(3) tests whether a variable (assumed returned as a status
from an I/O statement) has the "end of file" I/O status value.

The function is equivalent to comparing the variable with the
**iostat_end** parameter of the intrinsic module **iso_fortran_env**.

### **Arguments**

- **i**
  : An _integer_ status value to test if indicating end of file.

### **Returns**

Returns a _logical_ of the default kind, **.true.** if **i** has the value
which indicates an end of file condition for **iostat=** specifiers, and is
**.false.** otherwise.

### **Examples**

Sample program:

```fortran
program demo_iostat
implicit none
real               :: value
integer            :: ios
character(len=256) :: message
   write(*,*)'Begin entering numeric values, one per line'
   do
      read(*,*,iostat=ios,iomsg=message)value
      if(ios.eq.0)then
         write(*,*)'VALUE=',value
      elseif( is_iostat_end(ios) ) then
         stop 'end of file. Goodbye!'
      else
         write(*,*)'ERROR:',ios,trim(message)
      endif
      !
   enddo
end program demo_iostat
```

### **Standard**

Fortran 2003 and later

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
