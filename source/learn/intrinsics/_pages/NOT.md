## not

### **Name**

**not**(3) - \[BIT:LOGICAL\] Logical negation

### **Syntax**

```fortran
result = not(i)
```

### **Description**

NOT returns the bitwise Boolean inverse of I.

### **Arguments**

- **i**
  : The type shall be _integer_.

### **Returns**

The return type is _integer_, of the same kind as the argument.

### **Examples**

Sample program

```fortran
program demo_not
implicit none
integer :: i

   i=13741
   write(*,'(b32.32,1x,i0)')i,i
   write(*,'(b32.32,1x,i0)')not(i),not(i)

end program demo_not
```

Results:

```
   00000000000000000011010110101101 13741
   11111111111111111100101001010010 -13742
```

### **Standard**

Fortran 95 and later

### **See Also**

[**iand**(3)](#iand),
[**ior**(3)](#ior),
[**ieor**(3)](#ieor),
[**ibits**(3)](#ibits),
[**ibset**(3)](#ibset),

[**ibclr**(3)](#ibclr)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
