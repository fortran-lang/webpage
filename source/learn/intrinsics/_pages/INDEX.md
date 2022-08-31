## index

### **Name**

**index**(3) - \[CHARACTER:SEARCH\] Position of a substring within a string

### **Syntax**

```fortran
   index(string, substring, back, kind) result(start)

     character(len=*),intent(in) :: string
     character(len=*),intent(in) :: substring
     logical,intent(in),optional :: back
     integer,intent(in),optional :: kind
     integer(kind=KIND)          :: start
```

### **Description**

Returns the position of the start of the leftmost or rightmost
occurrence of string **substring** in **string**, counting from one. If
**substring** is not present in **string**, zero is returned.

### **Arguments**

- **string**
  : string to be searched

- **substring**
  : string to attempt to locate in **string**

- **back**
  : If the **back** argument is present and true, the return value is the
  start of the rightmost occurrence rather than the leftmost.

- **kind**
  : An _integer_ initialization expression indicating the kind parameter
  of the result.

### **Returns**

- **START**
  : The return value is of type _integer_ and of kind **kind**. If **kind** is
  absent, the return value is of default integer kind.

### **Examples**

Example program

```fortran
program demo_index
implicit none
character(len=*),parameter :: str=&
   'Search this string for this expression'
   !1234567890123456789012345678901234567890
   write(*,*)&
      index(str,'this').eq.8,              &
      ! return value is counted from the left end even if BACK=.TRUE.
      index(str,'this',back=.true.).eq.24, &
      ! INDEX is case-sensitive
      index(str,'This').eq.0
end program demo_index
```

Expected Results:

```text
   T T T
```

### **Standard**

FORTRAN 77 and later, with KIND argument Fortran 2003
and later

### **See Also**

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
