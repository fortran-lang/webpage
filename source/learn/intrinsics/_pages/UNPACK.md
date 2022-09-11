## unpack

### **Name**

**unpack**(3) - \[ARRAY CONSTRUCTION\] scatter the elements of a vector
into an array using a mask

### **Syntax**

```fortran
result = unpack(vector, mask, field)

 type(TYPE(kind=KIND)),intent(in) :: vector(:)
 logical,intent(in)               :: mask(..)
 type(TYPE(kind=KIND)),intent(in) :: field(..)
 type(TYPE(kind=KIND))            :: result(..)
```
### **Description**

Scatter the elements of **vector** into a copy of an array **field**
of any rank using _.true._ values from **mask** in array element order
to specify placement of the **vector** values.

So a copy of **field** is generated with select elements replaced with
values from **vector**.

### **Arguments**

- **vector**
  : Shall be an array of any type and rank one. It shall have at least
  as many elements as **mask** has **.true.** values.

- **mask**
  : Shall be an array of type _logical_. 

- **field**
  : Shall be of the same type and type parameters as **vector** and
  shall be conformable with **mask**.


### **Returns**

The result is an array of the same type and type parameters as **vector**
and the same shape as **mask**.

The element of the result that corresponds to the ith true element
of MASK, in array element order, has the value VECTOR (i) for i =
1, 2, . . ., t, where t is the number of true values in MASK. Each
other element has a value equal to FIELD if FIELD is scalar or to the
corresponding element of FIELD if it is an array.

The resulting array corresponds to **field** with **.true.** elements
of **mask** replaced by values from **vector** in array element order.



### **Examples**
Particular values may be "scattered" to particular positions in an array by using
```text
                       1 0 0        
    If M is the array  0 1 0 
                       0 0 1  

    V is the array [1, 2, 3],
		               . T .
    and Q is the logical mask  T . .
  	                       . . T
    where "T" represents true and "." represents false, then the result of 

    UNPACK (V, MASK = Q, FIELD = M) has the value
                                       
      1 2 0 
      1 1 0  
      0 0 3 

    and the result of UNPACK (V, MASK = Q, FIELD = 0) has the value

      0 2 0
      1 0 0 
      0 0 3
```

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
