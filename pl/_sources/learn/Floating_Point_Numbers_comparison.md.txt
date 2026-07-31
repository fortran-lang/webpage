# Floating-Point Tolerance and Precision in Fortran

Floating-point numbers like `0.1` cannot be represented exactly in binary because their binary form is infinite and repeating. Due to the limited precision of floating-point formats (like 32-bit or 64-bit), these numbers are rounded off to fit within the constrained number of bits.
This rounding can lead to small errors in representation and calculations. 

To ensure reliable comparisons, it is better to use **tolerance** to check whether two numbers are close enough rather than comparing them directly.

## Handling Floating-Point Comparisons

Here’s an example of how to use a tolerance value in Fortran:

### Example: Using Tolerance
```fortran
real(dp) :: tol
tol = 10 * epsilon(1.0_dp)  ! epsilon returns the smallest number such that 1.0 + epsilon > 1.0
    
if (abs(x - y) < tol) then
    print *, "Effectively Equal"
else
    print *, "Not Equal"
end if
```

In this example:
- The **tolerance** value is derived using either `epsilon()` or a manually defined small value.
- Instead of checking `x == y`, we compare the absolute difference `abs(x - y)` to the tolerance.

---

## Avoiding Floating-Point Precision Issues

Sometimes, directly incrementing floating-point numbers can cause cumulative rounding errors. 
Instead, use **integer iterators** and convert them to floating-point values within the loop.

### Example: Using Integer Iterators
```fortran
integer :: i
real(dp) :: step, value
step = 0.1_dp

do i = 0, 10
   value = i * step
   print *, value
end do
```

In this example:
- The step size is defined as `0.1` in double precision.
- The loop uses integers (`i`) to avoid compounding errors when iterating.

---

## Why Use Tolerance?

Due to rounding errors, numbers like `0.1 + 0.2` may not exactly equal `0.3`. Direct comparisons fail in such cases:
```fortran
if (a + b == c) then
   print *, "Equal"
else
   print *, "Not Equal"
end if
```
Instead, use a tolerance to make approximate comparisons:
```fortran
if (abs((a + b) - c) < tol) then
   print *, "Approximately Equal"
else
   print *, "Not Equal"
end if
```

---




