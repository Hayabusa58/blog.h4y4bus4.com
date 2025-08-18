#!/usr/bin/env python3
import os
import sys
from datetime import datetime
from jinja2 import Template

template_str = """+++
title = "{{ title }}"
date = "{{ date }}"
+++
"""

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_post.py <title> <output_dir>")
        sys.exit(1)

    title = sys.argv[1]
    output_dir = sys.argv[2]
    date_str = datetime.now().strftime("%Y-%m-%d")

    template = Template(template_str)
    rendered = template.render(title=title, date=date_str)

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "index.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)
        print(f"Successfully generate new dir: {title}")

if __name__ == "__main__":
    main()
