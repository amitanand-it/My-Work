
function! FindFile()

    " By default searcing is done in current directory.
    " dir_hash helps to search in other mentioned path
    let dir_hash = { 
        \   "GD/Graph.pm" : "/usr/share/perl5/",
        \   "Log/Log4perl.pm" : "/usr/share/perl5/",
        \   "Date/Calc.pm" : "/usr/share/perl5/",
        \   "File/Basename.pm" : "/usr/share/perl5",
        \   "Data/Dumper.pm" : "/usr/lib/",
        \   "HTML/FillInForm.pm" : "/usr/share/",
        \   "Time/HiRes.pm" : "/usr/lib/",
        \ }

    " hint_hash can be used if there are multiple files or specific
    " word and you give hint to the program which file should be used
    let hint_hash = {
        \   "Utils/FillInForm.pm" : "perl_modules_02/Utils.pm",
        \   "Utils.pm" : "perl_modules_02/Utils.pm",
        \   "Conf.pm" : 'perl_modules_02/Conf.pm',
        \   "Log/Log4perl.pm" : 'perl5/Log/Log4perl.pm',
        \   "/products_details.html" : "common/products_details.html",
        \   "/common/captcha.html" : "tradeshows/common/captcha.html",
        \   "$b2bglobal{current_user}" : 'perl_modules_02/B2B/User.pm',
        \   "$b2bglobal{current_employee}" : 'perl_modules_01/Erp/Employee.pm',
        \   "$b2bglobal{current_profile}" : 'perl_modules_02/B2B/Company.pm',
        \ }

    let module_cook = 0
    let file = ''
    let cfile = expand('<cfile>')
    let cfile = substitute(cfile,'\(\.html\).*','\1','g')

    let WORD = expand('<cWORD>')
    let WORD = substitute(WORD,'^.\{-}\(\$b2bglobal{.\{-}}\).*$','\1','g')

    if(has_key(hint_hash, cfile))
        let cfile = get(hint_hash, cfile)
    elseif(has_key(hint_hash, WORD))
        let cfile = get(hint_hash, WORD)
    elseif(match(cfile, '\.html$') >= 0)
        " if html file 
        let cfile = substitute(cfile,'^http\(s\)\?://.\{-}/','/','g')
        let cfile = substitute(cfile,'^/opt.*mason','','g')
    elseif(match(cfile, '::') >= 0)
        let module_cook = 1
    else
        " There must be some text selected under the cursor
        " only then request will check for variable
        if(!empty(cfile))
            let cfile = FindVariable()
            if(has_key(hint_hash, cfile))
                let cfile = get(hint_hash, cfile)
            else
                let module_cook = 1
            endif
        endif
    endif

    if(module_cook && match(cfile, '::') >= 0)
        let cfile = substitute(cfile,'^.\{-}\(\w\+\(::\w\+\)\+\).*$','\1','g') 
        let cfile = substitute(cfile,'\C\(::[-_A-Z0-9]\+\)\+$','','g') 
        let cfile = substitute(cfile,'\C\(::[-_a-z0-9]\+\)\+$','','g') 
        let cfile = substitute(cfile,'::','/','g') . '.pm' 
    endif

    if(empty(cfile))
        return
    endif

    let dir = ''
    if(has_key(dir_hash, cfile))
        let dir = get(dir_hash, cfile)
    endif

    let cmd = "find ". dir ." 2>/dev/null | grep -vP '\.(obj|swp)$' | grep '".cfile."'" 
    echo cmd

    let file_count = system(cmd . ' | wc -l ')
    if(file_count == 1)
        let cfile=system(cmd)
        let cfile= substitute(cfile,'\n\+$','','g') 
        if(filereadable(cfile))
            let file = cfile 
        endif
    elseif(file_count > 1)
        let file_count= substitute(file_count,'\n\+$','','g') 
        echo "There are " . file_count . " files with " . cfile
    endif
"    echo file
"    return
"""""""""""""""""""""
    if(filereadable(file))
        if(match(file, '.pm$') >= 0)
            exec ':tabnew ' .  file
        else 
            exec ':e ' .  file
        endif
    else
"        echo '  '
        echo '!! No file found !!'
    endif

endfunction

function! FindVariable()

    let word = expand('<cword>')
    let variable = '$' . word

    let current_line_number = line('.')    
    execute "silent normal! ma"
    while(variable != '$')
        try 
        " checking for line exists with ' variable = '
        execute "silent normal! gg/^[^#]*" . variable . ".*\=\<cr>"                                                      
        catch 'Pattern not found'
            exec ':' . current_line_number 
            break
        endtry

        let list = matchlist(getline("."), variable .  '\s\{-}=\s\{-}\(\$\w\+\).*$')
        if(empty(list))
            break
        endif

        let variable = list[1]

        if(match(variable, 'b2bglobal') >= 0)
            let current_line = getline(".")
            let variable = substitute(current_line,'^.\{-}\(\$b2bglobal{.\{-}}\).*$','\1','g')
        endif

    endwhile

    let initial_line = getline(".")
    execute "silent normal! `a"

    if(match(variable, '^\$b2bglobal{.\{-}}$') >= 0)
        return variable
    endif

    let term = substitute(initial_line,'\C^.\{-}=\U\+\|[^-_A-Za-z0-9:].*$','','g')
    return term

endfunction
