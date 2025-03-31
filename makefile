default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: prepare-markdown
prepare-markdown: # Prepare the markdown for PDF output.
	./scripts/prepare-markdown-for-ebook.sh "README.md" "hacker-laws.md"

.PHONY: create-pdf
create-pdf: # Create the PDF.
	docker run --rm \
		--platform linux/amd64 \
		-v ${PWD}:/data \
		pandoc/latex:3.6 \
		-V toc-title:"Table Of Contents" \
		--toc \
		--pdf-engine=lualatex \
		--standalone \
		--output hacker-laws.pdf \
		hacker-laws.md
