program fpm_search
  use julienne_m, only : file_t, command_line_t
  use package_index_m, only : package_index_t
  implicit none

  type(command_line_t) command_line
  character(len=:), allocatable :: search_string

  search_string = command_line%flag_value("--find")

  if (len(search_string)==0 .or. command_line%argument_present([character(len=len("--help")) :: ("--help"), "-h"])) then
    stop                             new_line('') // new_line('') &
      // 'Usage:'                 // new_line('') // new_line('') &
      // '  fpm run \'                            // new_line('') &
      // '    --compiler <compiler-name> \'       // new_line('') &
      // '    --profile release \'                // new_line('') &
      // '    -- [--help|-h] | [--find <string>]' // new_line('') // new_line('') &
      // 'where pipe-separated square brackets indicate alternative optional arguments' // new_line('') &
      // 'and angular brackets indicate user input values.'       // new_line('')
  end if

  block
    character(len=*), parameter :: index_url_base = "https://raw.githubusercontent.com/fortran-lang/webpage/refs/heads/main/data/"
    character(len=*), parameter :: index_path = "build/"
    character(len=*), parameter :: index_file = "package_index.yml"
    integer exit_status

    call execute_command_line( &
      command = "curl --silent -L " // index_url_base // index_file // " > " // index_path // index_file, &
      wait = .true., &
      exitstat = exit_status &
    )

    if (exit_status /= 0) then
      call execute_command_line( &
         command  = "wget --quiet -O " // index_path // index_file // " " // index_url_base // index_file &
        ,wait     = .true. &
        ,exitstat = exit_status &
      )
    end if

    associate(package_index => package_index_t(file_t(index_path // index_file)))
      associate(search_results => package_index%find(search_string))
        if (trim(adjustl(search_results)) == "") then
          print '(a)',"No packages found."
          stop ! work around malloc error in gfortran 13-16
        else
          print '(a)', new_line('') // search_results
        end if
      end associate
    end associate

  end block

end program fpm_search