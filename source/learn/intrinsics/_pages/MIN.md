(min)=
## min

### **Name**

**min**(3) - \[NUMERIC\] Minimum value of an argument list

### **Synopsis**

```fortran
    result = min(a1, a2, a3, ... )
```

```fortran
     elemental TYPE(kind=KIND) function min(a1, a2, a3, ... )

      TYPE(kind=KIND,intent(in)   :: a1
      TYPE(kind=KIND,intent(in)   :: a2
      TYPE(kind=KIND,intent(in)   :: a3
                :
                :
                :
```

### **Characteristics**

- **TYPE** may be _integer_, _real_ or _character_.

### **Description**

**min**(3) returns the argument with the smallest (most negative) value.

See **max**(3) for an extended example of the behavior of **min**(3) as
and **max**(3).

### **Options**

- **a1**
  : the first element of the set of values to determine the minimum of.

- **a2, a3, ...**
  : An expression of the same type and kind as **a1** completing the
  set of values to find the minimum of.

### **Result**

The return value corresponds to the minimum value among the arguments,
and has the same type and kind as the first argument.

### **Examples**

Sample program

```fortran
program demo_min
implicit none
    write(*,*)min(10.0,11.0,30.0,-100.0)
end program demo_min
```

Results:

```
      -100.0000000
```

### **Standard**

FORTRAN 77

### **See Also**

[**maxloc**(3)](#maxloc),
[**minloc**(3)](#minloc),
[**minval**(3)](#minval),
[**max**(3)](#max),

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
