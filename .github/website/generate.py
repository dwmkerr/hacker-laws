"""Generate the Hacker Laws website from the Hacker Laws README"""
import argparse
import os
import shutil
from jinja2 import Environment, FileSystemLoader
import markdown
from bs4 import BeautifulSoup


def bisect_text(content: str, bisect_line: str) -> tuple[str, str]:
    lines = content.splitlines()
    head = []
    tail = []
    found = False
    for line in lines:
        if found is False and line == bisect_line:
            found = True
            continue
        if found:
            tail.append(line)
        else:
            head.append(line)

    return ("\n".join(head), "\n".join(tail))


def load_template():
    """Load Jinja2 template from the specified directory."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    return env.get_template(TEMPLATE_FILE)


def prepare_markdown(path: str) -> str:
    """
    Pre-process the README markdown by removing content we will not show in
    the final website.
    """

    # Load the markdown content.
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def parse_markdown(markdown_content: str):
    (_, remains) = bisect_text(markdown_content, "<!-- vim-markdown-toc GFM -->")
    (_, content) = bisect_text(remains, "<!-- vim-markdown-toc -->")

    md = markdown.Markdown(extensions=['toc'])
    md.convert(content)
    toc = md.toc

    markdown_sections = content.split("\n#")  # Split by Markdown headings
    sections = []
    laws = []
    for markdown_section in markdown_sections:
        if markdown_section.strip():
            lines = markdown_section.split("\n", 1)
            title = lines[0].strip("# ").strip()
            content = md.convert(lines[1] if len(lines) > 1 else "")
            full_content = md.convert(markdown_section)
            id = title.lower().replace(" ", "-")
            laws.append({"title": title, "content": content, "id": id})
            sections.append({
                "title": title,
                "content": content,
                "id": id,
                "full_content": full_content
            })

    return (sections, toc)


def extract_static_files(html_content, output_dir):
    """
    Extract linked CSS, JS, and image files and copy them to the output
    directory.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    files_to_copy = []

    # Extract <link> stylesheets
    for link in soup.find_all("link", href=True):
        href = link["href"]
        if not href.startswith(("http", "//")):  # Ignore external links
            files_to_copy.append(href)

    # Extract <script> files
    for script in soup.find_all("script", src=True):
        src = script["src"]
        if not src.startswith(("http", "//")):
            files_to_copy.append(src)

    # Extract <img> files
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if not src.startswith(("http", "//")):
            files_to_copy.append(src)

    # Copy files to the output directory
    for file_path in files_to_copy:
        src_path = os.path.join(TEMPLATE_DIR, file_path)
        dest_path = os.path.join(output_dir, file_path)

        if os.path.exists(src_path):  # Ensure file exists before copying
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(src_path, dest_path)
            print(f"📂 Copied: {src_path} → {dest_path}")
        else:
            print(f"⚠️ Warning: Missing file {src_path} (skipping)")

    return files_to_copy


def generate_site(markdown_content: str, output_dir: str):
    """Generate the static HTML file from Markdown and Jinja2 template."""

    template = load_template()
    (sections, toc) = parse_markdown(markdown_content)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Render HTML
    html_output = template.render(toc=toc, sections=sections)

    # Save HTML to output directory
    output_file = os.path.join(output_dir, "index.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_output)

    print(f"✅ Static site generated: {output_file}")

    # Copy static files (CSS, JS, images)
    extract_static_files(html_output, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a static site from Markdown.")
    parser.add_argument("-o", "--output-dir", default="build", help="Directory to save the generated site.")
    args = parser.parse_args()

    # Read environment variables with defaults
    TEMPLATE_FILE = os.getenv("TEMPLATE_FILE", "template.html")
    TEMPLATE_DIR = os.getenv("TEMPLATE_DIR", ".")
    template_path = f"{TEMPLATE_DIR}/{TEMPLATE_FILE}"
    markdown_path = os.getenv("MARKDOWN_FILE", "laws.md")
    output_dir = args.output_dir
    print(f"📝 Loading template from: {template_path}")
    print(f"📖 Loading markdown from: {markdown_path}")
    print(f"💾 Outputting files to: {output_dir}")

    # First, extract that markdown that we want to process.
    markdown_content = prepare_markdown(markdown_path)

    # Generate the site from the markdown.
    generate_site(markdown_content, args.output_dir)
