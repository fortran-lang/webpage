## iachar

### **Name**

**iachar**(3) - \[CHARACTER:CONVERSION\] Code in ASCII collating sequence

### **Syntax**

```fortran
result = iachar(c, kind)
```

### **Description**

**iachar**(c) returns the code for the ASCII character in the first
character position of C.

### **Arguments**

- **c**
  : Shall be a scalar _character_, with _intent(in)_

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default integer kind.

### **Examples**

Sample program:

```fortran
program demo_iachar
implicit none
! create function to convert uppercase letters to lowercase
   write(*,'(a)')lower('abcdefg ABCDEFG')
contains
!
elemental pure function lower(str) result (string)
! Changes a string to lowercase
character(*), intent(In)     :: str
character(len(str))          :: string
integer                      :: i
   string = str
   ! step thru each letter in the string in specified range
   do i = 1, len(str)
      select case (str(i:i))
      case ('A':'Z') ! change letter to miniscule
         string(i:i) = char(iachar(str(i:i))+32)
      case default
      end select
   end do
end function lower
!
end program demo_iachar
```

Results:

```text
   abcdefg abcdefg
```

### **Note**

See [**ichar**(3)](ICHAR) for a discussion of converting between numerical
values and formatted string representations.

### **Standard**

Fortran 95 and later, with KIND argument - Fortran 2003 and later

### **See Also**

[**achar**(3)](ACHAR),
[**char**(3)](CHAR),
[**ichar**(3)](ICHAR)

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](ADJUSTL), [**adjustr**(3)](ADJUSTR), [**index**(3)](INDEX),
  [**scan**(3)](SCAN), [**verify**(3)](VERIFY)

- **Nonelemental:**
  [**len_trim**(3)](LEN_TRIM),
  [**len**(3)](LEN),
  [**repeat**(3)](REPEAT), [**trim**(3)](TRIM)

_fortran-lang intrinsic descriptions_
