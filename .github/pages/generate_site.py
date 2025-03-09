import argparse
import markdown
import os
from jinja2 import Environment, FileSystemLoader

# Read environment variables with defaults
TEMPLATE_FILE = os.getenv("TEMPLATE_FILE", "template.html")
MARKDOWN_FILE = os.getenv("MARKDOWN_FILE", "laws.md")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "output.html")
TEMPLATE_DIR = os.getenv("TEMPLATE_DIR", ".")


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
            # Skip sections which do not need to be processed.
            #  print(f"found title: {title}")
            #  if "hacker-laws" in title:
            #      continue
            content = markdown.markdown(lines[1] if len(lines) > 1 else "")
            law_id = title.lower().replace(" ", "-")
            laws.append({"title": title, "content": content, "id": law_id})

    return laws


def generate_site():
    """Generate the static HTML file from Markdown and Jinja2 template."""
    print(f"📝 Loading template from: {TEMPLATE_DIR}/{TEMPLATE_FILE}")
    print(f"📖 Loading markdown from: {MARKDOWN_FILE}")
    print(f"💾 Outputting HTML to: {OUTPUT_FILE}")

    template = load_template()
    laws = parse_markdown(MARKDOWN_FILE)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(template.render(laws=laws))

    print(f"✅ Static site generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a static site from Markdown.")
    parser.add_argument("--build", action="store_true", help="Build the static site.")
    args = parser.parse_args()

    if args.build:
        generate_site()
