## iand

### **Name**

**iand**(3) - \[BIT:LOGICAL\] Bitwise logical and

### **Syntax**

```fortran
result = iand(i, j)
```

### **Description**

Bitwise logical **and**.

### **Arguments**

- **i**
  : The type shall be _integer_.

- **j**
  : The type shall be _integer_, of the same kind as **i**.

### **Returns**

The return type is _integer_, of the same kind as the arguments. (If the
argument kinds differ, it is of the same kind as the larger argument.)

### **Examples**

Sample program:

```fortran
program demo_iand
implicit none
integer :: a, b
      data a / z'f' /, b / z'3' /
      write (*,*) iand(a, b)
end program demo_iand
```

Results:

```text
              3
```

### **Standard**

Fortran 95 and later

### **See Also**

[**btest**(3)](BTEST),
[**ibclr**(3)](IBCLR),
[**ibits**(3)](IBITS),
[**ibset**(3)](IBSET),
[**ieor**(3)](IEOR),
[**ior**(3)](IOR),
[**not**(3)](NOT),
[**mvbits**(3)](MVBITS)

_fortran-lang intrinsic descriptions_
