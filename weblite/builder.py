import os
import shutil
import yaml
import re

STYLE_ALIASES = {
        "big": "font-size: 36px",
        "medium": "font-size: 24px",
        "small": "font-size: 14px",
        "red": "color: #e74c3c",
        "gray": "color: #888",
        "blue": "color: #2980b9",
        "white": "color: #fff",
        "centered": "text-align: center",
        "padded": "padding: 15px",
        "box": "border: 1px solid #ccc; border-radius: 5px; padding: 10px",
}

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
    if tag == "img":
        if isinstance(value, dict):
            src = value.get("src", "")
        else:
            src = value
        return f"<img src='{src}' {style_attr}/>"
    
    elif tag == "a":
        if isinstance(value, dict):
            href = value.get("href", "#")
            label = value.get("label", href)
        else:
            href = value
            label = value
        return f"<a href='{href}' {style_attr}>{label}</a>"

    elif tag == "button":
        if isinstance(value, dict):
            label = format_text(value.get("label", "Click"))
            onclick = value.get("onclick")
            onclick_attr = f' onclick="{onclick}"' if onclick else ""
            return f"<button {style_attr}{onclick_attr}>{label}</button>"
        else:
            return f"<button {style_attr}>{format_text(value)}</button>"


    else:
        return f"<{tag} {style_attr}>{format_text(value)}</{tag}>"




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
def generate_nav(nav_items):
    style_attr = ""
    links = []

    # Check if the first item is a style dictionary
    if nav_items and isinstance(nav_items[0], dict) and "style" in nav_items[0]:
        style_dict = nav_items[0]["style"]
        style_str = resolve_style_dict(style_dict)
        style_attr = f' style="{style_str}"'
        links = nav_items[1:]
    else:
        links = nav_items

    html = f"<nav{style_attr}>\n"
    for item in links:
        html += f"<a href='{item.lower()}.html'>{item}</a>\n"
    html += "</nav>\n"
    return html

# 🔽 Footer bar
def generate_footer(footer_content, components=None):
    html = ""
    style_attr = ""
    items = []

    if isinstance(footer_content, list):
        for item in footer_content:
            if isinstance(item, dict) and "style" in item:
                style_dict = item["style"]
                style_str = resolve_style_dict(style_dict)
                style_attr = f' style="{style_str}"'
            else:
                items.append(item)
    else:
        items = [footer_content]

    html += f"<footer{style_attr}>\n"

    for item in items:
        if isinstance(item, dict):
            for raw_key, raw_val in item.items():
                key, style = parse_key_and_style(raw_key)
                html += render_semantic(key, raw_val, style) + "\n"
        elif isinstance(item, str):
            # Support footer components like: - SocialIcons
            if components and item in components:
                html += render_component(components[item])
            else:
                html += render_semantic("Paragraph", item) + "\n"

    html += "</footer>\n"
    return html

def resolve_style_dict(style_dict):
    style_parts = []

    for k, v in style_dict.items():
        if v is True and k in STYLE_ALIASES:
            style_parts.append(STYLE_ALIASES[k])
        elif k in STYLE_ALIASES:
            style_parts.append(STYLE_ALIASES[k])
        elif ":" in k:
            style_parts.append(k)  # raw CSS already
        else:
            style_parts.append(f"{k}: {v}")

    return "; ".join(style_parts)

def parse_key_and_style(raw_key):
    if ">>" in raw_key:
        key, style_def = raw_key.split(">>", 1)
        key = key.strip()
        style_parts = []

        # 🥇 If semicolons are present, split by them (best for raw CSS)
        if ";" in style_def:
            raw_styles = [s.strip() for s in style_def.split(";") if s.strip()]
            for token in raw_styles:
                if token in STYLE_ALIASES:
                    style_parts.append(STYLE_ALIASES[token])
                elif ":" in token:
                    style_parts.append(token)
                else:
                    print(f"Unknown style alias or raw CSS: '{token}'")

        # 🥈 If only one colon-style is used (e.g. "border-radius: 8px")
        elif ":" in style_def and style_def.count(":") == 1:
            style_parts.append(style_def.strip())

        # 🥉 Fallback: space-separated parsing
        else:
            tokens = style_def.strip().split()
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if token in STYLE_ALIASES:
                    style_parts.append(STYLE_ALIASES[token])
                    i += 1
                elif ':' in token:
                    style_parts.append(token)
                    i += 1
                elif i + 1 < len(tokens):
                    prop = token
                    val = []
                    i += 1
                    while i < len(tokens) and tokens[i] not in STYLE_ALIASES and ':' not in tokens[i]:
                        val.append(tokens[i])
                        i += 1
                    if val:
                        style_parts.append(f"{prop}: {' '.join(val)}")
                    else:
                        print(f"Malformed CSS property '{prop}'")
                else:
                    print(f"Unknown style token: '{token}'")
                    i += 1

        style_attr = f'style="{"; ".join(style_parts)}"' if style_parts else ""
    else:
        key = raw_key.strip()
        style_attr = ""

    return key, style_attr

def render_component(component_block):
    html = ""
    outer_style = ""

    if isinstance(component_block, dict):
        for sub_key, sub_val in component_block.items():
            key, style_attr = parse_key_and_style(sub_key)
            html += render_semantic(key, sub_val, style_attr) + "\n"

    elif isinstance(component_block, list):
        normal_items = []
        for item in component_block:
            if isinstance(item, dict) and "style" in item:
                style_str = resolve_style_dict(item["style"])
                outer_style = f' style="{style_str}"'
            else:
                normal_items.append(item)

        html += f"<div{outer_style}>\n"
        for sub in normal_items:
            if isinstance(sub, dict):
                for sub_key, sub_val in sub.items():
                    key, style_attr = parse_key_and_style(sub_key)
                    html += render_semantic(key, sub_val, style_attr) + "\n"
        html += "</div>\n"

    return html




# 🧩 Section with component and section-wide styling
def generate_section(section_name, section_content, components=None):
    html = ""
    section_style = ""
    items = []

    # 🧩 Handle section style whether it's at start, end or middle
    if isinstance(section_content, list):
        remaining_items = []
        for item in section_content:
            if isinstance(item, dict) and "style" in item:
                style_dict = item["style"]
                style_str = resolve_style_dict(style_dict)
                section_style = f' style="{style_str}"'
            else:
                remaining_items.append(item)
        items = remaining_items
    elif isinstance(section_content, dict):
        if "style" in section_content:
            style_dict = section_content["style"]
            style_str = resolve_style_dict(style_dict)
            section_style = f' style="{style_str}"'
        items = [{k: v} for k, v in section_content.items() if k != "style"]

    html += f"<section{section_style}>\n<!-- {section_name} section -->\n"

    for item in items:
        if isinstance(item, str) and components and item in components:
            html += render_component(components[item])  # You must define this helper

        elif isinstance(item, dict):
            if "style" in item:
                continue  # already handled
            for raw_key, raw_value in item.items():
                # 🧩 Component with parameters
                if components and raw_key in components and isinstance(raw_value, dict):
                    template = components[raw_key]

                    # 🔁 Extract style from template
                    template_style_dict = {}
                    if isinstance(template, list):
                        for t in template:
                            if isinstance(t, dict) and "style" in t:
                                template_style_dict = t["style"]
                                break

                    # 🔁 Extract style from usage
                    usage_style_dict = raw_value.get("style", {})
                    raw_value = {k: v for k, v in raw_value.items() if k != "style"}

                    # 🔁 Merge: usage overrides template
                    merged_style = {**template_style_dict, **usage_style_dict}
                    outer_style = ""
                    if merged_style:
                        style_str = resolve_style_dict(merged_style)
                        outer_style = f' style="{style_str}"'

                    html += f"<div{outer_style}>\n"

                    # Render each key in the template
                    tmpl_items = (
                        template.items() if isinstance(template, dict)
                        else [(k, v) for t in template if isinstance(t, dict) and "style" not in t for k, v in t.items()]
                    )

                    for tmpl_key, tmpl_val in tmpl_items:
                        key, style_attr = parse_key_and_style(tmpl_key)
                        tmpl_val = recursive_replace(tmpl_val, raw_value)
                        html += render_semantic(key, tmpl_val, style_attr) + "\n"
                    html += "</div>\n"

                else:
                    key, style_attr = parse_key_and_style(raw_key)
                    html += render_semantic(key, raw_value, style_attr) + "\n"

    html += "</section>\n"
    return html

def recursive_replace(data, context):
    if isinstance(data, str):
        for k, v in context.items():
            data = data.replace(f"{{{k}}}", str(v))
        return data
    elif isinstance(data, dict):
        return {k: recursive_replace(v, context) for k, v in data.items()}
    elif isinstance(data, list):
        return [recursive_replace(item, context) for item in data]
    else:
        return data


# 🖥️ Full page structure
def generate_page(page_name, page_content, global_nav=None, global_footer=None, nav_style=None,components=None):
    html = "<!DOCTYPE html>\n<html>\n<head>\n"
    html += f"<title>{page_name}</title>\n"
    html += "<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n"

    if global_nav:
        html += generate_nav(global_nav)

    for section_name, section_content in page_content.items():
        html += generate_section(section_name, section_content, components)


    if global_footer:
        html += generate_footer(global_footer, components)

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
    components = site.get("Components", {})


    for page_name, page_content in site.items():
        if page_name in ("Nav", "Footer", "NavStyle","Components"):
            continue

        html = generate_page(page_name, page_content, global_nav, global_footer, nav_style, components)
        with open(os.path.join(output_dir, f"{page_name.lower()}.html"), "w") as f:
            f.write(html)

    with open(os.path.join(output_dir, "style.css"), "w") as f:
        f.write(generate_css())
