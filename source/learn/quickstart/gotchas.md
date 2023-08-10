Gotchas
=======

Fortran syntax is generally simple and consistent, but as with many languages it has some flaws. Sometimes because of legacy reasons (the evolution of the Fortran standard strongly emphasizes the backward compatibility because of the huge amount of legacy code that is still actively used), sometimes because of real flaws (poor choice at some point, which is difficult if not impossible to correct without breaking the backward compatibility), and sometimes just because Fortran is not C or C++ or Python or whatever: it has its own logic, with features that can sometimes be surprising to developers who are used to some other languages. 

All code snippets are compiled with gfortran 13.

Implicit typing
---------------

```
program foo
    integer :: nbofchildrenperwoman, nbofchildren, nbofwomen
    nbofwomen = 10
    nbofchildrenperwoman = 2
    nbofchildren = nbofwomen * nbofchildrenperwoman
    print*, "number of children:", nbofchildrem
end program
```
The program compiles and the execution gives:
```
 number of children:           0
```
Wait... Fortran is unable to multiply two integer numbers?? Of course not... The problem here is a typo in the variable name when printing it: `nbofchildreM` instead of `nbofchildreN`. But why the compiler didn't catch the typo? Well, because by default Fortran uses implicit typing: when encountering a variable that hasn't been explicitly typed, the compiler infers the type according to the first letter of the name. Variables names starting by I, J, K, L, M, N, are of type `INTEGER`, and all other ones are of type `REAL` (hence the classic joke "`GOD` is `REAL`, unless declared as `INTEGER`").

Implicit typing is as old as Fortran, in times where there was no explicit typing. Although it can still be convenient for quickly writing some test code, this practice is highly error prone and is discouraged. The strongly recommended good practice is to always disable implicit typing by stating `implicit none` (introduced in Fortran 90) at the beginning of all program units (main program, modules, and standalone routines):

```
program foo
implicit none
    integer :: nbofchildrenperwoman, nbofchildren, nbofwomen
    nbofwomen = 10
    nbofchildrenperwoman = 2
    nbofchildren = nbofwomen * nbofchildrenperwoman
    print*, "number of children:", nbofchildrem
end program
```
And now the compilation fails, allowing to quickly correct the typo:
```
    7 |     print*, "number of children:", nbofchildrem
      |                                               1
Error: Symbol 'nbofchildrem' at (1) has no IMPLICIT type; did you mean 'nbofchildren'?
```

Implied save
------------

```
subroutine foo()
implicit none
    integer :: c=0

    c = c+1
    print*, c
end subroutine

program main
implicit none
    integer :: i

    do i = 1, 5
        call foo()
    end do
end program
```
People used to C/C++ expect this program to print 5 times `1`, because they interpret `integer :: c=0` as the concatenation of a declaration and an assignment, as if it was:
```
integer :: c
c = 0
```
**But it is not**. This program actually outputs:
```
1
2
3
4
5
```
`integer :: c=0` is actually a one-shot **compile time initialization**, and it makes the variable persistent between calls to `foo()`. It is actually equivalent to: 
```
integer, save :: c=0
```
The `save` attribute is equivalent to the C `static` attribute to make a variable persistent, and it is *implied* in the case the variable is initialized. This is a modernized syntax (introduced in Fortran 90) compared to the legacy (and still valid) syntax:
```
integer c
data c /0/
```
Old fortraners just know that the modernized syntax is equivalent to the legacy one, even when `save` is not specified. But as a matter of fact the *implied save* can be misleading to newcomers who are used to the C logic. That's why it is generally recommended to **always** specify the `save` attribute:
```
integer, save :: c=0   ! save could be omitted, but it's clearer with it
```

*Note: an initialization expression of a derived type component is a fully different case:*
```
type bar
    integer :: c = 0
end type
```
*Here, the `c` component is initialized to zero each time a `type(bar)` variable is instantiated (**runtime** initialization).*


Floating point literal constants
---------------------------------

The following code snippet defines a double precision constant `x` (which is on most systems a IEEE754 64 bits floating point, with 15 significant digits):
```
program foo
implicit none
    integer, parameter :: dp = kind(0d0)
    real(kind=dp), parameter :: x = 9.3
    print*, precision(x), x
end program
```
The output is:
```
          15   9.3000001907348633
```
So, `x` has 15 significant digits as expected, and still the printed value is wrong from the 8th digit. The reason is that floating point literal constants have implicitely the default real kind, wich is usually the IEEE754 single precision floating point (with about 7 significant digits). The real number $9.3$ has no exact floating point representation, so it is first approximated to single precision up to the 7th digit, then casted to double precision before being assigned to `x`. But the previously lost digits are obviously not recovered.

The solution is to explicitly specify the kind of the constant: 
```
real(kind=dp), parameter :: x = 9.3_dp
```
And now the output is correct up to the 15th digit:
```
          15   9.3000000000000007     
```

Floating point literal constants (again)
---------------------------------

Suppose now you need a floating point constant that is 1/3 (one-third). You may write:
```
program foo
implicit none
    integer, parameter :: dp = kind(0d0)
    real(dp), parameter :: onethird = 1_dp / 3_dp
    print*, onethird
end program
```
Then the output is (!):
```
   0.0000000000000000     
```
The reason is that `1_dp` and `3_dp` are **integer** literal constants, despite the `_dp` suffix that is *supposed* to represent a floating point kind. Consequently the division is the integer division, with 0 as a result. The gotcha here is that the standard allows compilers to use identical kind values for `REAL` and `INTEGER` types. For instance with gfortran, on most platforms the value $8$ is both the double precision kind AND the 64 bits integer kind, so that `1_dp` is a fully valid integer constant. In constrast, the NAG compiler uses by default unique kind values, such that in the example above `1_dp` would produce a compilation error.

The right way to denote floating point constants is to **always** include the point: 
```
    real(dp), parameter :: onethird = 1.0_dp / 3.0_dp
```
Then the ouput is:
```
  0.33333333333333331     
```

Leading space in prints
-----------------------

```
program foo
implicit none
    print*, "Hello world!"
end program
```
Ouput:
```
% gfortran hello.f90 && ./a.out
 Hello world!
```
Note the extra leading space, which is not present in the string of the source code. Historically, the first character was containing a [carriage control code](https://en.wikipedia.org/wiki/ASA_carriage_control_characters) for the early printers, and it was not printed per se. The space " " was instructing the printer to perform a CR+LF sequence before printing the content, and was automatically prepended by the Fortran `print*` statement. Some compilers still do that, although the modern output devices do neither intercept nor use the control character, which is hence "printed". If this leading blank is a problem (it rarely is), then instead of the `*` (which means "let the compiler decide how to format the output") we can code an explicit format:
```
    print "(A)", "Hello world!"
```
In this case, the compiler does no longer prepend the leading space:
```
% gfortran hello.f90 && ./a.out
Hello world!
```

Filename extension
------------------

Suppose we put the above "Hello world" program in the source file `hello.f`. Most compilers will produce many compilation errors:
```
% gfortran hello.f
hello.f:1:1:

 program foo
 1
Error: Non-numeric character in statement label at (1)
hello.f:1:1:

 implicit none
 1
Error: Non-numeric character in statement label at (1)
hello.f:2:1:

     print*, "Hello world!"
     1
Error: Non-numeric character in statement label at (1)

...[truncated]
```
The reason is that the `.f` extension is by a widely accepted convention "reserved" for the legacy "fixed source form", which was designed for the punch card systems. In particular, the columns 1-6 were reserved for labels, continuation characters, and comments, and the actual statements and instructions had to be within the columns 7-72. The free source form removes all the limitations of the fixed source form, but since the latter cohabits with the former, the convention adopted by most compilers is to use by default the `.f90` extension for the free form sources. Note that this can generally be changed by some compiler switches, and that the most recent versions of the Fortran Package Manager (fpm) considers by default that all sources are free form, regardless the extension.

*Note: a common misconception is that the `.f90` source files are restricted to the Fortran 90 revision of the standard and cannot contain features introduced in more recent revisions (Fortran 95/2003/2008/2018). **This is wrong and completely unrelated**: the only reason why `.f90` has been chosen is that the free form has been introduced in the Fortran 90 revision. Both `.f` and `.f90` source files can contain features from any revision of the standard.*
