## lle

### **Name**

**lle**(3) - \[CHARACTER:COMPARE\] ASCII Lexical less than or equal

### **Syntax**

```fortran
   elemental logical function lle(string_a, string_b)

    character(len=*),intent(in) :: string_a
    character(len=*),intent(in) :: string_b
```
### **Description**

  Determines whether one string is lexically less than or equal to
  another string, where the two strings are interpreted as containing
  ASCII character codes. if the **string_a** and **string_b** are not
  the same length, the shorter is compared as if spaces were appended
  to it to form a value that has the same length as the longer. Leading
  spaces are significant.

  In general, the lexical comparison intrinsics **lge**, **lgt**, **lle**,
  and **llt** differ from the corresponding intrinsic operators _.ge.,
  .gt., .le., and .lt._, in that the latter use the processor's character
  ordering (which is not ASCII on some targets), whereas the former
  always use the ASCII ordering.

### **Arguments**

- **str_a**
  : variable or array of default _character_ type.

- **str_b**
  : variable or array of default _character_ type.

  if **str_a** and **str_b** are both arrays they must be of the
  same shape.

### **Returns**

- **result**
  Returns _.true._ if **STR_A \<= STR_B**, and _.false._ otherwise, based on
  the ASCII ordering.

  If both input arguments are null strings, _.true._ is always returned.

### **Examples**

Sample program:

```fortran
program demo_lle
implicit none
integer :: i
   write(*,'(*(a))')(char(i),i=32,126)
   write(*,*) lle('abc','ABC')          ! F lowercase is > uppercase
   write(*,*) lle('abc','abc  ')        ! T trailing spaces
   ! If both strings are of zero length the result is true.
   write(*,*) lle('','')                ! T
   write(*,*) lle('','a')               ! T the null string is padded
   write(*,*) lle('a','')               ! F
   write(*,*) lle('abc',['abc','123'])  ! [T,F] scalar and array
   write(*,*) lle(['cba', '123'],'abc') ! [F,T]
   write(*,*) lle(['abc','123'],['cba','123']) ! [T,T] both arrays
end program demo_lle
```
Results:

```text
  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ
  [\]^_`abcdefghijklmnopqrstuvwxyz{|}~
  F
  T
  T
  T
  F
  T F
  F T
  T T
```

### **Standard**

FORTRAN 77 and later

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

 _fortran-lang intrinsic descriptions \@urbanjost_
