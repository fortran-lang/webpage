## command_argument_count

### **Name**

**command_argument_count**(3) - \[SYSTEM:COMMAND LINE\] Get number of command line arguments

### **Syntax**

```fortran
    result = command_argument_count()

     integer function command_argument_count() result(count)
     integer :: count
```

### **Description**

**command_argument_count()** returns the number of arguments passed
on the command line when the containing program was invoked.

### **Arguments**

None

### **Returns**

- **count**
  : The return value is of type default _integer_. It is the number of
  arguments passed on the command line when the program was invoked.

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

Fortran 2003 and later

### **See Also**

[**get_command**(3)](GET_COMMAND),
[**get_command_argument**(3)](GET_COMMAND_ARGUMENT)

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
