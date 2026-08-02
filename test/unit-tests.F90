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
             assert_text =>   assert_package%as_text() &
          ,caffeine_text => caffeine_package%as_text() &
          ,  formal_text =>   formal_package%as_text() &
          ,julienne_text => julienne_package%as_text() &
        )
          call report_result(packages%find("caffeine")  == caffeine_text, " finding a package with no optional data")
          call report_result(packages%find("formal")    ==   formal_text, " finding a package with optional license & version")
          call report_result(packages%find("julienne")  == julienne_text, " finding a package listed after a section header")
          call report_result(packages%find("numerical") ==   formal_text, " finding a package based on category text")
          call report_result(packages%find("fake")      ==            "", " returning zero-length text for a missing package")
          call report_result(packages%find("assert")    == julienne_text // assert_text, " finding two matching packages")
          stop ! work around gfortran 13-16 seg faults
        end associate capture_package_entry_text
      end associate define_index_and_package_entries
    end associate define_package_index_file_object
  end associate define_package_index_items
contains

  subroutine report_result(test_condition, test_description)
    logical, intent(in) :: test_condition
    character(len=*), intent(in) :: test_description
    print '(a)', "  " // merge("passes on", "FAILS  on", test_condition)// test_description
  end subroutine

end program unit_tests
