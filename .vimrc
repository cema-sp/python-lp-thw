" set keymap to use [Ctrl+^] for keymap switching
set keymap=russian-jcukenwin
" set default keymap to English
set iminsert=0
set imsearch=0
" Ignore register on search
set ic
" highlight search
set hls
" set [TAB] size to 4 spaces
set ts=2
" show line numbers
set number
" use spaces in case of TAB
set expandtab
" set TAB size in spaces
set softtabstop=2
" indentation size
set shiftwidth=2

set autoindent
set smartindent
set cindent

if has ("autocmd")
    " File type detection. Indent based on filetype. Recommended.
    filetype plugin indent on
endif

