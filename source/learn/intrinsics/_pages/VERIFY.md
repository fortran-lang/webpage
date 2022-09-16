## verify

### **Name**

**verify**(3) - \[CHARACTER:SEARCH\] Scan a string for the absence of a set of characters

### **Syntax**

```fortran
result = verify(string, set, back, kind)

  integer(kind=KIND) elemental function verify(string,set,back,kind)

   character(len=*),intent(in) :: string
   character(len=*),intent(in) :: set
   logical,intent(in),optional :: back
   integer,intent(in),optional :: KIND
```

### **Description**

Verifies that all the characters in **string** belong to the set of
characters in **set** by identifying the first character in the string(s)
that is not in the set(s).

If **back** is either absent or equals **.false.**, this function
returns the position of the leftmost character of **string** that is
not in **set**.

If **back** equals **.true.**, the rightmost position is returned.

If all characters of **string** are found in **set**, the result is zero.

This makes it easy to verify strings are all uppercase or lowercase,
follow a basic syntax, only contain printable characters, and many of the
conditions tested for with the C routines
**isalnum**(3c), **isalpha**(3c), **isascii**(3c), **isblank**(3c),
**iscntrl**(3c), **isdigit**(3c), **isgraph**(3c), **islower**(3c),
**isprint**(3c), **ispunct**(3c), **isspace**(3c), **isupper**(3c),
and **isxdigit**(3c); but for a string as well an an array of characters.

### **Arguments**

- **string**
  : Shall be of type _character_.

- **set**
  : Shall be of type _character_.

- **back**
  : shall be of type _logical_.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Returns**

The return value is of type _integer_ and of kind **kind**. If **kind**
is absent, the return value is of default integer kind.

### **Examples**

Sample program I:

```fortran
program demo_verify
implicit none
character(len=*),parameter :: int='0123456789'
character(len=*),parameter :: hex='abcdef0123456789'
character(len=*),parameter :: low='abcdefghijklmnopqrstuvwxyz'
character(len=*),parameter :: upp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
character(len=20):: string='   Howdy There!'
character(len=6) :: strings(2)=["Howdy ","there!"]
character(len=2) :: sets(2)=["de","gh"]

   write(*,*)'first non-blank character ',verify(string, ' ')
   ! NOTE: same as len_trim(3)
   write(*,*)'last non-blank character',verify(string, ' ',back=.true.)

   ! first non-lowercase non-blank character
   write(*,*) verify(string,low//' ')

   !! elemental -- using arrays for both strings and for sets

   ! first character in "Howdy" not in "de", and first letter in "there!"
   ! not in "gh"
   write(*,*) verify(strings,sets)

   ! check each string from right to left for non-letter
   write(*,*) 'last non-letter',verify(strings,upp//low,back=.true.)

   ! note character variables in an array have to be of same length
   ! find last non-uppercase character in "Howdy"
   ! and first non-lowercase in "There!"
   write(*,*) verify(strings,[upp,low],back=[.true.,.false.])

   write(*,*) verify("fortran", "", .true.)  ! 7, found 'n'
   ! 0' found none unmatched
   write(*,*) verify("fortran", "nartrof")


    !! CHECK IF STRING IS OF FORM NN-HHHHH
    CHECK : block
       logical                    :: lout
       character(len=80)          :: chars

       chars='32-af43d'
       lout=.true.

       ! are the first two characters integer characters?
       lout = lout.and.(verify(chars(1:2), int) == 0)

       ! is the third character a dash?
       lout = lout.and.(verify(chars(3:3), '-') == 0)

       ! is remaining string a valid representation of a hex value?
       lout = lout.and.(verify(chars(4:8), hex) == 0)

       if(lout)then
          write(*,*)trim(chars),' passed'
       endif

    endblock CHECK
end program demo_verify
```

Results:

```text
    first non-blank character            4
    last non-blank character          15
              4
              1           1
    last non-letter           6           6
              6           6
              7
              0
    32-af43d passed
```

Sample program II:

Determine if strings are valid integer representations

```fortran
program fortran_ints
implicit none
integer :: i
character(len=*),parameter :: ints(*)=[character(len=10) :: &
 '+1 ', &
 '3044848 ', &
 '30.40 ', &
 'September ', &
 '1 2 3', &
 '  -3000 ', &
 ' ']

   write(*,'("|",*(g0,"|"))') ints
   write(*,'("|",*(1x,l1,8x,"|"))') isint(ints)

contains

elemental function isint(line) result (lout)
!
! determine if string is a valid integer representation
! ignoring trailing spaces and leading spaces
!
character(len=*),parameter   :: digits='0123456789'
character(len=*),intent(in)  :: line
character(len=:),allocatable :: name
logical                      :: lout
   lout=.false.
   ! make sure at least two characters long to simplify tests
   name=adjustl(line)//'  '
   ! blank string
   if( name .eq. '' )return
   ! allow one leading sign
   if( verify(name(1:1),'+-') == 0 ) name=name(2:)
   ! was just a sign
   if( name .eq. '' )return
   lout=verify(trim(name), digits)  == 0
end function isint

end program fortran_ints
```

Results:

```text
|+1       |3044848  |30.40    |September|1 2 3    |  -3000  |         |
| T       | T       | F       | F       | F       | T       | F       |
```

Sample program III:

Determine if strings represent valid Fortran symbol names

```fortran
program fortran_symbol_name
implicit none
integer :: i
character(len=*),parameter :: symbols(*)=[character(len=10) :: &
 'A_ ', &
 '10 ', &
 'September ', &
 'A B', &
 '_A ', &
 ' ']

   write(*,'("|",*(g0,"|"))') symbols
   write(*,'("|",*(1x,l1,8x,"|"))') fortran_name(symbols)

contains

elemental function fortran_name(line) result (lout)
!
! determine if a string is a valid Fortran name
! ignoring trailing spaces (but not leading spaces)
!
character(len=*),parameter   :: int='0123456789'
character(len=*),parameter   :: lower='abcdefghijklmnopqrstuvwxyz'
character(len=*),parameter   :: upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
character(len=*),parameter   :: allowed=upper//lower//int//'_'

character(len=*),intent(in)  :: line
character(len=:),allocatable :: name
logical                      :: lout
   name=trim(line)
   if(len(name).ne.0)then
      ! first character is alphameric
      lout = verify(name(1:1), lower//upper) == 0  &
       ! other characters are allowed in a symbol name
       & .and. verify(name,allowed) == 0           &
       ! allowable length
       & .and. len(name) <= 63
   else
      lout = .false.
   endif
end function fortran_name

end program fortran_symbol_name
```

Results:

```text
|A_        |10        |September |A B       |_A        |          |
| T        | F        | T        | F        | F        | F        |
```

### **Standard**

Fortran 95 and later, with **kind** argument - Fortran 2003 and later

### **See Also**

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
