SHELL := /bin/bash
TEMPLATE_FILE=index.html.jinja
MARKDOWN_FILE=../../README.md
OUTPUT_FILE=index.html
TEMPLATE_DIR=.
default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: install
install: # 📦 install dependencies
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt

.PHONY: build
build: #🔨 building static site
	@echo "🔨 Building static site..."
	TEMPLATE_FILE=$(TEMPLATE_FILE) MARKDOWN_FILE=$(MARKDOWN_FILE) OUTPUT_FILE=$(OUTPUT_FILE) TEMPLATE_DIR=$(TEMPLATE_DIR) \
	python generate_site.py --build

.PHONY: serve
serve: # 🚀 start local server
	@echo "🚀 Starting local server at http://localhost:8000..."
	python3 -m http.server 8000

.PHONY: watch
watch: # 👀 Watch for changes...
	@echo "👀 Watching for changes..."
	watchmedo shell-command --patterns="$(MARKDOWN_FILE);*.py" --command="make build" .

.PHONY: clean
clean: #🧹 Clean up generated files
	@echo "🧹 Cleaning up generated files..."
	rm -f $(OUTPUT)
