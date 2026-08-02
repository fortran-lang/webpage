#include "fortran-lang-compiler-support.F90"

submodule(indexed_package_m) indexed_package_s
  implicit none

contains

  module procedure construct_from_components
    indexed_package%name_        = name
    indexed_package%description_ = description
    indexed_package%categories_  = categories
    indexed_package%tags_        = tags

    if (present(github)) then
      indexed_package%github_ = github
    else
      allocate(character(len=0) :: indexed_package%github_)
    end if

    if (present(gitlab)) then
      indexed_package%gitlab_ = gitlab
    else
      allocate(character(len=0) :: indexed_package%gitlab_)
    end if

    if (present(url)) then
      indexed_package%url_ = url
    else
      allocate(character(len=0) :: indexed_package%url_)
    end if

    if (present(license)) then
      indexed_package%license_ = license
    else
      allocate(character(len=0) :: indexed_package%license_)
    end if

    if (present(version)) then
      indexed_package%version_ = version
    else
      allocate(character(len=0) :: indexed_package%version_)
    end if
  end procedure

  pure function get_key_value(key, lines) result(key_value)
    character(len=*), intent(in) :: key
    type(string_t), intent(in) :: lines(:)
    character(len=:), allocatable :: key_value
    integer l

    do l = 1, size(lines)
      block
        character(len=:), allocatable :: characters
        characters = lines(l)%string()
        if (skip(characters)) cycle
        associate(colon => index(characters, ":"))
          if (colon == 0) error stop "missing key/value separator ':'"
          if (index(characters(1:colon-1), key)/=0)then
            key_value = characters(colon+1:)
            return
          end if
        end associate
      end block
    end do

    key_value = ""

  contains

    pure function skip(line) result(comment_or_blank)
      character(len=*), intent(in) :: line
      logical comment_or_blank

      if (len(trim(line)) == 0) then
         comment_or_blank = .true.
      else
        block
          character(len=:), allocatable :: hash_etc
          hash_etc = adjustl(line)
          if (hash_etc(1:1) == "#") then
            comment_or_blank = .true.
          else
            comment_or_blank = .false.
            return
          end if
        end block
      end if
    end function

  end function

  module procedure construct_from_strings
    indexed_package = construct_from_components( &
       name        =  get_key_value(     "- name", lines) &
      ,description =  get_key_value("description", lines) &
      ,categories  =  get_key_value( "categories", lines) &
      ,tags        =  get_key_value(       "tags", lines) &
      ,github      =  get_key_value(     "github", lines) &
      ,gitlab      =  get_key_value(     "gitlab", lines) &
      ,url         =  get_key_value(        "url", lines) &
      ,license     =  get_key_value(    "license", lines) &
      ,version     =  get_key_value(    "version", lines) &
    )
  end procedure

  module procedure construct_from_characters

    type(string_t), allocatable :: lines(:)
    integer l

    associate(delimiter_locations  => [1, new_line_locations(new_line_separated), len(new_line_separated)])

      allocate(lines(size(delimiter_locations)-1))

      l = 1
      lines(l) = new_line_separated(delimiter_locations(l):delimiter_locations(l+1)-1)

      do l = 2, size(lines)
        lines(l) = new_line_separated(delimiter_locations(l)+1:delimiter_locations(l+1)-1)
      end do

    end associate

    indexed_package = indexed_package_t(lines) 

  contains

    pure function new_line_locations(characters) result(locations)
      character(len=*), intent(in) :: characters
      integer, allocatable :: locations(:), tmp(:)
      integer new_lines, c

      new_lines = 0
      allocate(locations(new_lines))

      do c = 1, len(characters)
        if (characters(c:c) == new_line('')) then
          new_lines = new_lines + 1
          if (new_lines > size(locations)) then 
            call move_alloc(locations, tmp)
            allocate(locations(2*new_lines))
            locations(1:size(tmp)) = tmp 
            deallocate(tmp)
          end if
          locations(new_lines) = c
        end if
      end do

      locations = locations(1:new_lines)

    end function

  end procedure

  module procedure as_text
    text = &
         "- name : "      // self%name_        // new_line('') &
      // "description : " // self%description_ // new_line('') &
      // "categories : "  // self%categories_  // new_line('') &
      // "tags : "        // self%tags_
    if (len(self%github_ )/=0) text = text // new_line('') // "github : "  // self%github_
    if (len(self%gitlab_ )/=0) text = text // new_line('') // "gitlab : "  // self%gitlab_
    if (len(self%url_    )/=0) text = text // new_line('') // "url : "     // self%url_
    if (len(self%license_)/=0) text = text // new_line('') // "license : " // self%license_
    if (len(self%version_)/=0) text = text // new_line('') // "version : " // self%version_
    text = text // new_line('') // new_line('')
  end procedure

  module procedure contains

    match = any(0 /= [ &
       index(lower_case(self%name_)       , lower_case(search_string)) &
      ,index(lower_case(self%description_), lower_case(search_string)) &
      ,index(lower_case(self%categories_) , lower_case(search_string)) &
      ,index(lower_case(self%tags_)       , lower_case(search_string)) &
      ,index(lower_case(self%github_)     , lower_case(search_string)) &
      ,index(lower_case(self%gitlab_)     , lower_case(search_string)) &
      ,index(lower_case(self%url_)        , lower_case(search_string)) &
      ,index(lower_case(self%license_)    , lower_case(search_string)) &
      ,index(lower_case(self%version_)    , lower_case(search_string)) &
    ])

  contains

    pure function lower_case(string) result(lower_case_string)
      character(len=*), intent(in) :: string
      character(len=len(string))   :: lower_case_string

#if HAVE_DO_CONCURRENT_TYPE_SPEC_SUPPORT && HAVE_LOCALITY_SPECIFIER_SUPPORT
      do concurrent(integer :: i = 1:len(string)) default(none) shared(string, lower_case_string)
        associate(char => iachar(string(i:i)))
          lower_case_string(i:i) = merge(achar(char + (iachar('a') - iachar('A'))), string(i:i), char >= iachar('A') .and. char <= iachar('Z'))
        end associate
      end do
#else
      block
      integer i
      do concurrent(           i = 1:len(string))
        associate(char => iachar(string(i:i)))
          lower_case_string(i:i) = merge(achar(char + (iachar('a') - iachar('A'))), string(i:i), char >= iachar('A') .and. char <= iachar('Z'))
        end associate
      end do
      end block
#endif
    end function

  end procedure

end submodule indexed_package_s