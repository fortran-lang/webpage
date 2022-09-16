## exponent

### **Name**

**exponent**(3) - \[MODEL_COMPONENTS\] Exponent function

### **Syntax**

```fortran
result = exponent(x)
```

### **Description**

**exponent**(x) returns the value of the exponent part of **x**. If **x** is
zero the value returned is zero.

### **Arguments**

- **x**
  : The type shall be _real_.

### **Returns**

The return value is of type default _integer_.

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
end program demo_exponent
```

Results:

```text
              1
              0
```

### **Standard**

Fortran 95 and later

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
