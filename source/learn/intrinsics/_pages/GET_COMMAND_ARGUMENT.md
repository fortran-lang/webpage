(get_command_argument)=
## get_command_argument

### **Name**

**get_command_argument**(3) - \[SYSTEM:COMMAND LINE\] Get command line arguments

### **Synopsis**

```fortran
  call get_command_argument(number [,value] [,length] &
  & [,status] [,errmsg])
```

```fortran
   subroutine get_command_argument( number, value, length, &
   & status ,errmsg)

    integer(kind=**),intent(in)             :: number
    character(len=*),intent(out),optional   :: value
    integer(kind=**),intent(out),optional   :: length
    integer(kind=**),intent(out),optional   :: status
    character(len=*),intent(inout),optional :: errmsg
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
  meeting the conditions described herein.
- **number**, **length**, and **status** are scalar _integer_
  with a decimal exponent range of at least four.
- **value** and **errmsg** are scalar _character_ variables of default
  kind.

### **Description**

**get_command_argument**(3) retrieves or queries the n-th argument that
was passed on the command line to the current program execution.

There is not anything specifically stated about what an argument is but
in practice the arguments are strings split on whitespace unless the
arguments are quoted. IFS values (Internal Field Separators) used by
common shells are typically ignored and unquoted whitespace is almost
always the separator.

Shells have often expanded command arguments and spell characters before
passing them to the program, so the strings read are often not exactly
what the user typed on the command line.

### **Options**

- **number**
  : is a non-negative number indicating which argument of the current
  program command line is to be retrieved or queried.
  : If **number = 0**, the argument pointed to is set to the name of the
  program (on systems that support this feature).
  : if the processor does not have such a concept as a command name the
  value of command argument 0 is processor dependent.
  : For values from 1 to the number of arguments passed to the program a
  value is returned in an order determined by the processor. Conventionally
  they are returned consecutively as they appear on the command line from
  left to right.

### **Result**

- **value**
  : The **value** argument holds the command line argument.
  If **value** can not hold the argument, it is truncated to fit the
  length of **value**.
  : If there are less than **number** arguments specified at the command
  line or if the argument specified does not exist for other reasons,
  **value** will be filled with blanks.

- **length**
  : The **length** argument contains the length of the n-th command
  line argument. The length of **value** has no effect on this value,
  It is the length required to hold all the significant characters of
  the argument regardless of how much storage is provided by **value**.

- **status**
  : If the argument retrieval fails, **status** is a positive number;
  if **value** contains a truncated command line argument, **status**
  is **-1**; and otherwise the **status** is zero.

### **Examples**

Sample program:

```fortran
program demo_get_command_argument
implicit none
character(len=255)           :: progname
integer                      :: count, i, argument_length, istat
character(len=:),allocatable :: arg

 ! command name assuming it is less than 255 characters in length
  call get_command_argument (0, progname, status=istat)
  if (istat == 0) then
     print *, "The program's name is " // trim (progname)
  else
     print *, "Could not get the program's name " // trim (progname)
  endif

 ! get number of arguments
  count = command_argument_count()
  write(*,*)'The number of arguments is ',count

  !
  ! allocate string array big enough to hold command line
  ! argument strings and related information
  !
  do i=1,count
     call get_command_argument(number=i,length=argument_length)
     if(allocated(arg))deallocate(arg)
     allocate(character(len=argument_length) :: arg)
     call get_command_argument(i, arg,status=istat)
     ! show the results
     write (*,'(i3.3,1x,i0.5,1x,i0.5,1x,"[",a,"]")') &
     & i,istat,argument_length,arg
  enddo

end program demo_get_command_argument
```

Results:

```bash
 ./demo_get_command_argument a  test 'of getting  arguments ' " leading"
```

```text
 The program's name is ./demo_get_command_argument
 The number of arguments is            4
001 00000 00001 [a]
002 00000 00004 [test]
003 00000 00022 [of getting  arguments ]
004 00000 00008 [ leading]
```

### **Standard**

Fortran 2003

### **See Also**

[**get_command**(3)](#get_command),
[**command_argument_count**(3)](#command_argument_count)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

#
