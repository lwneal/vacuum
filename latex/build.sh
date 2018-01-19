#!/bin/sh
set -e
FILENAME=vacuum

echo "Compiling ${FILENAME}.tex"
pdflatex -interaction=nonstopmode ${FILENAME}.tex
rm -f latex.temp*.jpg

if [[ `uname` == "Darwin" ]]; then
    open ${FILENAME}.pdf
fi
# View in terminal, if imgcat is available
#convert -density 300 ${FILENAME}.pdf latex.temp.jpg
#imgcat latex.temp*.jpg
