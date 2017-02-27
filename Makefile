CHAPTERS=$(wildcard chapters/*.md)

PANDOCARGS=--variable sansfont=Arial --latex-engine=xelatex -f markdown -t latex

pdf: book.pdf
	
book.pdf: book.tex chapters.tex
	pdflatex -shell-escape book.tex
	makeindex book
	pdflatex -shell-escape book.tex
	pdflatex -shell-escape book.tex

chapters.tex: chapters.md
	pandoc chapters.md -o chapterstmp.tex $(PANDOCARGS)
	cat chapterstmp.tex | python process.py > chapters.tex

chapters.md: $(CHAPTERS)
	$(foreach f,$(CHAPTERS), cat $(f)  >> chapters.md; echo "\n\n" >> chapters.md;)

clean:
	rm -f chapters.tex chapters.md chapterstmp.tex
	rm -f book.idx book.ilg book.ind book.aux book.log book.out book.pdf book.toc chapters.md chapters.tex texput.log
