let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
exe "cd " . escape(expand("<sfile>:p:h"), ' ')
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 __main__.py
badd +1 population/population.py
badd +1 phenotype/phenotype.py
badd +1 individual/individual.py
badd +1 gene_network/geneNetwork.py
badd +1 ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat_func/__main__.py
badd +1 config/config.py
badd +1 geneNetwork/geneNetwork.py
badd +1 stats/stats.py
badd +0 stats/networks.py
badd +0 stats/profiles.py
argglobal
silent! argdel *
argadd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/__main__.py
argadd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/population/population.py
argadd phenotype/phenotype.py
argadd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/individual/individual.py
argadd gene_network/geneNetwork.py
set stal=2
edit __main__.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
edit __main__.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 43 - ((42 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
43
normal! 025|
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/config/config.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/config/config.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/population/population.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
2argu
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/geneNetwork/geneNetwork.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/geneNetwork/geneNetwork.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/stats/stats.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/stats/stats.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 3 - ((2 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
3
normal! 025|
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/stats/profiles.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 119 + 119) / 239)
exe 'vert 2resize ' . ((&columns * 119 + 119) / 239)
argglobal
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/stats/profiles.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
wincmd w
argglobal
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat/stats/networks.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 1 - ((0 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
wincmd w
exe 'vert 1resize ' . ((&columns * 119 + 119) / 239)
exe 'vert 2resize ' . ((&columns * 119 + 119) / 239)
tabedit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat_func/__main__.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
5argu
edit ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat_func/__main__.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 144 - ((24 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
144
normal! 034|
lcd ~/Programmation/Cours/BIG_M1/PRJ/genomat/genomat
tabnext 6
set stal=1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
