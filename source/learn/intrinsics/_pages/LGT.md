## lgt

### **Name**

**lgt**(3) - \[CHARACTER:COMPARE\] ASCII Lexical greater than

### **Syntax**
```fortran
   elemental logical function lgt(string_a, string_b)

    character(len=*),intent(in) :: string_a
    character(len=*),intent(in) :: string_b
```
### **Description**

  Determines whether one string is lexically greater than another string,
  where the two strings are interpreted as containing ASCII character
  codes. If the String **a** and String **b** are not the same length,
  the shorter is compared as if spaces were appended to it to form a
  value that has the same length as the longer.

  In general, the lexical comparison intrinsics **lge**, **lgt**, **lle**,
  and **llt** differ from the corresponding intrinsic operators _.ge.,
  .gt., .le., and .lt._, in that the latter use the processor's character
  ordering (which is not ASCII on some targets), whereas the former
  always use the ASCII ordering.

### **Arguments**

- **string_a**
  : Shall be of default _character_ type.

- **string_b**
  : Shall be of default _character_ type.

### **Returns**

  Returns _.true._ if string_a \> string_b, and _.false._ otherwise,
  based on the ASCII ordering.

  If both input arguments are null strings, _.false._ is always returned.

### **Examples**

Sample program:

```fortran
program demo_lgt
implicit none
integer :: i
   write(*,'(*(a))')(char(i),i=32,126)  ! ASCII order
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
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ
    [\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    T
    F
    F
    F
    T
    F T
    T F
    F F
```
### **Standard**

FORTRAN 77 and later

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

 _fortran-lang intrinsic descriptions \@urbanjost_
