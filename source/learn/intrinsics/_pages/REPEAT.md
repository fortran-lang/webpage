## repeat

### **Name**

**repeat**(3) - \[CHARACTER\] Repeated string concatenation

### **Syntax**

```fortran
result = repeat(string, ncopies)

   character(len=len(string)*ncopies) :: repeat
   character(len=*),intent(in)        :: string
   integer,intent(in)                 :: ncopies
```

### **Description**

Concatenates **ncopies** copies of a string.

### **Arguments**

- **string**
  : The input string to repeatedly generate.
  Shall be scalar and of type _character_.

- **ncopies**
  : Number of copies to make of _string_, greater than or equal to zero (0).
  Shall be scalar and of type _integer_.

### **Returns**

A new scalar of type _character_ built up from **ncopies** copies of **string**.

### **Examples**

Sample program:

```fortran
program demo_repeat
implicit none
integer :: i
    write(*,'(a)') repeat("^v", 36)         ! line break
    write(*,'(a)') repeat("_", 72)          ! line break
    write(*,'(a)') repeat("1234567890", 7)  ! number line
    do i=80,0,-1 ! a simple progress bar
        write(*,'(a)',advance='no') &
        & repeat("#", i)//repeat(' ',80-i)//char(13)
        !do something slow
    enddo
end program demo_repeat
```

Results:

```
   ^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v
   ________________________________________________________________________
   1234567890123456789012345678901234567890123456789012345678901234567890
```

### **Standard**

Fortran 95 and later

### **See Also**

Functions that perform operations on character strings:

- **Elemental:**
  [**adjustl**(3)](#adjustl),
  [**adjustr**(3)](#adjustr),
  [**index**(3)](#index),
  [**scan**(3)](#scan),
  [**verify**(3)](#verify)

- **Non-elemental:**
  [**len_trim**(3)](#len_trim),
  [**len**(3)](#len),
  [**repeat**(3)](#repeat),
  [**trim**(3)](#trim)

 _fortran-lang intrinsic descriptions_
