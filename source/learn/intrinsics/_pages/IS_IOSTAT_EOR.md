(is_iostat_eor)=
## is_iostat_eor

### **Name**

**is_iostat_eor**(3) - \[STATE:INQUIRY\] Test for end-of-record value

### **Synopsis**

```fortran
    result = is_iostat_eor(i)
```

```fortran
     elemental integer function is_iostat_eor(i)

      integer(kind=KIND),intent(in) :: i
```

### **Characteristics**

- **i** is _integer_ of any kind
- the return value is a default _logical_

### **Description**

**is_iostat_eor**(3) tests whether a variable has the value of the
I/O status "end of record". The function is equivalent to comparing
the variable with the **iostat_eor** parameter of the intrinsic module
**iso_fortran_env**.

### **Options**

- **i**
  : The value to test as indicating "end of record".

### **Result**

Returns _.true._ if and only if **i** has the value which indicates
an end-of-record condition for iostat= specifiers, and is _.false._
otherwise.

### **Examples**

Sample program:

```fortran
program demo_is_iostat_eor
use iso_fortran_env, only : iostat_eor
implicit none
integer :: inums(5), lun, ios

  ! create a test file to read from
   open(newunit=lun, form='formatted',status='scratch')
   write(lun, '(a)') '10 20 30'
   write(lun, '(a)') '40 50 60 70'
   write(lun, '(a)') '80 90'
   write(lun, '(a)') '100'
   rewind(lun)

   do
      read(lun, *, iostat=ios) inums
      write(*,*)'iostat=',ios
      if(is_iostat_eor(ios)) then
         stop 'end of record'
      elseif(is_iostat_end(ios)) then
         print *,'end of file'
         exit
      elseif(ios.ne.0)then
         print *,'I/O error',ios
         exit
      endif
   enddo

   close(lun,iostat=ios,status='delete')

end program demo_is_iostat_eor
```

Results:

```text
 >  iostat=           0
 >  iostat=          -1
 >  end of file
```

### **Standard**

Fortran 2003

### **See also**

[\*\*\*\*(3)](#)

_fortran-lang intrinsic descriptions_
