(llt)=
## llt

### **Name**

**llt**(3) - \[CHARACTER:COMPARE\] ASCII Lexical less than

### **Synopsis**

```fortran
     result = llt(string_a, stringb)
```

```fortran
      elemental logical function llt(string_a, string_b)

       character(len=*),intent(in) :: string_a
       character(len=*),intent(in) :: string_b
```

### **Characteristics**

- **string_a** is default _character_ or an ASCII character.
- **string_b** is the same type and kind as **string_a**
- the result is a default logical

### **Description**

**llt**(3) determines whether one string is lexically less than
another string, where the two strings are interpreted as containing
ASCII character codes. If the **string_a** and **string_b** are not
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

Returns _.true._ if string*a \<= string_b, and *.false.\_ otherwise,
based on the ASCII collating sequence.

If both input arguments are null strings, _.false._ is always returned.

If either string contains a character not in the ASCII character set,
the result is processor dependent.

### **Examples**

Sample program:

```fortran
program demo_llt
implicit none
integer :: i

   print *,'the ASCII collating sequence for printable characters'
   write(*,'(1x,19a)')(char(i),i=32,126) ! ASCII order

  ! basics
   print *,'case matters'
   write(*,*) llt('abc','ABC')           ! [F] lowercase is > uppercase
   write(*,*) llt('abc','abc  ')         ! [F] trailing spaces
   ! If both strings are of zero length the result is false.
   write(*,*) llt('','')                 ! [F]
   write(*,*) llt('','a')                ! [T] the null string is padded
   write(*,*) llt('a','')                ! [F]
   print *,'elemental'
   write(*,*) llt('abc',['abc','123'])   ! [F F]  scalar and array
   write(*,*) llt(['cba', '123'],'abc')  ! [F T]
   write(*,*) llt(['abc','123'],['cba','123']) ! [T F]  both arrays
end program demo_llt
```

Results:

```text
 >  the ASCII collating sequence for printable characters
 >   !"#$%&'()*+,-./012
 >  3456789:;<=>?@ABCDE
 >  FGHIJKLMNOPQRSTUVWX
 >  YZ[\]^_`abcdefghijk
 >  lmnopqrstuvwxyz{|}~
 >  case matters
 >  F
 >  F
 >  F
 >  T
 >  F
 >  elemental
 >  F F
 >  F T
 >  T F
```

### **Standard**

FORTRAN 77

### **See Also**

[**lge**(3)](#lge),
[**lgt**(3)](#lgt),
[**lle**(3)](#lle))

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl), [**adjustr**(3)](#adjustr), [**index**(3)](#index),
  [**scan**(3)](#scan), [**verify**(3)](#verify)

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat), [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
