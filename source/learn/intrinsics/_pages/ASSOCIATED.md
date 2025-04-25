(associated)=
## associated

### **Name**

**associated**(3) - \[STATE:INQUIRY\] Association status of a pointer or pointer/target pair

### **Synopsis**

```fortran
    result = associated(pointer [,target])
```

```fortran
     logical function associated(pointer,target)

      type(TYPE(kind=KIND),pointer :: pointer
      type(TYPE(kind=KIND),pointer,optional :: target
```

### **Characteristics**

- **pointer** shall have the _pointer_ attribute and it can be any type
  or may be a procedure pointer
- **target** shall be a pointer or a target. It must have the
  same type, kind type parameter, and array rank as **pointer**.
- The association status of neither **pointer** nor **target** shall
  be undefined.
- the result is a default _logical_ value

### **Description**

**associated**(3) determines the status of the pointer **pointer**
or if **pointer** is associated with the target **target**.

### **Options**

- **pointer**
  : A pointer to test for association.
  Its pointer association status shall not be undefined.

- **target**
  : A target that is to be tested for occupying the same storage
  units as the pointer **pointer**. That is, it is tested as to whether it
  is pointed to by **pointer**.

### **Result**

**associated**(3f) returns a scalar value of type _logical_.
There are several cases:

1.  When the optional **target** is not present then **associated(pointer)**
    is _.true._ if **pointer** is associated with a target; otherwise, it
    returns _.false._.

2.  If **target** is present and a scalar target, the result is _.true._ if
    **target** is not a zero-sized storage sequence and the target
    associated with **pointer** occupies the same storage units. If **pointer**
    is disassociated, the result is _.false._.

3.  If **target** is present and an array target, the result is _.true._ if
    **target** and **pointer** have the same shape, are not zero-sized arrays,
    are arrays whose elements are not zero-sized storage sequences, and
    **target** and **pointer** occupy the same storage units in array element
    order.

    As in case 2, the result is _.false._, if **pointer** is disassociated.

4.  If **target** is present and an scalar pointer, the result is _.true._ if
    **target** is associated with **pointer**, the target associated with **target**
    are not zero-sized storage sequences and occupy the same storage
    units.

    The result is _.false._, if either **target** or **pointer** is disassociated.

5.  If **target** is present and an array pointer, the result is _.true._ if
    target associated with **pointer** and the target associated with **target**
    have the same shape, are not zero-sized arrays, are arrays whose
    elements are not zero-sized storage sequences, and **target** and
    **pointer** occupy the same storage units in array element order.

6.  If **target** is present and is a procedure, the result is true if and
    only if **pointer** is associated with **target** and, if **target** is an
    internal procedure, they have the same host instance.

7.  If **target** is present and is a procedure pointer, the result is true
    if and only if **pointer** and **target** are associated with the same
    procedure and, if the procedure is an internal procedure, they have
    the same host instance.

### **Examples**

Sample program:

```fortran
program demo_associated
implicit none
real, target  :: tgt(2) = [1., 2.]
real, pointer :: ptr(:)
   ptr => tgt
   if (associated(ptr)     .eqv. .false.) &
   & stop 'POINTER NOT ASSOCIATED'
   if (associated(ptr,tgt) .eqv. .false.) &
   & stop 'POINTER NOT ASSOCIATED TO TARGET'
end program demo_associated
```

### **Standard**

Fortran 95

### **See Also**

[**null**(3)](#null)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
