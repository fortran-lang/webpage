(adjustl)=
## adjustl

### **Name**

**adjustl**(3) - \[CHARACTER:WHITESPACE\] Left-justified a string

### **Synopsis**

```fortran
  result = adjustl(string)
```

```fortran
   elemental character(len=len(string),kind=KIND) function adjustl(string)

    character(len=*,kind=KIND),intent(in) :: string
```

### **Characteristics**

- **string** is a _character_ variable of any supported kind
- The return value is a _character_ variable of the same kind
  and length as **string**

### **Description**

**adjustl**(3) will left-justify a string by removing leading
spaces. Spaces are inserted at the end of the string as needed.

### **Options**

- **string**
  : the string to left-justify

### **Result**

A copy of **string** where leading spaces are removed and the same
number of spaces are inserted on the end of **string**.

### **Examples**

Sample program:

```fortran
program demo_adjustl
implicit none
character(len=20) :: str = '   sample string'
character(len=:),allocatable :: astr
integer :: length

   ! basic use
    write(*,'(a,"[",a,"]")') 'original: ',str
    str=adjustl(str)
    write(*,'(a,"[",a,"]")') 'adjusted: ',str

    ! a fixed-length string can be printed
    ! trimmed using trim(3f) or len_trim(3f)
    write(*,'(a,"[",a,"]")') 'trimmed:  ',trim(str)
    length=len_trim(str)
    write(*,'(a,"[",a,"]")') 'substring:',str(:length)

    ! note an allocatable string stays the same length too
    ! and is not trimmed by just an adjustl(3f) call.
    astr='    allocatable string   '
    write(*,'(a,"[",a,"]")') 'original:',astr
    astr = adjustl(astr)
    write(*,'(a,"[",a,"]")') 'adjusted:',astr
    ! trim(3f) can be used to change the length
    astr = trim(astr)
    write(*,'(a,"[",a,"]")') 'trimmed: ',astr

end program demo_adjustl
```

Results:

```text
   original: [   sample string    ]
   adjusted: [sample string       ]
   trimmed:  [sample string]
   substring:[sample string]
   original:[    allocatable string   ]
   adjusted:[allocatable string       ]
   trimmed: [allocatable string]
```

### **Standard**

Fortran 95

### **See Also**

[**adjustr**(3)](#adjustr),
[**trim**(3)](#trim)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
