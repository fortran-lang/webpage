(dim)=
## dim

### **Name**

**dim**(3) - \[NUMERIC\] Positive difference of X - Y

### **Synopsis**

```fortran
    result = dim(x, y)
```

```fortran
     elemental TYPE(kind=KIND) function dim(x, y )

      TYPE(kind=KIND),intent(in) :: x, y
```

### **Characteristics**

- **x** and **y** may be any _real_ or _integer_ but of the same type
  and kind
- the result is of the same type and kind as the arguments

### **Description**

**dim**(3) returns the maximum of **x - y** and zero.
That is, it returns the difference **x - y** if the result is positive;
otherwise it returns zero. It is equivalent to

```fortran
  max(0,x-y)
```

### **Options**

- **x**
  : the subtrahend, ie. the number being subtracted from.

- **y**
  : the minuend; ie. the number being subtracted

### **Result**

Returns the difference **x - y** or zero, whichever is larger.

### **Examples**

Sample program:

```fortran
program demo_dim
use, intrinsic :: iso_fortran_env, only : real64
implicit none
integer           :: i
real(kind=real64) :: x

   ! basic usage
    i = dim(4, 15)
    x = dim(4.321_real64, 1.111_real64)
    print *, i
    print *, x

   ! elemental
    print *, dim([1,2,3],2)
    print *, dim([1,2,3],[3,2,1])
    print *, dim(-10,[0,-10,-20])

end program demo_dim
```

Results:

```text
 >            0
 >    3.21000000000000
 >            0           0           1
 >            0           0           2
 >            0           0          10
```

### **Standard**

FORTRAN 77

### **See Also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
