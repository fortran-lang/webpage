(exponent)=
## exponent

### **Name**

**exponent**(3) - \[MODEL_COMPONENTS\] Exponent of floating-point number

### **Synopsis**

```fortran
    result = exponent(x)
```

```fortran
     elemental integer function exponent(x)

      real(kind=**),intent(in) :: x
```

### **Characteristics**

- **x** shall be of type _real_ of any valid kind
- the result is a default _integer_ type

### **Description**

**exponent**(3) returns the value of the exponent part of **x**, provided
the exponent is within the range of default _integers_.

### **Options**

- **x**
  : the value to query the exponent of

### **Result**

**exponent**(3) returns the value of the exponent part of **x**

If **x** is zero the value returned is zero.

If **x** is an IEEE infinity or NaN, the result has the value HUGE(0).

### **Examples**

Sample program:

```fortran
program demo_exponent
implicit none
real :: x = 1.0
integer :: i
   i = exponent(x)
   print *, i
   print *, exponent(0.0)
   print *, exponent([10.0,100.0,1000.0,-10000.0])
   print *, 2**[10.0,100.0,1000.0,-10000.0]
   print *, exponent(huge(0.0))
   print *, exponent(tiny(0.0))
end program demo_exponent
```

Results:

```text
 >            4           7          10          14
 >          128
 >         -125
```

### **Standard**

Fortran 95

### **See Also**

[**digits**(3)](#digits),
[**epsilon**(3)](#epsilon),
[**fraction**(3)](#fraction),
[**huge**(3)](#huge),
[**maxexponent**(3)](#maxexponent),
[**minexponent**(3)](#minexponent),
[**nearest**(3)](#nearest),
[**precision**(3)](#precision),
[**radix**(3)](#radix),
[**range**(3)](#range),
[**rrspacing**(3)](#rrspacing),
[**scale**(3)](#scale),
[**set_exponent**(3)](#set_exponent),
[**spacing**(3)](#spacing),
[**tiny**(3)](#tiny)

_fortran-lang intrinsic descriptions_
