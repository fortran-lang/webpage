## new_line

### **Name**

**new_line**(3) - \[CHARACTER\] new-line character

### **Syntax**

```fortran
result = new_line(c)

   character(len=1,kind=kind(c)) :: new_line(c)
   character(len=1),intent(in) :: c(..)
```

### **Description**

**new_line(c)** returns the new-line character.

Case (i)
: If **a** is default _character_ and the character in position **10** of the
ASCII collating sequence is representable in the default character set,
then the result is **achar(10)**.

Case (ii)
: If **a** is an ASCII character or an ISO 10646 character, then the
result is **char(10, kind (a))**.

Case (iii)
: Otherwise, the result is a processor-dependent character that
represents a newline in output to files connected for formatted
stream output if there is such a character.

Case (iv)
: Otherwise, the result is the blank character.

### **Arguments**

- **C**
  : The argument shall be a scalar or array of the type _character_.

### **Returns**

Returns a _character_ scalar of length one with the new-line character of
the same kind as parameter **c**.

### **Examples**

Sample program:

```fortran
program demo_new_line
implicit none
character,parameter :: nl=new_line('a')
character(len=:),allocatable :: string

   string='This is record 1.'//nl//'This is record 2.'
   write(*,'(a)') string

   write(*,'(*(a))',advance='no') &
      nl,'This is record 1.',nl,'This is record 2.',nl

end program demo_new_line
```

Results:

```text
   This is record 1.
   This is record 2.

   This is record 1.
   This is record 2.
```

### **Standard**

Fortran 2003 and later

_fortran-lang intrinsic descriptions (license: MIT) @urbanjost_
