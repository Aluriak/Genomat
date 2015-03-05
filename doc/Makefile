SOURCE=report

all: move source clean

clean:
	- rm *.aux *.log 

show:
	evince $(SOURCE).pdf

source:
	pdflatex $(SOURCE).tex && pdflatex $(SOURCE).tex
	$(MAKE) show

move:
	- cp ../data/stats.csv ./

