(get_environment_variable)=
## get_environment_variable

### **Name**

**get_environment_variable**(3) - \[SYSTEM:ENVIRONMENT\] Get value of an environment variable

### **Synopsis**

```fortran
    call get_environment_variable(name [,value] [,length] &
    & [,status] [,trim_name] [,errmsg] )
```

```fortran
     subroutine character(len=*) get_environment_variable( &
     & name, value, length, status, trim_name, errmsg )

      character(len=*),intent(in) :: name
      character(len=*),intent(out),optional   :: value
      integer(kind=**),intent(out),optional   :: length
      integer(kind=**),intent(out),optional   :: status
      logical,intent(out),optional            :: trim_name
      character(len=*),intent(inout),optional :: errmsg
```

### **Characteristics**

- a kind designated as \*\* may be any supported kind for the type
  meeting the conditions described herein.
- **name**, **value**, and **errmsg** are a scalar _character_ of
  default kind.
- **length** and **status** are _integer_ scalars with a decimal exponent
  range of at least four.
- **trim_name** is a scalar of type _logical_ and of default kind.

### **Description**

**get_environment_variable**(3) gets the **value** of the environment
variable **name**.

Note that **get_environment_variable**(3) need not be thread-safe. It
is the responsibility of the user to ensure that the environment is not
being updated concurrently.

If running in parallel be aware
It is processor dependent whether an environment variable that exists
on an image also exists on another image, and if it does exist on both
images whether the values are the same or different.

### **Options**

- **name**
  : The name of the environment variable to query.
  The interpretation of case is processor dependent.

### **Result**

- **value**
  : The value of the environment variable being queried. If **value**
  is not large enough to hold the data, it is truncated. If the variable
  **name** is not set or has no value, or the processor does not support
  environment variables **value** will be filled with blanks.

- **length**
  : Argument **length** contains the length needed for storing the
  environment variable **name**. It is zero if the environment variable
  is not set.

- **status**
  : **status** is **-1** if **value** is present but too short for the
  environment variable; it is **1** if the environment variable does
  not exist and **2** if the processor does not support environment
  variables; in all other cases **status** is zero.

- **trim_name**
  : If **trim_name** is present with the value _.false._, the trailing
  blanks in **name** are significant; otherwise they are not part of
  the environment variable name.

### **Examples**

Sample program:

```fortran
program demo_getenv
implicit none
character(len=:),allocatable :: homedir
character(len=:),allocatable :: var

     var='HOME'
     homedir=get_env(var)
     write (*,'(a,"=""",a,"""")')var,homedir

contains

function get_env(name,default) result(value)
! a function that makes calling get_environment_variable(3) simple
implicit none
character(len=*),intent(in)          :: name
character(len=*),intent(in),optional :: default
character(len=:),allocatable         :: value
integer                              :: howbig
integer                              :: stat
integer                              :: length
   length=0
   value=''
   if(name.ne.'')then
      call get_environment_variable( name, &
      & length=howbig,status=stat,trim_name=.true.)
      select case (stat)
      case (1)
       print *, name, " is not defined in the environment. Strange..."
       value=''
      case (2)
       print *, &
       "This processor does not support environment variables. Boooh!"
       value=''
      case default
       ! make string of sufficient size to hold value
       if(allocated(value))deallocate(value)
       allocate(character(len=max(howbig,1)) :: value)
       ! get value
       call get_environment_variable( &
       & name,value,status=stat,trim_name=.true.)
       if(stat.ne.0)value=''
      end select
   endif
   if(value.eq.''.and.present(default))value=default
end function get_env

end program demo_getenv
```

Typical Results:

```text
   HOME="/home/urbanjs"
```

### **Standard**

Fortran 2003

### **See also**

[**get_command_argument**(3)](#get_command_argument),
[**get_command**(3)](#get_command)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_

#
