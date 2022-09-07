## ichar

### **Name**

**ichar**(3) - \[CHARACTER:CONVERSION\] Character-to-integer conversion function

### **Syntax**

```fortran
   elemental function ichar(c,kind)

    character(len=1),intent(in) :: c
    integer,intent(in),optional :: kind
```

### **Description**

**ichar(c)** returns the code for the character in the system's native
character set. The correspondence between characters and their codes is
not necessarily the same across different Fortran implementations. For
example, a platform using EBCDIC would return different values than an
ASCII platform.

See **iachar**(3) for specifically working with the ASCII character
set.

### **Arguments**

- **c**
  : Shall be a scalar _character_, with **intent(in)**

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default _integer_ kind.

### **Examples**

Sample program:

```fortran
program demo_ichar
implicit none
integer i

   write(*,*)ichar(['a','z','A','Z'])
   do i=0,127
      call printme()
   enddo

contains

   subroutine printme()
   character(len=1) :: letter
   
      letter=char(i)
      select case(i)
      case (:31,127:)
         write(*,'(1x,i0.3,1x,"HEX=",z2.2,1x,i0)')i,letter,ichar(letter)
      case default
         write(*,'(1x,i0.3,1x,a,1x,i0)')i,letter,ichar(letter)
      end select
   
   end subroutine printme

end program demo_ichar
```

### **Note**

No intrinsic exists to convert between a numeric value and a formatted
character string representation -- for instance, given the _character_
value '154', obtaining an _integer_ or _real_ value with the value 154, or
vice versa. Instead, this functionality is provided by internal-file
I/O, as in the following example:

```
program read_val
integer value
character(len=10) string, string2
   string = '154'

   ! Convert a string to a numeric value
   read (string,'(I10)') value
   print *, value

   ! Convert a value to a formatted string
   write (string2,'(I10)') value
   print *, string2
end program read_val
```

Results:

```text
            154
           154
```

### **Standard**

Fortran 95 and later, with KIND argument -Fortran 2003 and later

### **See Also**

[**achar**(3)](ACHAR),
[**char**(3)](CHAR),
[**iachar**(3)](IACHAR)

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](ADJUSTL),
  [**adjustr**(3)](ADJUSTR),
  [**index**(3)](INDEX),

[**scan**(3)](SCAN),
[**verify**(3)](VERIFY)

- **Nonelemental:**
  [**len_trim**(3)](LEN_TRIM),
  [**len**(3)](LEN),
  [**repeat**(3)](REPEAT),
  [**trim**(3)](TRIM)

###### fortran-lang intrinsic descriptions
