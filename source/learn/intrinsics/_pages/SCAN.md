(scan)=
## scan

### **Name**

**scan**(3) - \[CHARACTER:SEARCH\] Scan a string for the presence of a set of characters

### **Synopsis**

```fortran
    result = scan( string, set, [,back] [,kind] )
```

```fortran
     elemental integer(kind=KIND) function scan(string,set,back,kind)

      character(len=*,kind=**),intent(in) :: string
      character(len=*,kind=**),intent(in) :: set
      logical,intent(in),optional :: back
      integer,intent(in),optional :: kind
```

### **Characteristics**

- **string** is a _character_ string of any kind
- **set** must be a _character_ string with the same kind as **string**
- **back** is a _logical_
- **kind** is a scalar _integer_ constant expression
- the result is an _integer_ with the kind specified by **kind**. If
  **kind** is not present the result is a default _integer_.

### **Description**

**scan**(3) scans a **string** for any of the characters in a **set**
of characters.

If **back** is either absent or equals _.false._, this function
returns the position of the leftmost character of **STRING** that is
in **set**. If **back** equals _.true._, the rightmost position is
returned. If no character of **set** is found in **string**, the result
is zero.

### **Options**

- **string**
  : the string to be scanned

- **set**
  : the set of characters which will be matched

- **back**
  : if _.true._ the position of the rightmost character matched is
  returned, instead of the leftmost.

- **kind**
  : the kind of the returned value is the same as **kind** if
  present. Otherwise a default _integer_ kind is returned.

### **Result**

If **back** is absent or is present with the value false and if
**string** contains at least one character that is in **set**, the value
of the result is the position of the leftmost character of **string**
that is in **set**.

If **back** is present with the value true and if **string** contains at
least one character that is in **set**, the value of the result is the
position of the rightmost character of **string** that is in **set**.

The value of the result is zero if no character of STRING is in SET
or if the length of STRING or SET is zero.

### **Examples**

Sample program:

```fortran
program demo_scan
implicit none
   write(*,*) scan("fortran", "ao")          ! 2, found 'o'
   write(*,*) scan("fortran", "ao", .true.)  ! 6, found 'a'
   write(*,*) scan("fortran", "c++")         ! 0, found none
end program demo_scan
```

Results:

```text
 >            2
 >            6
 >            0
```

### **Standard**

Fortran 95 , with KIND argument - Fortran 2003

### **See Also**

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl), [**adjustr**(3)](#adjustr), [**index**(3)](#index),
  [**verify**(3)](#verify)

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat), [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
