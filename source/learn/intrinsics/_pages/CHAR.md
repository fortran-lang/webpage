## char

### **Name**

**char**(3) - \[CHARACTER\] Character conversion function

### **Syntax**

```fortran
result = char(i, kind)
   elemental integer function char(i,kind)

    integer(kind=KIND),intent(in) :: c
    integer,intent(in),optional :: KIND
```

### **Description**

**char(i, kind)** returns the character represented by the integer **i**.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _character_

### **Examples**

Sample program:

```fortran
program demo_char
implicit none
integer :: i = 74
character(1) :: c
    c = char(i)
    print *, i, c ! returns 'J'
end program demo_char
```

Results:

```text
             74 J
```

### **Note**

See [**ichar**(3)](CHAR) for a discussion of converting between numerical
values and formatted string representations.

### **Standard**

FORTRAN 77 and later

### **See Also**

[**achar**(3)](ACHAR),
[**iachar**(3)](IACHAR),
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

###### fortran-lang intrinsic descriptions
