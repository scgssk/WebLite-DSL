import os
import shutil
import yaml
import re

# 🧱 Prepare output folder
def init_output():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "output")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    return output_dir

# 🧠 Markdown-like formatting
def format_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"\*\*([^\*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<em>\1</em>", text)
    text = re.sub(r"\*_(.+?)_\*", r"<strong><em>\1</em></strong>", text)
    return text


# 🔧 Render HTML tag with optional style
def render_tag(tag, value, style_attr=""):
    value = format_text(value)
    if tag == "img":
        return f"<img src='{value}' {style_attr}/>"
    elif tag == "a":
        return f"<a href='{value}' {style_attr}>{value}</a>"
    elif tag == "button":
        return f"<button {style_attr}>{value}</button>"
    else:
        return f"<{tag} {style_attr}>{value}</{tag}>"

# 🎯 Map keys like "Title" to tags like "h1"
def render_semantic(key, value, style_attr=""):
    mapping = {
        "Title": "h1",
        "Subtitle": "h2",
        "Description": "p",
        "CTA": "button",
        "Image": "img",
        "Link": "a",
        "Note": "p",
        "Paragraph": "p",
        "Text": "p",
    }
    tag = mapping.get(key, key.lower())
    return render_tag(tag, value, style_attr)

# 🔼 Navigation bar
def generate_nav(nav_items, nav_style=None):
    style_attr = ""
    if nav_style:
        style_str = "; ".join(f"{k}:{v}" for k, v in nav_style.items())
        style_attr = f' style="{style_str}"'

    html = f"<nav{style_attr}>\n"
    for item in nav_items:
        html += f"<a href='{item.lower()}.html'>{item}</a>\n"
    html += "</nav>\n"
    return html

# 🔽 Footer bar
def generate_footer(footer_content):
    html = "<footer>\n"
    if isinstance(footer_content, dict):
        for key, value in footer_content.items():
            html += render_semantic(key, value) + "\n"
    elif isinstance(footer_content, str):
        html += render_semantic("Text", footer_content) + "\n"
    html += "</footer>\n"
    return html

def parse_key_and_style(raw_key):
    if ">>" in raw_key:
        key, style_def = raw_key.split(">>", 1)
        key = key.strip()
        style_parts = [s.strip() for s in style_def.split(";") if s.strip()]
        style_attr = f'style="{"; ".join(style_parts)}"'
    else:
        key = raw_key.strip()
        style_attr = ""
    return key, style_attr



# 🧩 Section with component and section-wide styling
def generate_section(section_name, section_content):
    html = ""

    # Section-wide styles
    section_style = ""
    if isinstance(section_content, dict) and "style" in section_content:
        style_dict = section_content["style"]
        style_str = "; ".join(f"{k.strip()}:{v.strip()}" for k, v in style_dict.items())
        section_style = f' style="{style_str}"'

    html += f"<section{section_style}>\n<!-- {section_name} section -->\n"

    # Render all content inside the section
    for raw_key, raw_value in section_content.items():
        if raw_key == "style":
            continue

        # If value is a list of styled or plain items (e.g., list of Paragraphs, Images, etc.)
        if isinstance(raw_value, list) and all(isinstance(item, dict) for item in raw_value):
            for item in raw_value:
                for sub_key, sub_value in item.items():
                    key, style_attr = parse_key_and_style(sub_key)
                    html += render_semantic(key, sub_value, style_attr) + "\n"
        else:
            key, style_attr = parse_key_and_style(raw_key)
            html += render_semantic(key, raw_value, style_attr) + "\n"

    html += "</section>\n"
    return html



# 🖥️ Full page structure
def generate_page(page_name, page_content, global_nav=None, global_footer=None, nav_style=None):
    html = "<!DOCTYPE html>\n<html>\n<head>\n"
    html += f"<title>{page_name}</title>\n"
    html += "<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n"

    if global_nav:
        html += generate_nav(global_nav, nav_style)

    for section_name, section_content in page_content.items():
        html += generate_section(section_name, section_content)

    if global_footer:
        html += generate_footer(global_footer)

    html += "\n</body>\n</html>"
    return html

# 🎨 Default styling
def generate_css():
    return """
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
nav {
  background: #333;
  padding: 10px;
  text-align: center;
}
nav a {
  color: white;
  margin: 0 15px;
  text-decoration: none;
}
section {
  padding: 20px;
}
footer {
  background-color: #222;
  color: white;
  text-align: center;
  padding: 15px;
  position: relative;
  bottom: 0;
  width: 100%;
}
img {
  max-width: 100%;
  height: auto;
}
button {
  cursor: pointer;
  padding: 10px 20px;
  font-size: 1em;
  margin-top: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}
"""

# 🚀 Builder entry
def build(input_file):
    output_dir = init_output()

    with open(input_file, "r", encoding="utf-8") as f:
        site = yaml.safe_load(f)

    global_nav = site.get("Nav")
    global_footer = site.get("Footer")
    nav_style = site.get("NavStyle")

    for page_name, page_content in site.items():
        if page_name in ("Nav", "Footer", "NavStyle"):
            continue

        html = generate_page(page_name, page_content, global_nav, global_footer, nav_style)
        with open(os.path.join(output_dir, f"{page_name.lower()}.html"), "w") as f:
            f.write(html)

    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(generate_css())
