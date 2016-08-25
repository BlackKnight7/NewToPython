set nocompatible              " be iMproved, required
filetype off                  " required

" ============================================================================
" Plugins
" ============================================================================
set rtp+=$VIM/vimfiles/bundle/Vundle.vim/  
call vundle#begin('$VIM/vimfiles/bundle/')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'altercation/vim-colors-solarized'
Plugin 'jnurmine/Zenburn'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'kien/ctrlp.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'davidhalter/jedi-vim'

" python-mode VIM plugin seems to conflict with jedi-vim, therefore you should disable it before enabling jedi-vim.
" Plugin 'klen/python-mode'

" use python-mode instead of others.
" Plugin 'tmhedberg/SimpylFold'  
" Plugin 'scrooloose/syntastic'
" Plugin 'nvie/vim-flake8'

" don't know why can not use this git plugin in windows
" Plugin 'tpope/vim-fugitive'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required


" ============================================
" Plugin settings
" ============================================
" vim-colors-solarized
if has('gui_running')
  set background=dark
  colorscheme solarized
else
  colorscheme Zenburn
endif

" nerdtree
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

" vim-airline, Smarter tab line
let g:airline#extensions#tabline#enabled = 1

" ============================================================================
" settings
" ============================================================================
" Code Folding
set foldmethod=indent
set foldlevel=99
nnoremap <space> za
" suport utf-8
set encoding=utf-8

" show line number
set nu

" Better copy & paste, when you want to paste large blocks of code into vim
set pastetoggle=<F2>
set clipboard=unnamed

" Bind nohl
" Removes highlight of your last search
" ``<C>`` stands for ``CTRL`` and therefore ``<C-n>`` stands for ``CTRL+n``
noremap <C-n> :nohl<CR>
vnoremap <C-n> :nohl<CR>
inoremap <C-n> :nohl<CR>

syntax on
" ============================================
" Python settings
" ============================================
" Python formats
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |

au BufNewFile,BufRead *.js,*.html,*.css
    \ set tabstop=2 |
    \ set softtabstop=2 |
    \ set shiftwidth=2 |
	

" ============================================
" Default settings after install
" ============================================
" we can ingore these
source $VIMRUNTIME/vimrc_example.vim
"source $VIMRUNTIME/mswin.vim
"behave mswin

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction
