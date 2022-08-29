## scan

### **Name**

**scan**(3) - \[CHARACTER:SEARCH\] Scan a string for the presence of a set of characters

### **Syntax**

```fortran
result = scan(string, set[, back [, kind]])
```

### **Description**

Scans a **string** for any of the characters in a **set** of characters.

If **back** is either absent or equals **.false.**, this function returns the
position of the leftmost character of **STRING** that is in **set**. If **back**
equals **.true.**, the rightmost position is returned. If no character of **set**
is found in **string**, the result is zero.

### **Arguments**

- **string**
  : Shall be of type _character_.

- **set**
  : Shall be of type _character_.

- **back**
  : (Optional) shall be of type _logical_.

- **kind**
  : (Optional) An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind** is absent,
the return value is of default integer kind.

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
              2
              6
              0
```

### **Standard**

Fortran 95 and later, with KIND argument - Fortran 2003 and later

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
