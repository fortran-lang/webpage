(lle)=
## lle

### **Name**

**lle**(3) - \[CHARACTER:COMPARE\] ASCII Lexical less than or equal

### **Synopsis**

```fortran
     result = lle(string_a, stringb)
```

```fortran
      elemental logical function lle(string_a, string_b)

       character(len=*),intent(in) :: string_a
       character(len=*),intent(in) :: string_b
```

### **Characteristics**

- **string_a** is default _character_ or an ASCII character.
- **string_b** is the same type and kind as **string_a**
- the result is a default logical

### **Description**

**lle**(3) determines whether one string is lexically less than or equal
to another string, where the two strings are interpreted as containing
ASCII character codes.

If **string_a** and **string_b** are not the
same length, the shorter is compared as if spaces were appended to it
to form a value that has the same length as the longer.

Leading spaces are significant.

In general, the lexical comparison intrinsics **lge**, **lgt**, **lle**,
and **llt** differ from the corresponding intrinsic operators _.ge.,
.gt., .le., and .lt._, in that the latter use the processor's character
ordering (which is not ASCII on some targets), whereas **lle**(3)
always uses the ASCII ordering.

### **Options**

- **string_a**
  : string to be tested

- **string_b**
  : string to compare to **string_a**

### **Result**

- **result**
  Returns _.true._ if **string_a \<= string_b**, and _.false._ otherwise,
  based on the ASCII collating sequence.

  If both input arguments are null strings, _.true._ is always returned.

  If either string contains a character not in the ASCII character set,
  the result is processor dependent.

### **Examples**

Sample program:

```fortran
program demo_lle
implicit none
integer :: i
   print *,'the ASCII collating sequence for printable characters'
   write(*,'(1x,19a)')(char(i),i=32,126)
  ! basics

   print *,'case matters'
   write(*,*) lle('abc','ABC')          ! F lowercase is > uppercase

   print *,'a space is the lowest printable character'
   write(*,*) lle('abcd','abc')         ! F  d > space
   write(*,*) lle('abc','abcd')         ! T  space < d

   print *,'leading spaces matter, trailing spaces do not'
   write(*,*) lle('abc','abc  ')        ! T trailing spaces
   write(*,*) lle('abc',' abc')         ! F leading spaces are significant

   print *,'even null strings are padded and compared'
   ! If both strings are of zero length the result is true.
   write(*,*) lle('','')                ! T
   write(*,*) lle('','a')               ! T the null string is padded
   write(*,*) lle('a','')               ! F
   print *,'elemental'
   write(*,*) lle('abc',['abc','123'])  ! [T,F] scalar and array
   write(*,*) lle(['cba', '123'],'abc') ! [F,T]
   ! per the rules for elemental procedures arrays must be the same size
   write(*,*) lle(['abc','123'],['cba','123']) ! [T,T] both arrays
end program demo_lle
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
 >  a space is the lowest printable character
 >  F
 >  T
 >  leading spaces matter, trailing spaces do not
 >  T
 >  F
 >  even null strings are padded and compared
 >  T
 >  T
 >  F
 >  elemental
 >  T F
 >  F T
 >  T T
```

### **Standard**

FORTRAN 77

### **See Also**

[**lge**(3)](#lge),
[**lgt**(3)](#lgt),
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
