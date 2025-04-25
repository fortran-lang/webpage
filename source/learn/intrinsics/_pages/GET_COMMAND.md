(get_command)=
## get_command

### **Name**

**get_command**(3) - \[SYSTEM:COMMAND LINE\] Get the entire command line invocation

### **Synopsis**

```fortran
    call get_command([command] [,length] [,status] [,errmsg])
```

```fortran
     subroutine get_command( command ,length ,status, errmsg )

      character(len=*),intent(out),optional   :: command
      integer(kind=**),intent(out),optional   :: length
      integer(kind=**),intent(out),optional   :: status
      character(len=*),intent(inout),optional :: errmsg
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
  meeting the conditions described herein.
- **command** and **errmsg** are scalar _character_ variables of default kind.
- **length** and **status** are scalar _integer_ with a decimal exponent
  range of at least four.

### **Description**

**get_command**(3) retrieves the entire command line that was used to
invoke the program.

Note that what is typed on the command line is often processed by
a shell. The shell typically processes special characters and white
space before passing it to the program. The processing can typically be
turned off by turning off globbing or quoting the command line arguments
and/or changing the default field separators, but this should rarely
be necessary.

### **Result**

- **command**
  : If **command** is present, the entire command line that was used
  to invoke the program is stored into it. If the command cannot be
  determined, **command** is assigned all blanks.

- **length**
  : If **length** is present, it is assigned the length of the command line.
  It is system-dependent as to whether trailing blanks will be counted.
  : If the command length cannot be determined, a length of 0 is assigned.

- **status**
  : If **status** is present, it is assigned 0 upon success of the
  command, **-1** if **command** is too short to store the command line,
  or a positive value in case of an error.

- **errmsg**
  : It is assigned a processor-dependent explanatory message if the
  command retrieval fails. Otherwise, it is unchanged.

### **Examples**

Sample program:

```fortran
program demo_get_command
implicit none
integer                      :: command_line_length
character(len=:),allocatable :: command_line
   ! get command line length
   call get_command(length=command_line_length)
   ! allocate string big enough to hold command line
   allocate(character(len=command_line_length) :: command_line)
   ! get command line as a string
   call get_command(command=command_line)
   ! trim leading spaces just in case
   command_line=adjustl(command_line)
   write(*,'("OUTPUT:",a)')command_line
end program demo_get_command
```

Results:

```bash
     # note that shell expansion removes some of the whitespace
     # without quotes
     ./test_get_command  arguments    on command   line to   echo

     OUTPUT:./test_get_command arguments on command line to echo

     # using the bash shell with single quotes
     ./test_get_command  'arguments  *><`~[]!{}?"\'| '

     OUTPUT:./test_get_command arguments  *><`~[]!{}?"'|
```

### **Standard**

Fortran 2003

### **See Also**

[**get_command_argument**(3)](#get_command_argument),
[**command_argument_count**(3)](#command_argument_count)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

#
