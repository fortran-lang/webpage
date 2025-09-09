(char)=
## char

### **Name**

**char**(3) - \[CHARACTER\] Generate a character from a code value

### **Synopsis**

```fortran
    result = char(i [,kind])
```

```fortran
     elemental character(kind=KIND) function char(i,KIND)

      integer(kind=**),intent(in) :: i
      integer(kind=**),intent(in),optional :: KIND
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
- **i** is an _integer_ of any kind
- **kind** is an _integer_ initialization expression indicating the kind
  parameter of the result.
- The returned value is a character with the kind specified by **kind**
  or if **kind** is not present, the default _character_ kind.

### **Description**

Generates a _character_ value given a numeric code representing the
position **i** in the collating sequence associated with the specified
kind **kind**.

Note that **achar**(3) is a similar function specifically for ASCII
characters that is preferred when only ASCII is being processed,
which is equivalent to **char(i,kind=selected_char_kind("ascii") )**

The **ichar**(3) function is the reverse of **char**(3), converting
characters to their collating sequence value.

<!--
   ICHAR (CHAR (I, KIND (C))) shall have the value I for 0 <= I <= n - 1 and
  CHAR (ICHAR (C), KIND (C)) shall have the value C for any character C capable of representation in the
  processor.
-->

### **Options**

- **i**
  : a value in the range **0 <= I <= n-1**, where **n** is the number of characters
  in the collating sequence associated with the specified kind type parameter.
  : For ASCII, **n** is 127. The default character set may or may not allow higher
  values.

- **kind**
  : A constant _integer_ initialization expression indicating the kind
  parameter of the result. If not present, the default kind is assumed.

### **Result**

The return value is a single _character_ of the specified kind, determined by the
position of **i** in the collating sequence associated with the specified **kind**.

### **Examples**

Sample program:

```fortran
program demo_char
implicit none
integer, parameter :: ascii =  selected_char_kind ("ascii")
character(len=1, kind=ascii ) :: c
integer :: i
  ! basic
   i=74
   c=char(i)
   write(*,*)'ASCII character ',i,'is ',c
  !
   print *, 'a selection of ASCII characters (shows hex if not printable)'
   do i=0,127,10
      c = char(i,kind=ascii)
      select case(i)
      case(32:126)
         write(*,'(i3,1x,a)')i,c
      case(0:31,127)
         ! print hexadecimal value for unprintable characters
         write(*,'(i3,1x,z2.2)')i,c
      case default
         write(*,'(i3,1x,a,1x,a)')i,c,'non-standard ASCII'
      end select
   enddo

end program demo_char
```

Results:

```text
    ASCII character           74 is J
    a selection of ASCII characters (shows hex if not printable)
     0 00
    10 0A
    20 14
    30 1E
    40 (
    50 2
    60 <
    70 F
    80 P
    90 Z
   100 d
   110 n
   120 x
```

### **Standard**

FORTRAN 77

### **See Also**

[**achar**(3)](#achar),
[**iachar**(3)](#iachar),
[**ichar**(3)](#ichar)

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
