program unit_tests
  !! Test the package-search library functions
  use julienne_m, only : file_t, string_t
  use indexed_package_m, only : indexed_package_t
  use package_index_m, only : package_index_t
  implicit none

  ! ______ Test data ______
  define_package_index_items: &
  associate( &
    formal => [ &
       string_t("- name: formal") &
      ,string_t("  github: BerkeleyLab/formal") &
      ,string_t("  description: Formulaic mimetic abstraction language") &
      ,string_t("  categories: numerical") &
      ,string_t("  tags: partial-differential-equations domain-specific-language mimetic-discretizations") &
      ,string_t("  license: BSD") &
      ,string_t("  version: 0.3.0") &
    ] &
    ,julienne => [ &
       string_t("- name: julienne") &
      ,string_t("  github: berkeleylab/Julienne") &
      ,string_t("  description: A correctness-checking framework supporting expressive idioms for writing assertions and tests") &
      ,string_t("  categories: testing") &
      ,string_t("  tags: unit-testing assertions pure-procedure-diagnostic-output") &
      ,string_t("  version: 3.4.1") &
    ] &
    ,assert => [ &
         string_t("- name: assert") &
        ,string_t("  url: https://github.com/BerkeleyLab/assert") &
        ,string_t("  description: A library for the run-time checking of program invariants and for providing diagnostic error output inside pure procedures") &
        ,string_t("  categories: testing") &
        ,string_t("  tags: programming-utilities learning high-performance-computing") &
        ,string_t("  license: BSD") &
    ] &
    ,caffeine => [ &
       string_t("- name: caffeine") &
      ,string_t("  github: BerkeleyLab/Caffeine") &
      ,string_t("  description: CoArray Fortran Framework of Efficient Interfaces to Network Environments") &
      ,string_t("  categories: compiler") &
      ,string_t("  tags: parallel-runtime-library prif llvm-flang lfortran gasnet") &
    ] &
  )
    define_package_index_file_object: &
    associate( &
      berkeley_packages => file_t([ &
         string_t("# File Header") &
        ,string_t("#") &
        ,formal &
        ,string_t("") &
        ,string_t("# Section Header") &
        ,julienne &
        ,string_t("") &
        ,assert &
        ,string_t("") &
        ,caffeine &
      ]))

      ! ______ Test subject ______
      print '(a)', "The package-search program"

      ! ______ Tests ______
      define_index_and_package_entries: &
      associate( &
                 packages => package_index_t(berkeley_packages) &
        ,  assert_package => indexed_package_t(assert) &
        ,caffeine_package => indexed_package_t(caffeine) &
        ,  formal_package => indexed_package_t(formal) &
        ,julienne_package => indexed_package_t(julienne) &
      )
        capture_package_entry_text: &
        associate( &
             assert_txt =>   assert_package%as_text() &
          ,caffeine_txt => caffeine_package%as_text() &
          ,  formal_txt =>   formal_package%as_text() &
          ,julienne_txt => julienne_package%as_text() &
        )
          block
            integer :: tests = 0, passes = 0
            call test(packages%find("caffeine")  == caffeine_txt, " finding a package with no optional data", tests, passes)
            call test(packages%find("formal")    ==   formal_txt, " finding a package with optional license/version", tests, passes)
            call test(packages%find("julienne")  == julienne_txt, " finding a package listed after a section header", tests, passes)
            call test(packages%find("numerical") ==   formal_txt, " finding a package based on category text", tests, passes)
            call test(packages%find("fake")      ==            "", " returning blank text for a missing package", tests, passes)
            call test(packages%find("assert")    == julienne_txt // assert_txt, " finding two matching packages", tests, passes)
            if (passes /= tests) then
              print fmt(tests), "______ ", tests - passes, " of ", tests, " tests failed. ______"
              error stop
            else
              print fmt(tests), "All ", tests, " tests passed."
#ifdef __GFORTRAN__
              stop ! work around gfortran 13-16 seg faults
#endif
            end if
          end block
        end associate capture_package_entry_text
      end associate define_index_and_package_entries
    end associate define_package_index_file_object
  end associate define_package_index_items
contains

  subroutine test(test_condition, test_description, num_tests, num_passes)
    logical, intent(in) :: test_condition
    integer, intent(inout) :: num_tests, num_passes
    character(len=*), intent(in) :: test_description
    print '(a)', "  " // merge("passes on", "FAILS  on", test_condition)// test_description
    num_tests = num_tests + 1
    num_passes = num_passes + merge(1, 0, test_condition)
  end subroutine

  pure function fmt(num_tests)
    integer, intent(in) :: num_tests
    character(len=:), allocatable :: fmt
    select case(num_tests)
    case(0:9)
      fmt = "(*(a,i1))" 
    case(10-99)
      fmt = "(*(a,i2))" 
    case(100-999)
      fmt = "(*(a,i3))" 
    case(1000-9999)
      fmt = "(*(a,i4))" 
    case default
      fmt = "(*(a,i9))" 
    end select
  end function

end program unit_tests
