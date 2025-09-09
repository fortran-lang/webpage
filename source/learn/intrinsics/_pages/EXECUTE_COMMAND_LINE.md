(execute_command_line)=
## execute_command_line

### **Name**

**execute_command_line**(3) - \[SYSTEM:PROCESSES\] Execute a shell command

### **Synopsis**

```fortran
    call execute_command_line( &
    & command [,wait] [,exitstat] [,cmdstat] [,cmdmsg] )
```

```fortran
     subroutine execute_command_line(command,wait,exitstat,cmdstat,cmdmsg)

      character(len=*),intent(in)             :: command
      logical,intent(in),optional             :: wait
      integer,intent(inout),optional          :: exitstat
      integer,intent(inout),optional          :: cmdstat
      character(len=*),intent(inout),optional :: cmdmsg
```

### **Characteristics**

- **command** is a default _character_ scalar
- **wait** is a default _logical_ scalar. If **wait** is present with the
- **exitstat** is an _integer_ of the default kind.
  It must be of a kind with at least a decimal exponent range of 9.
- **cmdstat** is an _integer_ of default kind
  The kind of the variable must support at least a decimal exponent range of four.

- **cmdmsg** is a _character_ scalar of the default kind.

### **Description**

For **execute_command_line**(3) the **command** argument is passed
to the shell and executed. (The shell is generally **sh**(1) on Unix
systems, and cmd.exe on Windows.) If **wait** is present and has the
value _.false._, the execution of the command is asynchronous if the
system supports it; otherwise, the command is executed synchronously.

The three last arguments allow the user to get status information. After
synchronous execution, **exitstat** contains the integer exit code of
the command, as returned by **system**. **cmdstat** is set to zero if
the command line was executed (whatever its exit status was). **cmdmsg**
is assigned an error message if an error has occurred.

Note that the system call need not be thread-safe. It is the
responsibility of the user to ensure that the system is not called
concurrently if required.

When the command is executed synchronously, **execute_command_line**
returns after the command line has completed execution. Otherwise,
**execute_command_line** returns without waiting.

Because this intrinsic is making a system call, it is very system
dependent. Its behavior with respect to signaling is processor
dependent. In particular, on POSIX-compliant systems, the SIGINT and
SIGQUIT signals will be ignored, and the SIGCHLD will be blocked. As
such, if the parent process is terminated, the child process might
not be terminated alongside.

### **Options**

- **command**
  : the command line to be executed. The interpretation is
  programming-environment dependent.

- **wait**
  : If **wait** is present with the
  value _.false._, and the processor supports asynchronous execution of
  the command, the command is executed asynchronously; otherwise it is
  executed synchronously.

  When the command is executed synchronously, **execute_command_line**(3)
  returns after the command line has completed execution. Otherwise,
  **execute_command_line**(3) returns without waiting.

- **exitstat**
  : If the command is executed synchronously, it is assigned the value
  of the processor-dependent exit status. Otherwise, the value of
  **exitstat** is unchanged.

- **cmdstat**
  : If an error condition occurs and **cmdstat** is not present, error
  termination of execution of the image is initiated.

  It is assigned the value **-1** if the processor does not support
  command line execution, a processor-dependent positive value if an
  error condition occurs, or the value **-2** if no error condition
  occurs but **wait** is present with the value false and the processor
  does not support asynchronous execution. Otherwise it is assigned
  the value 0.

- **cmdmsg**
  : If an error condition occurs, it is assigned a processor-dependent
  explanatory message. Otherwise, it is unchanged.

### **Examples**

Sample program:

```fortran
program demo_exec
implicit none
   integer :: i

   call execute_command_line("external_prog.exe", exitstat=i)
   print *, "Exit status of external_prog.exe was ", i

   call execute_command_line("reindex_files.exe", wait=.false.)
   print *, "Now reindexing files in the background"
end program demo_exec
```

### **Standard**

Fortran 2008

### **See also**

[**get_environment_variable**(3)](#get_environment_variable)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
