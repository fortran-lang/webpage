## get_environment

### **Name**

**get_environment_variable**(3) - \[SYSTEM:ENVIRONMENT\] Get an environmental variable

### **Syntax**

```fortran
  call get_environment_variable(name, value, length, status, trim_name)

   character(len=*),intent(in) :: name
   character(len=*),intent(out),optional :: value
   integer,intent(out),optional :: length
   integer,intent(out),optional :: status
   logical,intent(out),optional :: trim_name
```

### **Description**

Get the **value** of the environmental variable **name**.

Note that **get_environment_variable**(3) need not be thread-safe. It
is the responsibility of the user to ensure that the environment is not
being updated concurrently.

### **Options**

- **name**
  : The name of the environment variable to query.

  Shall be a scalar of type _character_ and of default kind.

### **Returns**

- **value**
  : The value of the environment variable being queried.

  Shall be a scalar of type _character_ and of default kind.
  The value of **name** is stored in **value**. If **value** is not large enough
  to hold the data, it is truncated. If **name** is not set, **value** will be
  filled with blanks.

- **length**
  : Argument **length** contains the length needed for storing the
  environment variable **name** or zero if it is not present.

  Shall be a scalar of type _integer_ and of default kind.

- **status**
  : **status** is **-1** if **value** is present but too short for the
  environment variable; it is **1** if the environment variable does not
  exist and **2** if the processor does not support environment variables;
  in all other cases **status** is zero.

  Shall be a scalar of type _integer_ and of default kind.

- **trim_name**
  : If **trim_name** is present with the value **.false.**, the trailing blanks in
  **name** are significant; otherwise they are not part of the environment
  variable name.

  Shall be a scalar of type _logical_ and of default kind.

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

function get_env(NAME,DEFAULT) result(VALUE)
! a function that makes calling get_environment_variable(3) simple
implicit none
character(len=*),intent(in)          :: NAME
character(len=*),intent(in),optional :: DEFAULT
character(len=:),allocatable         :: VALUE
integer                              :: howbig
integer                              :: stat
integer                              :: length
   ! get length required to hold value
   length=0
   VALUE=''
   if(NAME.ne.'')then
      call get_environment_variable( &
      & NAME, length=howbig,status=stat,trim_name=.true.)
      select case (stat)
      case (1)
       !*!print *, NAME, " is not defined in the environment. Strange..."
       VALUE=''
      case (2)
       !*!print *, &
       !*!"This processor does not support environment variables. Boooh!"
       VALUE=''
      case default
       ! make string to hold value of sufficient size
       if(allocated(VALUE))deallocate(VALUE)
       allocate(character(len=max(howbig,1)) :: VALUE)
       ! get value
       call get_environment_variable( &
       & NAME,VALUE,status=stat,trim_name=.true.)
       if(stat.ne.0)VALUE=''
      end select
   endif
   if(VALUE.eq.''.and.present(DEFAULT))VALUE=DEFAULT
end function get_env

end program demo_getenv
```

Typical Results:

```text
   HOME="/home/urbanjs"
```

### **Standard**

Fortran 2003 and later

###### fortran-lang intrinsic descriptions (license: MIT) @urbanjost
