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

See [**ichar**(3)](#char) for a discussion of converting between numerical
values and formatted string representations.

### **Standard**

FORTRAN 77 and later

### **See Also**

[**achar**(3)](#achar),
[**iachar**(3)](#iachar),
[**ichar**(3)](#ichar)

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl), [**adjustr**(3)](#adjustr), [**index**(3)](#index),
  [**scan**(3)](#scan), [**verify**(3)](#verify)

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat), [**trim**(3)](#trim)

 _fortran-lang intrinsic descriptions_
