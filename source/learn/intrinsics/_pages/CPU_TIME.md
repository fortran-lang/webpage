(cpu_time)=
## cpu_time

### **Name**

**cpu_time**(3) - \[SYSTEM:TIME\] Return CPU processor time used in seconds

### **Synopsis**

```fortran
     call cpu_time(time)
```

```fortran
      subroutine cpu_time(time)

       real,intent(out) :: time
```

### **Characteristics**

- **time** is a _real_ of any kind

### **Description**

**cpu_time**(3) returns a _real_ value representing the elapsed CPU time
in seconds. This is useful for testing segments of code to determine
execution time.

If no time source is available, **time** is set to a negative value.

The exact definition of time is left imprecise because of the variability
in what different processors are able to provide.

Note that **time** may contain a system dependent, arbitrary offset and may
not start with 0.0. For **cpu_time**(3) the absolute value is meaningless.
Only differences between subsequent calls, as shown in the example below,
should be used.

PARALLEL PROCESSING

Whether the value assigned is an approximation to the amount of time used
by the invoking image, or the amount of time used by the whole program,
is processor dependent.

A processor for which a single result is inadequate (for example, a
parallel processor) might choose to provide an additional version for
which **time** is an array.

### **Result**

- **time**
  : is assigned a processor-dependent approximation to the processor
  time in seconds. If the processor cannot return a meaningful time,
  a processor-dependent negative value is returned.

  : The start time is left imprecise because the purpose is to time
  sections of code, as in the example. This might or might not
  include system overhead time.

### **Examples**

Sample program:

```fortran
program demo_cpu_time
use, intrinsic :: iso_fortran_env, only : real_kinds,real32,real64,real128
implicit none
real :: start, finish
real(kind=real64) :: startd, finishd
   !
   call cpu_time(start)
   call cpu_time(startd)
   ! put code to time here
   call cpu_time(finish)
   call cpu_time(finishd)
   !
  ! writes processor time taken by the piece of code.

  ! the accuracy of the clock and whether it includes system time
  ! as well as user time is processor dependent. Accuracy up to
  ! milliseconds is common but not guaranteed, and may be much
  ! higher or lower
   print '("Processor Time = ",f6.3," seconds.")',finish-start

   ! see your specific compiler documentation for how to measure
   ! parallel jobs and for the precision of the time returned
   print '("Processor Time = ",g0," seconds.")',finish-start
   print '("Processor Time = ",g0," seconds.")',finishd-startd
end program demo_cpu_time
```

Results:

The precision of the result, some aspects of what is returned,
and what if any options there are for parallel applications
may very from system to system. See compiler-specific for details.

```text
   Processor Time =  0.000 seconds.
   Processor Time = .4000030E-05 seconds.
   Processor Time = .2000000000000265E-05 seconds.
```

### **Standard**

Fortran 95

### **See Also**

[**system_clock**(3)](#system_clock),
[**date_and_time**(3)](#date_and_time)

_fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
