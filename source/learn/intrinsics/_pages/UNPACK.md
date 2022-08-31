## unpack

### **Name**

**unpack**(3) - \[ARRAY CONSTRUCTION\] Store the elements of a vector in an array of higher rank

### **Syntax**

```fortran
result = unpack(vector, mask, field)
```

### **Description**

Store the elements of **vector** in an array of higher rank.

### **Arguments**

- **vector**
  : Shall be an array of any type and rank one. It shall have at least
  as many elements as **mask** has **.true.** values.

- **mask**
  : Shall be an array of type _logical_.

- **field**
  : Shall be of the same type as **vector** and have the same shape as **mask**.

### **Returns**

The resulting array corresponds to **field** with **.true.** elements of **mask**
replaced by values from **vector** in array element order.

### **Examples**

Sample program:

```fortran
program demo_unpack
implicit none
integer :: vector(2)  = [1,1]
logical :: mask(4)  = [ .true., .false., .false., .true. ]
integer :: field(2,2) = 0, unity(2,2)

   ! result: unity matrix
   unity = unpack(vector, reshape(mask, [2,2]), field)
   write(*,*)unity,size(unity),shape(unity)

end program demo_unpack
```

Results:

```text
              1           0           0           1           4
              2           2
```

### **Standard**

Fortran 95 and later

### **See Also**

[**pack**(3)](PACK),
[**merge**(3)](MERGE),
[**pack**(3)](PACK),
[**spread**(3)](SPREAD),
[**unpack**(3)](UNPACK)

###### fortran-lang intrinsic descriptions
