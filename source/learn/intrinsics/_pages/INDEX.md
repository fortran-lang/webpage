(index)=
## index

### **Name**

**index**(3) - \[CHARACTER:SEARCH\] Position of a substring within a string

### **Synopsis**

```fortran
result = index( string, substring [,back] [,kind] )
```

```fortran
 elemental integer(kind=KIND) function index(string,substring,back,kind)

  character(len=*,kind=KIND),intent(in) :: string
  character(len=*,kind=KIND),intent(in) :: substring
  logical(kind=**),intent(in),optional :: back
  integer(kind=**),intent(in),optional :: kind
```

### **Characteristics**

- **string** is a _character_ variable of any kind
- **substring** is a _character_ variable of the same kind as **string**
- **back** is a _logical_ variable of any supported kind
- **KIND** is a scalar integer constant expression.

### **Description**

**index**(3) returns the position of the start of the leftmost
or rightmost occurrence of string **substring** in **string**,
counting from one. If **substring** is not present in **string**,
zero is returned.

### **Options**

- **string**
  : string to be searched for a match

- **substring**
  : string to attempt to locate in **string**

- **back**
  : If the **back** argument is present and true, the return value is the
  start of the rightmost occurrence rather than the leftmost.

- **kind**
  : if **kind** is present, the kind type parameter is that specified by the value of
  **kind**; otherwise the kind type parameter is that of default integer type.

### **Result**

The result is the starting position of the first substring
**substring** found in **string**.

If the length of **substring** is longer than **string** the result
is zero.

If the substring is not found the result is zero.

If **back** is _.true._ the greatest starting position is returned
(that is, the position of the right-most match). Otherwise,
the smallest position starting a match (ie. the left-most match)
is returned.

The position returned is measured from the left with the first
character of **string** being position one.

Otherwise, if no match is found zero is returned.

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

FORTRAN 77 , with KIND argument Fortran 2003

### **See Also**

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
