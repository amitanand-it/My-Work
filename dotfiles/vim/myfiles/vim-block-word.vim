
"=================================================================
"=====| Encapsulate a WORD beteen symbols |======================
"=================================================================
let s:symbol_map = {
    \   '[': '[]', ']': '[]',
    \   '{': '{}', '}': '{}',
    \   '(': '()', ')': '()',
    \}

function! BlockWord() 
   let l:sym=nr2char(getchar())
   try 
   let sym = s:symbol_map[l:sym]
   catch 'Key.*not.*Dictionary'
          let sym = l:sym. l:sym 
   endtry
   execute "silent normal! ciw" . sym . "\<ESC>P"
endfunction
"=================================================================
noremap <silent> <leader><leader> :call BlockWord()<cr>
"=================================================================

