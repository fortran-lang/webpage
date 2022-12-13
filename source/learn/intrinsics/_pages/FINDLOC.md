## findloc

### **Name**

**findloc**(3) - \[ARRAY:LOCATION\] Location of first element of ARRAY identified by MASK along dimension DIM having a value

### **Syntax**

```fortran
findloc (array, value, dim, mask, kind, back)

or

findloc(array, value, mask, kind, back)
```

### **Description**

Location of the first element of **array** identified by **mask** along
dimension **dim** having a value equal to **value**.

If both **array** and **value** are of type logical, the comparison is
performed with the **.eqv.** operator; otherwise, the comparison is
performed with the == operator. If the value of the comparison is
true, that element of **array** matches **value**.

If only one element matches **value**, that element's subscripts are
returned. Otherwise, if more than one element matches **value** and
**back** is absent or present with the value false, the element whose
subscripts are returned is the first such element, taken in array
element order. If **back** is present with the value true, the element
whose subscripts are returned is the last such element, taken in array
element order.

### **Options**

- **array**
  : shall be an array of intrinsic type.

- **value**
  : shall be scalar and in type conformance with **array**, as specified
  in Table 7.3 for relational intrinsic operations 7.1.5.5.2).

- **dim**
  : shall be an integer scalar with a value in the range 1 **DIM** n, where
  n is the rank of **array**. The corresponding actual argument shall
  not be an optional dummy argument.

- **mask**
  : (optional) shall be of type logical and shall be conformable with
  **array**.

- **kind**
  : (optional) shall be a scalar integer initialization expression.

- **back**
  : (optional) shall be a logical scalar.

### **Returns**

Result Characteristics. Integer. If **kind** is present, the kind type
parameter is that specified by the value of **kind**; otherwise the kind
type parameter is that of default integer type. If **dim** does not appear,
the result is an array of rank one and of size equal to the rank of
**array**; otherwise, the result is of rank n - 1 and shape

```
   [d1, d2, . . ., dDIM-1, dDIM+1, . . ., dn ]
```

where

```
   [d1, d2, . . ., dn ]
```

is the shape of **array**.

### **Returns**

- **Case (i):**
  The result of **findloc (array, value)** is a rank-one array whose
  element values are the values of the subscripts of an element of
  **array** whose value matches **value**. If there is such a value, the
  ith subscript returned lies in the range 1 to ei, where ei is the
  extent of the ith dimension of **array**. If no elements match **value**
  or **array** has size zero, all elements of the result are zero.

- **Case (ii):**
  the result of **findloc (array, value, mask = mask)** is a
  rank-one array whose element values are the values of the subscripts
  of an element of **array**, corresponding to a true element of **mask**,
  whose value matches **value**. If there is such a value, the ith
  subscript returned lies in the range 1 to ei, where ei is the
  extent of the ith dimension of **array**. If no elements match
  **value**, **array** has size zero, or every element of **mask** has the
  value false, all elements of the result are zero.

- **Case (iii):**
  If **array** has rank one, the result of

```
      findloc (array, value, dim=dim [, mask = mask])
```

is a scalar whose value is equal to that of the first element of

```
      findloc (array, value [, mask = mask])
```

Otherwise, the value of element

```
      (s1, s2, . . ., sDIM-1, sDIM+1, . . ., sn )
```

of the result is equal to

```
      findloc (array (s1, s2, ..., sdim-1, :, sdim+1, ..., sn ), &
      value, dim=1 [, mask = mask (s1, s2, ..., sdim-1, :,
                      sdim+1, ..., sn )]).
```

### **Examples**

- **Case (i):**
  The value of

```
        findloc ([2, 6, 4, 6,], value = 6)
```

is \[2\], and the value of

```
        findloc ([2, 6, 4, 6], value = 6, back = .true.)
```

is \[4\].

- **Case (ii):**
  If **a** has the value

```text
      0 -5  7 7
      3  4 -1 2
      1  5  6 7
```

and **m** has the value

```text
       T T F T
       T T F T
       T T F T

      findloc (a, 7, mask = m)
```

has the value \[1, 4\] and

```
      findloc (a, 7, mask = m, back = .true.)
```

has the value \[3, 4\]. This is independent of the declared lower
bounds for **a** .

- **Case (iii):**
  The value of

```
      findloc ([2, 6, 4], value = 6, dim = 1)
```

is 2. If **b** has the value

```
       1 2 -9
       2 2  6
```

> findloc (b, **value** = 2, dim = 1)

has the value \[2, 1, 0\] and

```
      findloc (b, value = 2, dim = 2)
```

has the value \[2, 1\]. This is independent of the declared lower
bounds for **b**.

 _fortran-lang intrinsic descriptions_
