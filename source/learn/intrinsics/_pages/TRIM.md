## trim

### **Name**

**trim**(3) - \[CHARACTER:WHITESPACE\] Remove trailing blank characters of a string

### **Syntax**

```fortran
result = trim(string)
```

### **Description**

Removes trailing blank characters of a string.

### **Arguments**

- **string**
  : Shall be a scalar of type _character_.

### **Returns**

A scalar of type _character_ which length is that of **string** less the
number of trailing blanks.

### **Examples**

Sample program:

```fortran
program demo_trim
implicit none
character(len=10), parameter :: s = "gfortran  "
   write(*,*) len(s), len(trim(s))  ! "10 8", with/without trailing blanks

   ! with/without trailing blanks
   write(*,*) len(s), len(trim('   leading'))
   write(*,*) len(s), len(trim('   trailing    '))
   write(*,*) len(s), len(trim('               '))

end program demo_trim
```

Results:

```text
      10           8
      10          10
      10          11
      10           0
```

### **Standard**

Fortran 95 and later

### **See Also**

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
