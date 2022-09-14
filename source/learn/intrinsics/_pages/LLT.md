## llt

### **Name**

**llt**(3) - \[CHARACTER:COMPARE\] Lexical less than

### **Syntax**

```fortran
result = llt(string_a, string_b)
```

### **Description**

Determines whether one string is lexically less than another string,
where the two strings are interpreted as containing ASCII character
codes. If the **string_a** and **string_b** are not the same length, the shorter
is compared as if spaces were appended to it to form a value that has
the same length as the longer.

In general, the lexical comparison intrinsics LGE, LGT, LLE, and LLT
differ from the corresponding intrinsic operators .ge., .gt., .le., and
.lt., in that the latter use the processor's character ordering (which
is not ASCII on some targets), whereas the former always use the ASCII
ordering.

### **Arguments**

- **string_a**
  : Shall be of default _character_ type.

- **string_b**
  : Shall be of default _character_ type.

### **Returns**

Returns .true. if string_a \<= string_b, and .false. otherwise, based
on the ASCII ordering.

### **Standard**

FORTRAN 77 and later

### **See Also**

[**lge**(3)](LGE),
[**lgt**(3)](LGT),
[**lle**(3](LLE))

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
