(extends_type_of)=
## extends_type_of

### **Name**

**extends_type_of**(3) - \[STATE:INQUIRY\] Determine if the dynamic type
of **a** is an extension of the dynamic type of **mold**.

### **Synopsis**

```fortran
    result = extends_type_of(a, mold)
```

```fortran
     logical extends_type_of(a, mold)

      type(TYPE(kind=KIND),intent(in) :: a
      type(TYPE(kind=KIND),intent(in) :: mold
```

### **Characteristics**

-**a** shall be an object or pointer to an extensible declared type,
or unlimited polymorphic. If it is a polymorphic pointer, it
shall not have an undefined association status. -**mole** shall be an object or pointer to an extensible declared type
or unlimited polymorphic. If it is a polymorphic pointer,
it shall not have an undefined association status.

- the result is a scalar default logical type.

### **Description**

**extends_type_of**(3) is .true. if and only if the dynamic type of
**a** is or could be (for unlimited polymorphic) an extension of the
dynamic type of **mold**.

#### NOTE1

The dynamic type of a disassociated pointer or unallocated allocatable
variable is its declared type.

#### NOTE2

The test performed by **extends_type_of** is not the same as the
test performed by the type guard **class is**. The test performed by
**extends_type_of** does not consider kind type parameters.

### **options**

- **a**
  : be an object of extensible declared type or unlimited
  polymorphic. If it is a polymorphic pointer, it shall not have an
  undefined association status.

- **mold**
  : be an object of extensible declared type or unlimited
  polymorphic. If it is a polymorphic pointer, it shall not have an
  undefined association status.

### **Result**

If **mold** is unlimited polymorphic and is either a disassociated
pointer or unallocated allocatable variable, the result is true.

Otherwise if **a** is unlimited polymorphic and is either a
disassociated pointer or unallocated allocatable variable, the result
is false.

Otherwise the result is true if and only if the dynamic type of **a**

if the dynamic type of A or MOLD is extensible, the result is true if
and only if the dynamic type of A is an extension type of the dynamic
type of MOLD; otherwise the result is processor dependent.

### **Examples**

Sample program:

```fortran
  ! program demo_extends_type_of
  module M_demo_extends_type_of
  implicit none
  private

  type nothing
  end type nothing

  type, extends(nothing) :: dot
    real :: x=0
    real :: y=0
  end type dot

  type, extends(dot) :: point
    real :: z=0
  end type point

  type something_else
  end type something_else

  public :: nothing
  public :: dot
  public :: point
  public :: something_else

  end module M_demo_extends_type_of

  program demo_extends_type_of
  use M_demo_extends_type_of, only : nothing, dot, point, something_else
  implicit none
  type(nothing) :: grandpa
  type(dot) :: dad
  type(point) :: me
  type(something_else) :: alien

   write(*,*)'these should all be true'
   write(*,*)extends_type_of(me,grandpa),'I am descended from Grandpa'
   write(*,*)extends_type_of(dad,grandpa),'Dad is descended from Grandpa'
   write(*,*)extends_type_of(me,dad),'Dad is my ancestor'

   write(*,*)'is an object an extension of itself?'
   write(*,*)extends_type_of(grandpa,grandpa) ,'self-propagating!'
   write(*,*)extends_type_of(dad,dad) ,'clone!'

   write(*,*)' you did not father your grandfather'
   write(*,*)extends_type_of(grandpa,dad),'no paradox here'

   write(*,*)extends_type_of(dad,me),'no paradox here'
   write(*,*)extends_type_of(grandpa,me),'no relation whatsoever'
   write(*,*)extends_type_of(grandpa,alien),'no relation'
   write(*,*)extends_type_of(me,alien),'not what everyone thinks'

   call pointers()
   contains

   subroutine pointers()
   ! Given the declarations and assignments
   type t1
   real c
   end type
   type, extends(t1) :: t2
   end type
   class(t1), pointer :: p, q
      allocate (p)
      allocate (t2 :: q)
      ! the result of EXTENDS_TYPE_OF (P, Q) will be false, and the result
      ! of EXTENDS_TYPE_OF (Q, P) will be true.
      write(*,*)'(P,Q)',extends_type_of(p,q),"mind your P's and Q's"
      write(*,*)'(Q,P)',extends_type_of(q,p)
   end subroutine pointers

  end program demo_extends_type_of
```

Results:

```text
    these should all be true
    T I am descended from Grandpa
    T Dad is descended from Grandpa
    T Dad is my ancestor
    is an object an extension of itself?
    T self-propagating!
    T clone!
     you did not father your grandfather
    F no paradox here
    F no paradox here
    F no relation whatsoever
    F no relation
    F not what everyone thinks
    (P,Q) F mind your P's and Q's
    (Q,P) T
```

### **Standard**

Fortran 2003

### **See Also**

[**same_type_as**(3)](#same_type_as)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
