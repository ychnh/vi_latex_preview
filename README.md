# vi_latex_preview

On a per line basis shows the latex output in vim.
# Requirements
* vim python3
  * :call echo('python3')
* sympy
* latex interpreter
* opencv
* A font that support braille (Dejavu Sans - works best for me so far)
  * http://www.alanwood.net/unicode/fontsbyrange.html#u2800

# Installation
* Use your favorite Plugin manger Vim-Plug and add to .vimrc
* Plug 'ychnh/vi_latex_preview'

* and bind to use
  * nnoremap \<F2\> :call latex#Ltx()<CR>
