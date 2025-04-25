(present)=
## present

### **Name**

**present**(3) - [STATE:INQUIRY\] Determine whether an optional dummy argument
is specified

### **Synopsis**

```fortran
    result = present(a)
```

```fortran
     logical function present (a)

      type(TYPE(kind=KIND)) :: a(..)
```

### **Characteristics**

- **a** May be of any type and may be a pointer, scalar or array value,
  or a dummy procedure.

### **Description**

**present**(3) can be used in a procedure to determine if an optional
dummy argument was present on the current call to the procedure.

**a** shall be the name of an optional dummy argument that is accessible
in the subprogram in which the **present**(3) function reference
appears. There are no other requirements on **a**.

Note when an argument is not present when the current procedure is
invoked, you may only pass it as an optional argument to another
procedure or pass it as an argument to **present**.

### **Options**

- **a**
  : the name of an optional dummy argument accessible within the current
  subroutine or function.

### **Result**

Returns _.true._ if the optional argument **a** is present (was passed
on the call to the procedure) , or _.false._ otherwise.

### **Examples**

Sample program:

```fortran
program demo_present
implicit none
integer :: answer
   ! argument to func() is not present
   answer=func()
   write(*,*) answer
   ! argument to func() is present
   answer=func(1492)
   write(*,*) answer
contains
!
integer function func(x)
! the optional characteristic on this definition allows this variable
! to not be specified on a call; and also allows it to subsequently
! be passed to PRESENT(3):
integer, intent(in), optional :: x
integer :: x_local
   !
   ! basic
   if(present(x))then
     ! if present, you can use x like any other variable.
     x_local=x
   else
     ! if not, you cannot define or reference x except to
     ! pass it as an optional parameter to another procedure
     ! or in a call to present(3f)
     x_local=0
   endif
   !
   func=x_local**2
   !
   ! passing the argument on to other procedures
   ! so something like this is a bad idea because x is used
   ! as the first argument to merge(3f) when it might not be
   ! present
   ! xlocal=merge(x,0,present(x)) ! NO!!
   !
   ! We can pass it to another procedure if another
   ! procedure declares the argument as optional as well,
   ! or we have tested that X is present
   call tattle('optional argument x',x)
   if(present(x))call not_optional(x)
end function
!
subroutine tattle(label,arg)
character(len=*),intent(in) :: label
integer,intent(in),optional :: arg
   if(present(arg))then
      write(*,*)label,' is present'
   else
      write(*,*)label,' is not present'
   endif
end subroutine tattle
!
subroutine not_optional(arg)
integer,intent(in) :: arg
   write(*,*)'already tested X is defined',arg
end subroutine not_optional
!
end program demo_present
```

Results:

```text
    optional argument x is not present
              0
    optional argument x is present
    already tested X is defined 1492
        2226064
```

### **Standard**

Fortran 95

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
