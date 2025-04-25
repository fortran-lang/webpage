(ichar)=
## ichar

### **Name**

**ichar**(3) - \[CHARACTER:CONVERSION\] Character-to-integer code conversion function

### **Synopsis**

```fortran
    result = ichar(c [,kind])
```

```fortran
     elemental integer(kind=KIND) function ichar(c,KIND)

      character(len=1,kind=**),intent(in) :: c
      integer,intent(in),optional :: KIND
```

### **Characteristics**

- **c** is a scalar _character_
- **kind** is a constant _integer_ initialization expression indicating
  the kind parameter of the result.
- The return value is of type _integer_ and of kind **kind**. If **kind**
  is absent, the return value is of default _integer_ kind.

### **Description**

**ichar**(3) returns the code for the character in the system's native
character set. The correspondence between characters and their codes is
not necessarily the same across different Fortran implementations. For
example, a platform using EBCDIC would return different values than an
ASCII platform.

See **iachar**(3) for specifically working with the ASCII character set.

### **Options**

- **c**
  : The input character to determine the code for.
  Its value shall be that of a character capable of representation in the processor.

- **kind**
  : indicates the kind parameter of the result. If **kind** is absent,
  the return value is of default _integer_ kind.

### **Result**

The code in the system default character set for the character being
queried is returned.

The result is the position of **c** in the processor collating sequence
associated with the kind type parameter of **c**.

it is nonnegative and less than n, where n is the number of characters
in the collating sequence.

The kind type parameter of the result shall specify an integer kind
that is capable of representing n.

For any characters C and D capable of representation in the processor,
C <= D is true if and only if ICHAR (C) <= ICHAR (D) is true and C ==
D is true if and only if ICHAR (C) == ICHAR (D) is true.

### **Examples**

Sample program:

```fortran
program demo_ichar
implicit none

   write(*,*)ichar(['a','z','A','Z'])

end program demo_ichar
```

Results:

```text
             97         122          65          90
```

### **Standard**

Fortran 95 , with KIND argument -Fortran 2003

### **See Also**

[**achar**(3)](#achar),
[**char**(3)](#char),
[**iachar**(3)](#iachar)

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl),
  [**adjustr**(3)](#adjustr),
  [**index**(3)](#index),

[**scan**(3)](#scan),
[**verify**(3)](#verify)

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat),
  [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
