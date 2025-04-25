(dot_product)=
## dot_product

### **Name**

**dot_product**(3) - \[TRANSFORMATIONAL\] Dot product of two vectors

### **Synopsis**

```fortran
    result = dot_product(vector_a, vector_b)
```

```fortran
     TYPE(kind=KIND) function dot_product(vector_a, vector_b)

      TYPE(kind=KIND),intent(in) :: vector_a(:)
      TYPE(kind=KIND),intent(in) :: vector_b(:)
```

### **Characteristics**

- **vector_a**, **vector_b** may be any numeric or logical type array
  of rank one of the same size
- the two vectors need not be of the same kind, but both must be logical
  or numeric for any given call.
- the result is the same type and kind of the vector that is the higher
  type that the other vector is optionally promoted to if they differ.

The two vectors may be either numeric or logical and must be arrays
of rank one and of equal size.

### **Description**

**dot_product**(3) computes the dot product
multiplication of two vectors **vector_a** and **vector_b**.

### **Options**

- **vector_a**
  : A rank 1 vector of values

- **vector_b**
  : The type shall be numeric if **vector_a** is of numeric type
  or _logical_ if vector*a is of type \_logical*. vector_b shall be a
  rank-one array of the same size as **vector_a**.

### **Result**

If the arguments are numeric, the return value is a scalar of numeric
type. If the arguments are _logical_, the
return value is _.true._ or _.false._.

If the vectors are _integer_ or _real_, the result is

```fortran
     sum(vector_a*vector_b)
```

If the vectors are _complex_, the result is

```fortran
     sum(conjg(vector_a)*vector_b)**
```

If the vectors are _logical_, the result is

```fortran
     any(vector_a .and. vector_b)
```

### **Examples**

Sample program:

```fortran
program demo_dot_prod
implicit none
    integer, dimension(3) :: a, b
    a = [ 1, 2, 3 ]
    b = [ 4, 5, 6 ]
    print '(3i3)', a
    print *
    print '(3i3)', b
    print *
    print *, dot_product(a,b)
end program demo_dot_prod
```

Results:

```text
  >  1  2  3
  >
  >  4  5  6
  >
  >           32
```

### **Standard**

Fortran 95

### **See Also**

[**sum**(3)](#sum),
[**conjg**(3)](#conjg),
[**any**(3)](#any)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
