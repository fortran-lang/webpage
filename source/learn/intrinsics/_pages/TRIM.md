(trim)=
## trim

### **Name**

**trim**(3) - \[CHARACTER:WHITESPACE\] Remove trailing blank characters from a string

### **Synopsis**

```fortran
    result = trim(string)
```

```fortran
     character(len=:,kind=KIND) function trim(string)

      character(len=*,kind=KIND),intent(in) :: string
```

### **Characteristics**

- **KIND** can be any kind supported for the _character_ type.
- The result has the same type and kind as the input argument **string**.

### **Description**

**trim**(3) removes trailing blank characters from a string.

### **Options**

- **string**
  : A string to trim

### **Result**

The result is the same as **string** except trailing blanks are removed.

If **string** is composed entirely of blanks or has zero length,
the result has zero length.

### **Examples**

Sample program:

```fortran
program demo_trim
implicit none
character(len=:), allocatable :: str, strs(:)
character(len=*),parameter :: brackets='( *("[",a,"]":,1x) )'
integer :: i

   str='   trailing    '
   print brackets, str,trim(str) ! trims it

   str='   leading'
   print brackets, str,trim(str) ! no effect

   str='            '
   print brackets, str,trim(str) ! becomes zero length
   print *,  len(str), len(trim('               '))

  ! array elements are all the same length, so you often
  ! want to print them
   strs=[character(len=10) :: "Z"," a b c","ABC",""]

   write(*,*)'untrimmed:'
   ! everything prints as ten characters; nice for neat columns
   print brackets, (strs(i), i=1,size(strs))
   print brackets, (strs(i), i=size(strs),1,-1)
   write(*,*)'trimmed:'
   ! everything prints trimmed
   print brackets, (trim(strs(i)), i=1,size(strs))
   print brackets, (trim(strs(i)), i=size(strs),1,-1)

end program demo_trim
```

Results:

```text
    > [   trailing    ] [   trailing]
    > [   leading] [   leading]
    > [            ] []
    >           12           0
    >  untrimmed:
    > [Z         ] [ a b c    ] [ABC       ] [          ]
    > [          ] [ABC       ] [ a b c    ] [Z         ]
    >  trimmed:
    > [Z] [ a b c] [ABC] []
    > [] [ABC] [ a b c] [Z]
```

### **Standard**

Fortran 95

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
