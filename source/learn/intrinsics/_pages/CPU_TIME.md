## cpu_time

### **Name**

**cpu_time**(3) - \[SYSTEM:TIME\] return CPU processor time in seconds

### **Syntax**

```fortran
     call cpu_time(time)
     real,intent(out) :: time
```

### **Description**

Returns a _real_ value representing the elapsed CPU time in seconds. This
is useful for testing segments of code to determine execution time.

The exact definition of time is left imprecise because of the
variability in what different processors are able to provide.

If no time source is available, TIME is set to a negative value.

Note that TIME may contain a system dependent, arbitrary offset and may
not start with 0.0. For cpu_time the absolute value is meaningless.
Only differences between subsequent calls, as shown in the example
below, should be used.

A processor for which a single result is inadequate (for example, a
parallel processor) might choose to provide an additional version for
which time is an array.

### **Returns**

- **time**
  : The type shall be _real_ with **intent(out)**. It is assigned a
  processor-dependent approximation to the processor time in seconds.
  If the processor cannot return a meaningful time, a
  processor-dependent negative value is returned.

  : The start time is left imprecise because the purpose is to time
  sections of code, as in the example. This might or might not
  include system overhead time.

### **Examples**

Sample program:

```fortran
program demo_cpu_time
implicit none
real :: start, finish
   !
   call cpu_time(start)
   ! put code to test here
   call cpu_time(finish)
   !
   ! writes processor time taken by the piece of code.
   print '("Processor Time = ",f6.3," seconds.")',finish-start
end program demo_cpu_time
```

Results:

```text
   Processor Time =  0.000 seconds.
```

### **Standard**

Fortran 95 and later

### **See Also**

[**system_clock**(3)](#system_clock),
[**date_and_time**(3)](#date_and_time)

 _fortran-lang intrinsic descriptions (license: MIT) \@urbanjost_
