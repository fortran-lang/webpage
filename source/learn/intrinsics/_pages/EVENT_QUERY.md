## event_query

### **Name**

**event_query**(3) - \[COLLECTIVE\] Query whether a coarray event has occurred

### **Syntax**

```fortran
call event_query(event, count, stat)
```

### **Description**

**event_query** assigns the number of events to **count** which have been
posted to the **event** variable and not yet been removed by calling
**event_wait**. When **stat** is present and the invocation was successful, it
is assigned the value **0**. If it is present and the invocation has failed,
it is assigned a positive value and **count** is assigned the value **-1**.

### **Arguments**

- **event**
  : (intent(in)) Scalar of type event_type, defined in
  iso_fortran_env; shall not be coindexed.

- **count**
  : (intent(out))Scalar integer with at least the precision of default
  _integer_.

- **stat**
  : (OPTIONAL) Scalar default-kind _integer_ variable.

### **Examples**

Sample program:

```fortran
program demo_event_query
use iso_fortran_env
implicit none
type(event_type) :: event_value_has_been_set[*]
integer :: cnt
   if (this_image() == 1) then
      call event_query(event_value_has_been_set, cnt)
      if (cnt > 0) write(*,*) "Value has been set"
   elseif (this_image() == 2) then
      event post(event_value_has_been_set[1])
   endif
end program demo_event_query
```

### **Standard**

TS 18508 or later

 _fortran-lang intrinsic descriptions_
