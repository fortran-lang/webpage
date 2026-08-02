module indexed_package_m
  use iso_c_binding, only : c_int
  use julienne_m, only : string_t
  implicit none

  !private
  public :: indexed_package_t

  type indexed_package_t
    !! Encapslate package-specific information from the fortran-lang package_index.yml file
    private
    character(len=:), allocatable :: name_, description_, categories_, tags_
    character(len=:), allocatable :: github_, gitlab_, url_ ! optional (zero length if not present)
    character(len=:), allocatable :: license_, version_     ! optional (zero length if not present)
  contains
    procedure as_text
    procedure contains
  end type

  interface indexed_package_t

    pure module function construct_from_components( &
      name, description, categories, tags, license, version, github, gitlab, url) result(indexed_package)
      !! Construct new indexed_package_t object from components
      implicit none
      character(len=*), intent(in) :: name, description, categories, tags
      character(len=*), intent(in), optional :: github, gitlab, url
      character(len=*), intent(in), optional :: license, version
      type(indexed_package_t) indexed_package 
    end function

    pure module function construct_from_strings(lines) result(indexed_package)
      !! Construct new indexed_package_t object from file lines
      implicit none
      type(string_t), intent(in) :: lines(:)
      type(indexed_package_t) indexed_package 
    end function

    pure module function construct_from_characters(new_line_separated) result(indexed_package)
      !! Construct new indexed_package_t object from file lines
      implicit none
      character(len=*), intent(in) :: new_line_separated
      type(indexed_package_t) indexed_package 
    end function

  end interface

  interface

    pure module function as_text(self) result(text)
      implicit none
      class(indexed_package_t), intent(in) :: self
      character(len=:), allocatable :: text
    end function

    pure module function contains(self, search_string) result(match)
      implicit none
      class(indexed_package_t), intent(in) :: self
      character(len=*), intent(in) :: search_string
      logical match
    end function

  end interface

end module indexed_package_m