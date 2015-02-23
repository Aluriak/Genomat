SOURCE=report

all: move source clean

clean:
	- rm *.aux *.log 

source:
	pdflatex $(SOURCE).tex && pdflatex $(SOURCE).tex
	evince $(SOURCE).pdf

move:
	- cp ../data/stats.csv ./

