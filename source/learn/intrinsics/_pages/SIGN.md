## sign

### **Name**

**sign**(3) - \[NUMERIC\] Sign copying function

### **Syntax**

```fortran
result = sign(a, b)

    elemental function sign(a, b)
    type(TYPE(kind=KIND))            :: sign
    type(TYPE(kind=KIND)),intent(in) :: a, b
```

where TYPE may be *real* or *integer* and KIND is any supported kind for the type.


### **Description**

**sign**(a,b) returns the value of **a** with the sign of **b**.


For processors that distinguish between positive and negative zeros  **sign()** may be used to
distinguish between **real** values 0.0 and −0.0. SIGN (1.0, -0.0) will
return −1.0 when a negative zero is distinguishable.

    29  1 Description. Magnitude of A with the sign of B.



### **Arguments**

  - **a**
    : Shall be of type *integer* or *real*

  - **b**
    : Shall be of the same type and kind as **a**

### **Returns**

The kind of the return value is the magnitude of **a** with the sign of **b**. That is,

  - If **b \>= 0**, the result is **abs(a)**;
  - else if **b < 0**, the result it is -**abs(a)**.
  - If **b** is *real* and the processor distinguishes between **-0.0** and **0.0** then the
    result is **-abs(a)**.

### **Examples**

Sample program:

```fortran
program demo_sign
implicit none
   print *,  sign( -12,  1 )
   print *,  sign( -12,  0 )
   print *,  sign( -12, -1 )

   print *,  sign( -12.0, [1.0, 0.0, -1.0] )

   print *,  'can I distinguise 0 from -0? ', sign( 1.0, -0.0 ) .ne. sign( 1.0, 0.0 )
end program demo_sign
````

Results:

```text
             12
             12
            -12
      12.00000       12.00000      -12.00000
    can I distinguise 0 from -0?  F
```

### **Standard**

FORTRAN 77 and later

####### fortran-lang intrinsic descriptions (license: MIT)
