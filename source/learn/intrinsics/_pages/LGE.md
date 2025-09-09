(lge)=
## lge

### **Name**

**lge**(3) - \[CHARACTER:COMPARE\] ASCII Lexical greater than or equal

### **Synopsis**

```fortran
    result = lge(string_a, stringb)
```

```fortran
     elemental logical function lge(string_a, string_b)

      character(len=*),intent(in) :: string_a
      character(len=*),intent(in) :: string_b
```

### **Characteristics**

- **string_a** is default _character_ or an ASCII character.
- **string_b** is the same type and kind as **string_a**
- the result is a default logical

### **Description**

**lge**(3) determines whether one string is lexically greater than
or equal to another string, where the two strings are interpreted as
containing ASCII character codes. If **string_a** and **string_b**
are not the same length, the shorter is compared as if spaces were
appended to it to form a value that has the same length as the longer.

The lexical comparison intrinsics **lge**(3), **lgt**(3), **lle**(3),
and **llt**(3) differ from the corresponding intrinsic operators
_.ge., .gt., .le., and .lt._, in that the latter use the processor's
character ordering (which is not ASCII on some targets), whereas the
former always use the ASCII ordering.

### **Options**

- **string_a**
  : string to be tested

- **string_b**
  : string to compare to **string_a**

### **Result**

Returns _.true._ if string*a == string_b, and *.false.\_ otherwise,
based on the ASCII collating sequence.

If both input arguments are null strings, _.true._ is always returned.

If either string contains a character not in the ASCII character set,
the result is processor dependent.

### **Examples**

Sample program:

```fortran
program demo_lge
implicit none
integer :: i
   print *,'the ASCII collating sequence for printable characters'
   write(*,'(1x,19a)')(char(i),i=32,126) ! ASCII order
   write(*,*) lge('abc','ABC')           ! [T] lowercase is > uppercase
   write(*,*) lge('abc','abc  ')         ! [T] trailing spaces
   ! If both strings are of zero length the result is true
   write(*,*) lge('','')                 ! [T]
   write(*,*) lge('','a')                ! [F] the null string is padded
   write(*,*) lge('a','')                ! [T]
   ! elemental
   write(*,*) lge('abc',['abc','123'])   ! [T T]  scalar and array
   write(*,*) lge(['cba', '123'],'abc')  ! [T F]
   write(*,*) lge(['abc','123'],['cba','123']) ! [F T]  both arrays
end program demo_lge
```

Results:

```text
 >  the ASCII collating sequence for printable characters
 >   !"#$%&'()*+,-./012
 >  3456789:;<=>?@ABCDE
 >  FGHIJKLMNOPQRSTUVWX
 >  YZ[\]^_`abcdefghijk
 >  lmnopqrstuvwxyz{|}~
 >  T
 >  T
 >  T
 >  F
 >  T
 >  T T
 >  T F
 >  F T
```

### **Standard**

FORTRAN 77

### **See Also**

[**lgt**(3)](#lgt),
[**lle**(3)](#lle),
[**llt**(3)](#llt)

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
