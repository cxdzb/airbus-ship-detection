@echo off
chcp 65001
cls

set ARTICLE=tjumain
latex -synctex=1 %ARTICLE%
bibtex %ARTICLE%
latex -synctex=1 %ARTICLE%
latex -synctex=1 %ARTICLE%
dvipdfmx  %ARTICLE%.dvi
call clean
