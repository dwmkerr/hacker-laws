import argparse
import markdown
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

# Read environment variables with defaults
TEMPLATE_FILE = os.getenv("TEMPLATE_FILE", "template.html")
MARKDOWN_FILE = os.getenv("MARKDOWN_FILE", "laws.md")
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR", ".")  # Directory where template is stored


def load_template():
    """Load Jinja2 template from the specified directory."""
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    return env.get_template(TEMPLATE_FILE)


def parse_markdown(md_file):
    """Parse a Markdown file and return structured law sections."""
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    sections = md_content.split("\n## ")  # Split by Markdown headings
    laws = []
    for section in sections:
        if section.strip():
            lines = section.split("\n", 1)
            title = lines[0].strip("# ").strip()
            content = markdown.markdown(lines[1] if len(lines) > 1 else "")
            law_id = title.lower().replace(" ", "-")
            laws.append({"title": title, "content": content, "id": law_id})

    return laws


def extract_static_files(html_content, output_dir):
    """Extract linked CSS, JS, and image files and copy them to the output directory."""
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


def generate_site(output_dir):
    """Generate the static HTML file from Markdown and Jinja2 template."""
    print(f"📝 Loading template from: {TEMPLATE_DIR}/{TEMPLATE_FILE}")
    print(f"📖 Loading markdown from: {MARKDOWN_FILE}")
    print(f"💾 Outputting files to: {output_dir}")

    template = load_template()
    laws = parse_markdown(MARKDOWN_FILE)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Render HTML
    html_output = template.render(laws=laws)

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

    generate_site(args.output_dir)
