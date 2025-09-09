(command_argument_count)=
## command_argument_count

### **Name**

**command_argument_count**(3) - \[SYSTEM:COMMAND LINE\] Get number of command line arguments

### **Synopsis**

```fortran
    result = command_argument_count()
```

```fortran
     integer function command_argument_count()
```

### **Characteristics**

- the result is of default integer scalar.

### **Description**

**command_argument_count**(3) returns the number of arguments passed
on the command line when the containing program was invoked.

### **Options**

None

### **Result**

: The return value is of type default _integer_. It is the number of
arguments passed on the command line when the program was invoked.

If there are no command arguments available or if the processor does
not support command arguments, then the result has the value zero.

If the processor has a concept of a command name, the command name
does not count as one of the command arguments.

### **Examples**

Sample program:

```fortran
program demo_command_argument_count
implicit none
integer :: count
   count = command_argument_count()
   print *, count
end program demo_command_argument_count
```

Sample output:

```bash
   # the command verb does not count
   ./test_command_argument_count
       0
   # quoted strings may count as one argument
   ./test_command_argument_count count arguments
       2
   ./test_command_argument_count 'count arguments'
       1
```

### **Standard**

Fortran 2003

### **See Also**

[**get_command**(3)](#get_command),
[**get_command_argument**(3)](#get_command_argument)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
