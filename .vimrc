set nocompatible               " be iMproved
filetype off                   " required!

" ============================================================================
" Plugins
" ============================================================================
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'

" My Bundles here:
Plugin 'altercation/vim-colors-solarized'
Plugin 'jnurmine/Zenburn'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'kien/ctrlp.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'davidhalter/jedi-vim'

filetype plugin indent on     " required!

" ============================================
" Plugin settings
" ============================================
" vim-colors-solarized
set background=dark
colorscheme solarized

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
