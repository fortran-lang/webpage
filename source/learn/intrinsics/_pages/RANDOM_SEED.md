(random_seed)=
## random_seed

### **Name**

**random_seed**(3) - \[MATHEMATICS:RANDOM\] Initialize a pseudo-random number sequence

### **Synopsis**

```fortran
    call random_seed( [size] [,put] [,get] )
```

```fortran
     subroutine random_seed( size, put, get )

      integer,intent(out),optional :: size
      integer,intent(in),optional :: put(*)
      integer,intent(out),optional :: get(*)
```

### **Characteristics**

- **size** a scalar default _integer_
- **put** a rank-one default _integer_ array
- **get** a rank-one default _integer_ array
- the result

### **Description**

**random_seed**(3) restarts or queries the state of the pseudorandom
number generator used by random_number.

If random_seed is called without arguments, it is seeded with random
data retrieved from the operating system.

### **Options**

- **size**
  : specifies the minimum size of the arrays used with the **put**
  and **get** arguments.

- **put**
  : the size of the array must be larger than or equal to the number
  returned by the **size** argument.

- **get**
  : It is **intent(out)** and the size of the array must be larger than
  or equal to the number returned by the **size** argument.

### **Examples**

Sample program:

```fortran
program demo_random_seed
implicit none
integer, allocatable :: seed(:)
integer :: n

   call random_seed(size = n)
   allocate(seed(n))
   call random_seed(get=seed)
   write (*, *) seed

end program demo_random_seed
```

Results:

```text
     -674862499 -1750483360  -183136071  -317862567   682500039
     349459   344020729 -1725483289
```

### **Standard**

Fortran 95

### **See Also**

[**random_number**(3)](#random_number)

_fortran-lang intrinsic descriptions_
