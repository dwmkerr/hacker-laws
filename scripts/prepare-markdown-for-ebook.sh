#!/usr/bin/env bash
# This script prepares a `hacker-laws.md` file for export to PDF or e-book format.

# Require a version number and get the current date.
version=$1
date=$(date "+%Y-%m-%d")

if [ -z "$version" ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

# Create `hacker-laws.md` with frontmatter and README content in one step.
cat << EOF > hacker-laws.md
---
title: "Hacker Laws"
author: "Dave Kerr, github.com/dwmkerr/hacker-laws"
subtitle: "Laws, Theories, Principles, and Patterns that developers will find useful. ${version}, ${date}."
---

EOF
cat README.md >> hacker-laws.md

# Use a single `sed` command to clean up unwanted lines and emojis in one pass.
sed -i'' -e '/💻📖.*/d' \
         -e 's/❗/Warning/g' \
         -e '/^\[Translations.*/d' \
         -e '/\*.*/d' \
         -e '/    \*.*/d' \
         -e '/## Translations/,$d' hacker-laws.md

echo "hacker-laws.md prepared successfully."
