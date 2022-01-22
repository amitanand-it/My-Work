"=================================================================
"=====| Comment Lines using comment symbol |======================
"=================================================================
let s:comment_map = {
    \   "c": '//', "cpp": '//', "java": '//', "javascript": '//', "php": '//',
    \   "python": '#', "ruby": '#', "sh": '#', "fstab": '#', "conf": '#', 
    \   "profile": '#', "bashrc": '#', "bash_profile": '#', "perl": '#',
    \   "vim": '"',
    \ }

let s:comment_symbol= {"%": '%#', "/": '//' }

let g:comment_sym = ''
function! CommentLines() 
    if getline('.') =~ '^\s*\([#"]\|%#\|//\)'
"        uncomment
        execute 'silent s!^\(\s*\)\(["#]\|%#\|//\)!\1!g'
    else

       if has_key(s:comment_map, &filetype)
          let g:comment_sym = s:comment_map[&filetype]
      elseif &filetype == "mason"
            execute "silent normal! ma"
            execute "silent normal! ?\\(<%\\|<script\\|</script>\\)\<cr>ll"
            let block_name = expand('<cWORD>')
            execute "silent normal! 'a"

            let g:comment_sym = '%#'
            if block_name == "<%perl>" || block_name == "<%args>" || block_name == "<%attr>"
                    let g:comment_sym = '#'
            elseif block_name == "<%doc>"
                    let g:comment_sym = '%'
            elseif block_name =~ "<script"
                    let g:comment_sym = '//'
            endif
       endif

       if(empty(g:comment_sym))
           let char = getchar()
           let g:comment_sym= char == 13 ? '%#' : nr2char(char)
       endif

       if has_key(s:comment_symbol, g:comment_sym)
           let sym = s:comment_symbol[g:comment_sym]
       else
           let sym = g:comment_sym
       endif

       execute "silent normal! :s!^!". sym . "!\<CR>"

       if(line(".") == a:lastline)
           let g:comment_sym=''
       endif
   endif
endfunction

"=================================================================
"nnoremap <silent> <leader>cc :call CommentLines()<cr>
"vnoremap <silent> <leader>cc :call CommentLines()<cr>
"=================================================================

