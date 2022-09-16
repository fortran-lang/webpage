## present

### **Name**

**present**(3) - [STATE\] Determine whether an optional dummy argument
is specified

### **Syntax**

```fortran
result = present(a)

   function present (a)
   logical :: present
```

### **Description**

Determines whether an optional dummy argument is present.

### **Arguments**

- **a**
  : May be of any type and may be a pointer, scalar or array value,
  or a dummy procedure. It shall be the name of an optional dummy
  argument accessible within the current subroutine or function.

### **Returns**

Returns either **.true.** if the optional argument **a** is present,
or **.false.** otherwise.

### **Examples**

Sample program:

```fortran
program demo_present
implicit none
   write(*,*) func(), func(42)
contains

integer function func(x)
integer, intent(in), optional :: x
   if(present(x))then
     func=x**2
   else
     func=0
   endif
end function

end program demo_present
```

Results:

```text
     0        1764
```

### **Standard**

Fortran 95 and later

 _fortran-lang intrinsic descriptions_
