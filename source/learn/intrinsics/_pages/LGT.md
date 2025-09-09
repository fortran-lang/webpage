(lgt)=
## lgt

### **Name**

**lgt**(3) - \[CHARACTER:COMPARE\] ASCII Lexical greater than

### **Synopsis**

```fortran
     result = lgt(string_a, string_b)
```

```fortran
      elemental logical function lgt(string_a, string_b)

       character(len=*),intent(in) :: string_a
       character(len=*),intent(in) :: string_b
```

### **Characteristics**

- **string_a** is default _character_ or an ASCII character.
- **string_b** is the same type and kind as **string_a**
- the result is a default logical

### **Description**

**lgt**(3) determines whether one string is lexically greater than
another string, where the two strings are interpreted as containing
ASCII character codes. If the String **a** and String **b** are not
the same length, the shorter is compared as if spaces were appended
to it to form a value that has the same length as the longer.

In general, the lexical comparison intrinsics **lge**, **lgt**, **lle**,
and **llt** differ from the corresponding intrinsic operators _.ge.,
.gt., .le., and .lt._, in that the latter use the processor's character
ordering (which is not ASCII on some targets), whereas the former
always use the ASCII ordering.

### **Options**

- **string_a**
  : string to be tested

- **string_b**
  : string to compare to **string_a**

### **Result**

Returns _.true._ if string*a \> string_b, and *.false.\_ otherwise,
based on the ASCII ordering.

If both input arguments are null strings, _.false._ is returned.

If either string contains a character not in the ASCII character set,
the result is processor dependent.

### **Examples**

Sample program:

```fortran
program demo_lgt
implicit none
integer :: i
   print *,'the ASCII collating sequence for printable characters'
   write(*,'(1x,19a)')(char(i),i=32,126)

   write(*,*) lgt('abc','ABC')          ! [T] lowercase is > uppercase
   write(*,*) lgt('abc','abc  ')        ! [F] trailing spaces

   ! If both strings are of zero length the result is false.
   write(*,*) lgt('','')                ! [F]
   write(*,*) lgt('','a')               ! [F] the null string is padded
   write(*,*) lgt('a','')               ! [T]
   write(*,*) lgt('abc',['abc','123'])  ! [F T]  scalar and array
   write(*,*) lgt(['cba', '123'],'abc') ! [T F]
   write(*,*) lgt(['abc','123'],['cba','123']) ! [F F]  both arrays
end program demo_lgt
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
 >  F
 >  F
 >  F
 >  T
 >  F T
 >  T F
 >  F F
```

### **Standard**

FORTRAN 77

### **See Also**

[**lge**(3)](#lge),
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
