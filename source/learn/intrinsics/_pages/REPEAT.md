(repeat)=
## repeat

### **Name**

**repeat**(3) - \[CHARACTER\] Repeated string concatenation

### **Synopsis**

```fortran
    result = repeat(string, ncopies)
```

```fortran
     character(len=len(string)*ncopies) function repeat(string, ncopies)

      character(len=*),intent(in)   :: string
      integer(kind=**),intent(in)   :: ncopies
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **string** is a scalar _character_ type.
- **ncopies** is a scalar integer.
- the result is a new scalar of type _character_ of the same kind as
  **string**

### **Description**

**repeat**(3) concatenates copies of a string.

### **Options**

- **string**
  : The input string to repeat

- **ncopies**
  : Number of copies to make of **string**, greater than or equal to zero (0).

### **Result**

A new string built up from **ncopies** copies of **string**.

### **Examples**

Sample program:

```fortran
program demo_repeat
implicit none
    write(*,'(a)') repeat("^v", 35)         ! line break
    write(*,'(a)') repeat("_", 70)          ! line break
    write(*,'(a)') repeat("1234567890", 7)  ! number line
    write(*,'(a)') repeat("         |", 7)  !
end program demo_repeat
```

Results:

```text
 > ^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v
 > ______________________________________________________________________
 > 1234567890123456789012345678901234567890123456789012345678901234567890
 >          |         |         |         |         |         |         |
```

### **Standard**

Fortran 95

### **See Also**

Functions that perform operations on character strings:

- **Elemental:**
  [**adjustl**(3)](#adjustl),
  [**adjustr**(3)](#adjustr),
  [**index**(3)](#index),
  [**scan**(3)](#scan),
  [**verify**(3)](#verify)

- **Non-elemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat),
  [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

#
