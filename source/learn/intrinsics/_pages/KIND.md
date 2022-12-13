## kind

### **Name**

**kind**(3) - \[KIND INQUIRY\] Kind of an entity

### **Syntax**

```fortran
k = kind(x)
```

### **Description**

**kind(x)** returns the kind value of the entity **x**.

### **Arguments**

- **x**
  : Shall be of type _logical_, _integer_, _real_, _complex_ or _character_.

### **Returns**

The return value is a scalar of type _integer_ and of the default integer
kind.

### **Examples**

Sample program:

```fortran
program demo_kind
implicit none
integer,parameter :: kc = kind(' ')
integer,parameter :: kl = kind(.true.)

   print *, "The default character kind is ", kc
   print *, "The default logical kind is ", kl

end program demo_kind
```

Results:

```text
    The default character kind is            1
    The default logical kind is            4
```

### **Standard**

Fortran 95 and later

 _fortran-lang intrinsic descriptions_
