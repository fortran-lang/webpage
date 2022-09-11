## min

### **Name**

**min**(3) - \[NUMERIC\] Minimum value of an argument list

### **Syntax**

```fortran
result = min(a1, a2, a3, ... )
```

### **Description**

Returns the argument with the smallest (most negative) value.

### **Arguments**

- **a1**
  : The type shall be _integer_ or _real_.

- **a2, a3, ...**
  : An expression of the same type and kind as **a1**.

### **Returns**

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

FORTRAN 77 and later

### **See Also**

[**max**(3)](MAX),
[**minloc**(3)](MINLOC),
[**minval**(3)](MINVAL)

###### fortran-lang intrinsic descriptions
