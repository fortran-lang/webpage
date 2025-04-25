(same_type_as)=
## same_type_as

### **Name**

**same_type_as**(3) - \[STATE:INQUIRY\] Query dynamic types for equality

### **Synopsis**

```fortran
    result = same_type_as(a, b)
```

```fortran
     logical same_type_as(a, b)

      type(TYPE(kind=KIND),intent(in) :: a
      type(TYPE(kind=KIND),intent(in) :: b
```

### **Characteristics**

- **a** shall be an object of extensible declared type or unlimited
  polymorphic. If it is a polymorphic pointer, it shall not have
  an undefined association status.

- **b** shall be an object of extensible declared type or unlimited
  polymorphic. If it is a polymorphic pointer, it shall not have
  an undefined association status.

### **Description**

**same_type_as**(3) queries the dynamic types of objects for equality.

### **Options**

- **a**
  : object to compare to **b** for equality of type

- **b**
  : object to be compared to for equality of type

### **Result**

If the dynamic type of **a** or **b** is extensible, the result is true
if and only if the dynamic type of **a** is the same as the dynamic
type of **b**. If neither **a** nor **b** has extensible dynamic type,
the result is processor dependent.

    NOTE1

The dynamic type of a disassociated pointer or unallocated allocatable
variable is its declared type. An unlimited polymorphic entity has no
declared type.

    NOTE2

The test performed by SAME_TYPE_AS is not the same as the test performed
by the type guard TYPE IS. The test performed by SAME_TYPE_AS does
not consider kind type parameters.

Sample program:

```fortran
  ! program demo_same_type_as
  module M_ether
  implicit none
  private

  type   :: dot
    real :: x=0
    real :: y=0
  end type dot

  type, extends(dot) :: point
    real :: z=0
  end type point

  type something_else
  end type something_else

  public :: dot
  public :: point
  public :: something_else

  end module M_ether

  program demo_same_type_as
  use M_ether, only : dot, point, something_else
  implicit none
  type(dot) :: dad, mom
  type(point) :: me
  type(something_else) :: alien

   write(*,*)same_type_as(me,dad),'I am descended from Dad, but equal?'
   write(*,*)same_type_as(me,me) ,'I am what I am'
   write(*,*)same_type_as(dad,mom) ,'what a pair!'

   write(*,*)same_type_as(dad,me),'no paradox here'
   write(*,*)same_type_as(dad,alien),'no relation'

   call pointers()
   contains
   subroutine pointers()
   ! Given the declarations and assignments
   type t1
      real c
   end type
   type, extends(t1) :: t2
   end type
   class(t1), pointer :: p, q, r
      allocate (p, q)
      allocate (t2 :: r)
      ! the result of SAME_TYPE_AS (P, Q) will be true, and the result
      ! of SAME_TYPE_AS (P, R) will be false.
      write(*,*)'(P,Q)',same_type_as(p,q),"mind your P's and Q's"
      write(*,*)'(P,R)',same_type_as(p,r)
   end subroutine pointers

  end program demo_same_type_as
```

Results:

```text
    F I am descended from Dad, but equal?
    T I am what I am
    T what a pair!
    F no paradox here
    F no relation
    (P,Q) T mind your P's and Q's
    (P,R) F
```

### **Standard**

Fortran 2003

### **See Also**

[**extends_type_of**(3)](#extends_type_of)

_fortran-lang intrinsic descriptions_
