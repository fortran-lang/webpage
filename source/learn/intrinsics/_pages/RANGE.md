## range

### **Name**

**range**(3) - \[NUMERIC MODEL\] Decimal exponent range of a real kind

### **Syntax**

```fortran
result = range(x)

      function range (x)
      integer :: range
      type(TYPE,kind=KIND),intent(in) :: x
```

where TYPE is _real_ or _complex_ and KIND is any kind supported by
TYPE.

### **Description**

**range(x)** returns the decimal exponent range in the model of the type
of **x**.

### **Arguments**

- **x**
  : Shall be of type _real_ or _complex_.

### **Returns**

The return value is of type _integer_ and of the default integer kind.

### **Examples**

Sample program:

```fortran
program demo_range
use,intrinsic :: iso_fortran_env, only : dp=>real64,sp=>real32
implicit none
real(kind=sp)    :: x(2)
complex(kind=dp) :: y
   print *, precision(x), range(x)
   print *, precision(y), range(y)
end program demo_range
```

Results:

```text
              6          37
             15         307
```

### **Standard**

Fortran 95 and later

### **See Also**

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**exponent**(3)](#exponent),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

 _fortran-lang intrinsic descriptions_
