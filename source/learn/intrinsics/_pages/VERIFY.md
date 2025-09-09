(verify)=
## verify

### **Name**

**verify**(3) - \[CHARACTER:SEARCH\] Position of a character in a string
of characters that does not appear in a given set of characters.

### **Synopsis**

```fortran
    result = verify(string, set [,back] [,kind] )
```

```fortran
     elemental integer(kind=KIND) function verify(string,set,back,KIND)

      character(len=*,kind=**),intent(in) :: string
      character(len=*,kind=**),intent(in) :: set
      logical,intent(in),optional :: back
      integer,intent(in),optional :: KIND
```

### **Characteristics**

- **string** and **set** must be of type _character_ and have the same kind for any
  individual call, but that can be any supported _character_ kind.
- **KIND** must be a constant _integer_ initialization expression and a
  valid kind for the _integer_ type.
- **back** shall be of type logical.
- the kind of the returned value is the same as **kind** if
  present. Otherwise a default _integer_ kind is returned.

### **Description**

**verify**(3) verifies that all the characters in **string** belong
to the set of characters in **set** by identifying the position of
the first character in the string that is not in the set.

This makes it easy to verify strings are all uppercase or lowercase,
follow a basic syntax, only contain printable characters, and many
of the conditions tested for with the C routines **isalnum**(3c),
**isalpha**(3c), **isascii**(3c), **isblank**(3c), **iscntrl**(3c),
**isdigit**(3c), **isgraph**(3c), **islower**(3c), **isprint**(3c),
**ispunct**(3c), **isspace**(3c), **isupper**(3c), and **isxdigit**(3c);
but for a string as well as an array of strings.

### **Options**

- **string**
  : The string to search in for an unmatched character.

- **set**
  : The set of characters that must be matched.

- **back**
  : The direction to look for an unmatched character. The left-most
  unmatched character position is returned unless **back** is present
  and _.false._, which causes the position of the right-most unmatched
  character to be returned instead of the left-most unmatched character.

- **kind**
  : An _integer_ initialization expression indicating the kind
  parameter of the result.

### **Result**

If all characters of **string** are found in **set**, the result is zero.

If **string** is of zero length a zero (0) is always returned.

Otherwise, if an unmatched character is found
The position of the first or last (if **back** is _.false._) unmatched
character in **string** is returned, starting with position one on the
left end of the string.

### **Examples**

#### Sample program I:

```fortran
program demo_verify
implicit none
! some useful character sets
character,parameter :: &
 & int*(*)   = '1234567890', &
 & low*(*)   = 'abcdefghijklmnopqrstuvwxyz', &
 & upp*(*)   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', &
 & punc*(*)  = "!""#$%&'()*+,-./:;<=>?@[\]^_`{|}~", &
 & blank*(*) = ' ', &
 & tab       = char(11), &
 & prnt*(*) = int//low//upp//blank//punc

character(len=:),allocatable :: string
integer :: i
    print *, 'basics:'
    print *, VERIFY ('ABBA', 'A')                ! has the value 2.
    print *, VERIFY ('ABBA', 'A', BACK = .TRUE.) ! has the value 3.
    print *, VERIFY ('ABBA', 'AB')               ! has the value 0.

   print *,'find first non-uppercase letter'
   ! will produce the location of "d", because there is no match in UPP
   write(*,*) 'something unmatched',verify("ABCdEFG", upp)

   print *,'if everything is matched return zero'
   ! will produce 0 as all letters have a match
   write(*,*) 'everything matched',verify("ffoorrttrraann", "nartrof")

   print *,'easily categorize strings as uppercase, lowercase, ...'
   ! easy C-like functionality but does entire strings not just characters
   write(*,*)'isdigit 123?',verify("123", int) == 0
   write(*,*)'islower abc?',verify("abc", low) == 0
   write(*,*)'isalpha aBc?',verify("aBc", low//upp) == 0
   write(*,*)'isblank aBc dEf?',verify("aBc dEf", blank//tab ) /= 0
   ! check if all printable characters
   string="aB;cde,fgHI!Jklmno PQRSTU vwxyz"
   write(*,*)'isprint?',verify(string,prnt) == 0
   ! this now has a nonprintable tab character in it
   string(10:10)=char(11)
   write(*,*)'isprint?',verify(string,prnt) == 0

   print *,'VERIFY(3) is very powerful using expressions as masks'
   ! verify(3f) is often used in a logical expression
   string=" This is NOT all UPPERCASE "
   write(*,*)'all uppercase/spaces?',verify(string, blank//upp) == 0
   string=" This IS all uppercase "
   write(*,*) 'string=['//string//']'
   write(*,*)'all uppercase/spaces?',verify(string, blank//upp) == 0

  ! set and show complex string to be tested
   string='  Check this out. Let me know  '
   ! show the string being examined
   write(*,*) 'string=['//string//']'
   write(*,*) '        '//repeat(int,4) ! number line

   ! the Fortran functions returns a position just not a logical like C
   print *, 'returning a position not just a logical is useful'
   ! which can be very useful for parsing strings
   write(*,*)'first non-blank character',verify(string, blank)
   write(*,*)'last non-blank character',verify(string, blank,back=.true.)
   write(*,*)'first non-letter non-blank',verify(string,low//upp//blank)

  !VERIFY(3) is elemental so you can check an array of strings in one call
  print *, 'elemental'
   ! are strings all letters (or blanks)?
   write(*,*) 'array of strings',verify( &
   ! strings must all be same length, so force to length 10
   & [character(len=10) :: "YES","ok","000","good one","Nope!"], &
   & low//upp//blank) == 0

   ! rarer, but the set can be an array, not just the strings to test
   ! you could do ISPRINT() this (harder) way :>
   write(*,*)'isprint?',.not.all(verify("aBc", [(char(i),i=32,126)])==1)
   ! instead of this way
   write(*,*)'isprint?',verify("aBc",prnt) == 0

end program demo_verify
```

Results:

```text
 >  basics:
 >            2
 >            3
 >            0
 >  find first non-uppercase letter
 >  something unmatched           4
 >  if everything is matched return zero
 >  everything matched           0
 >  easily categorize strings as uppercase, lowercase, ...
 >  isdigit 123? T
 >  islower abc? T
 >  isalpha aBc? T
 >  isblank aBc dEf? T
 >  isprint? T
 >  isprint? F
 >  VERIFY(3) is very powerful using expressions as masks
 >  all uppercase/spaces? F
 >  string=[ This IS all uppercase ]
 >  all uppercase/spaces? F
 >  string=[  Check this out. Let me know  ]
 >          1234567890123456789012345678901234567890
 >  returning a position not just a logical is useful
 >  first non-blank character           3
 >  last non-blank character          29
 >  first non-letter non-blank          17
 >  elemental
 >  array of strings T T F T F
 >  isprint? T
 >  isprint? T
```

#### Sample program II:

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
   ! show the strings to test
   write(*,'("|",*(g0,"|"))') ints
   ! show if strings pass or fail the test done by isint(3f)
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
   if( name == '' )return
   ! allow one leading sign
   if( verify(name(1:1),'+-') == 0 ) name=name(2:)
   ! was just a sign
   if( name == '' )return
   lout=verify(trim(name), digits)  == 0
end function isint

end program fortran_ints
```

Results:

```text
|+1       |3044848  |30.40    |September|1 2 3    |  -3000  |         |
| T       | T       | F       | F       | F       | T       | F       |
```

#### Sample program III:

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

#### Sample program IV:

check if string is of form NN-HHHHH

```fortran
program checkform
! check if string is of form NN-HHHHH
implicit none
character(len=*),parameter :: int='1234567890'
character(len=*),parameter :: hex='abcdefABCDEF0123456789'
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
   else
      write(*,*)trim(chars),' failed'
   endif
end program checkform
```

Results:

```text
    32-af43d passed
```

#### Sample program V:

exploring uses of elemental functionality and dusty corners

```fortran
program more_verify
implicit none
character(len=*),parameter :: &
  & int='0123456789', &
  & low='abcdefghijklmnopqrstuvwxyz', &
  & upp='ABCDEFGHIJKLMNOPQRSTUVWXYZ', &
  & blank=' '
! note character variables in an array have to be of the same length
character(len=6) :: strings(3)=["Go    ","right ","home! "]
character(len=2) :: sets(3)=["do","re","me"]

  ! elemental -- you can use arrays for both strings and for sets

   ! check each string from right to left for non-letter/non-blank
   write(*,*)'last non-letter',verify(strings,upp//low//blank,back=.true.)

   ! even BACK can be an array
   ! find last non-uppercase character in "Howdy "
   ! and first non-lowercase in "there "
   write(*,*) verify(strings(1:2),[upp,low],back=[.true.,.false.])

   ! using a null string for a set is not well defined. Avoid it
   write(*,*) 'null',verify("for tran ", "", .true.) ! 8,length of string?
   ! probably what you expected
   write(*,*) 'blank',verify("for tran ", " ", .true.) ! 7,found 'n'

   ! first character in  "Go    " not in "do",
   ! and first letter in "right " not in "ri"
   ! and first letter in "home! " not in "me"
   write(*,*) verify(strings,sets)

end program more_verify
```

Results:

```text
    > last non-letter 0 0 5
    > 6 6
    > null 9
    > blank 8
    > 1 2 1
```

### **Standard**

Fortran 95 , with **kind** argument - Fortran 2003

### **See Also**

Functions that perform operations on character strings, return lengths
of arguments, and search for certain arguments:

- **Elemental:**
  [**adjustl**(3)](#adjustl),
  [**adjustr**(3)](#adjustr),
  [**index**(3)](#index),
  [**scan**(3)](#scan),

- **Nonelemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat),
  [**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
