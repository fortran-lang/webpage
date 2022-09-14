## all

### **Name**

**all**(3) - \[ARRAY REDUCTION\] determines if all the values are true

### **Syntax**

```fortran
result = all(mask, dim)
```

### **Description**

Logical conjunction of elements of **mask** along dimension **dim**.

"**all(mask, dim)**" determines if all the values are true in **mask**
in the array along dimension **dim**.

### **Arguments**

- **mask**
  : shall be a logical array. 

- **dim**
  : (optional) **dim** shall be a scalar integer with a value that lies
  between one and the rank of **mask**. The corresponding actual argument
  shall not be an optional dummy argument.

### **Returns**

"**all(mask)**" returns a scalar value of type _logical_ where the kind
type parameter is the same as the kind type parameter of **mask**. If
**dim** is present, then **all(mask, dim)** returns an array with the rank
of **mask** minus 1. The shape is determined from the shape of **mask**
where the **dim** dimension is elided.

1.  **all(mask)** is true if all elements of **mask** are true. It also is
    true if **mask** has zero size; otherwise, it is false.

2.  If the rank of **mask** is one, then **all(mask, dim)** is equivalent
    to **all(mask)**. If the rank is greater than one, then **all(mask,
    dim)** is determined by applying **all()** to the array sections.

3.  Result Characteristics. The result is of type _logical_ with the
    same kind type parameter as **mask**. It is scalar if **dim**
    is absent or **n = 1**; otherwise, the result has rank **n - 1**
    and shape **\[d1, d2, . . ., dDIM-1, dDIM+1, . . ., dn \]**
    where **\[d1, d2, . . ., dn \]** is the shape of **mask**.

4.  Result Value.

    Case (i):
    : The result of **all(mask)** has the value true if all
    elements of **mask** are true or if **mask** has
    size zero, and the result has value false if any element
    of **mask** is false.

    Case (ii):
    : If **mask** has rank one, **all(mask,dim)** is equal to
    **all(mask)**. Otherwise, the value of element **(s1, s2,
    . . ., sdim-1, sdim+1, . . ., sn )** of all **(mask,
    dim)** is equal to **all(mask (s1, s2, . . ., sdim-1,
    :, sdim+1, . . ., sn ))**.

### **Examples**

Sample program:

```fortran
program demo_all
implicit none
logical bool
  ! basic usage
   ! is everything true?
   bool = all([ .true., .true., .true. ])
   bool = all([ .true., .false., .true. ])
   print *, bool
  ! by a dimension
   ARRAYS: block
   integer :: a(2,3), b(2,3)
    ! set everything to one except one value in b
    a = 1
    b = 1
    b(2,2) = 2
    ! now compare those two arrays
    print *,'entire array :', all(a .eq. b )
    print *,'compare columns:', all(a .eq. b, dim=1)
    print *,'compare rows:', all(a .eq. b, dim=2)
  end block ARRAYS
end program demo_all
```
  Results:
```text
    T
    F
    entire array : F
    compare columns: T F T
    compare rows: T F
```
### **See Also**
[**any**(3)](ANY)

### **Standard**
Fortran 95 and later

_fortran-lang intrinsic descriptions_
