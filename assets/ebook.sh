#!/usr/bin/env bash
#
# Requirements:
# - pandoc
# - xelatex
# brew install 
# brew cask install basictex

# First, we need to make a copy of the README, which we will modify slighty.
cp README.md hacker-laws.md

# Remove the title - we have it in the front-matter of the doc, so it will
# automatically be added to the PDF.
sed -i '' '/💻📖.*/d' hacker-laws.md

# We can't have emojis in the final content with the PDF generator we're using.
sed -i '' 's/❗/Warning/' hacker-laws.md

# Now rip out the translations line.
sed -i '' '/^\[Translations.*/d' hacker-laws.md

# # Now rip out any table of contents items.
sed -i '' '/\*.*/d' hacker-laws.md
sed -i '' '/    \*.*/d' hacker-laws.md

# Delete everything from 'Translations' onwards (we don't need the translations
# lists, related projects, etc).
sed -i ' ' '/## Translations/,$d' hacker-laws.md

# Now build the e-book as a PDF.
pandoc  -V toc-title:"Table Of Contents" --toc --pdf-engine=pdflatex -s -o hacker-laws.pdf hacker-laws.md
