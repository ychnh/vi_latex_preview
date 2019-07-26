# vi_latex_preview
![](s1.png)

Scans the latex expression that your cursor is closest to on the current line and displays this as an output.

# Requirements
* vim python3
  * :call echo('python3')
* sympy
* latex interpreter
* opencv
* A font that support braille (Dejavu Sans - works best for me so far)
  * Ok so we probably want to inject the braile font into the standard terminal font because variable pitch is bad. like really bad.
  * http://www.alanwood.net/unicode/fontsbyrange.html#u2800

# Installation
* Use your favorite Plugin manger Vim-Plug and add to .vimrc
* Plug 'ychnh/vi_latex_preview'

* and bind to use
  * nnoremap \<F2\> :call latex#Ltx()<CR>
