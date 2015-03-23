SOURCE=report

all: compile show clean

clean:
	- rm *.aux *.log 

show:
	evince $(SOURCE).pdf

compile:
	pdflatex $(SOURCE).tex && pdflatex $(SOURCE).tex

