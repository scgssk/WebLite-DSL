# 🚀 WebLite

[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/Made%20with-Python%203.11-blue?logo=python)](https://www.python.org/)
[![Blazing Fast](https://img.shields.io/badge/Build%20Sites-FAST-success?style=flat&logo=fastapi)](https://github.com/scgssk/WebLite-DSL)
[![YAML Powered](https://img.shields.io/badge/YAML-Powered-yellow?logo=yaml)](https://yaml.org/)

**WebLite** is a **blazing-fast, YAML-powered static site generator** that lets you create stunning websites *without writing HTML or CSS*. Define your site in simple `.wl` files, and WebLite transforms them into fully styled HTML pages in seconds.

> Think Markdown meets HTML, with built-in styling superpowers. 🪄

---

## ✨ Why WebLite?

- **No HTML/CSS Knowledge Needed**: Write structured YAML, and WebLite handles the rest.
- **Blazing Fast**: Generate static sites in a flash.
- **Inline Styling**: Add styles directly in YAML—no separate CSS files.
- **Semantic Simplicity**: Use intuitive tags like `Title`, `Subtitle`, and `CTA`.
- **Portable & Lightweight**: Runs anywhere Python does, with zero dependencies.
- **Customizable**: Easily extend to fit your needs.

---

## 📦 Get Started

### 1. Clone the Repository

```bash
git clone https://github.com/scgssk/WebLite-DSL.git
cd WebLite-DSL
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install WebLite CLI

```bash
pip install -e .
```

---

## 🛠️ Build Your First Site

1. Create a `site.wl` file with your website structure:

```yaml
Nav:
  - Home
  - About
  - Contact

Home:
  Hero:
    Title: "**Welcome to WebLite**"
    Subtitle: "Build websites instantly with YAML"
    CTA >> background-color: #ff6600; color: white: "Get Started"
```

2. Generate your site:

```bash
weblite site.wl
```

3. Find your static website in the `output/` folder, ready to deploy!

---

## 🧾 YAML Syntax Guide

WebLite’s YAML syntax is intuitive and powerful. Here’s a quick overview:

### Global Elements

Define navigation, footer, or global styles:

```yaml
Nav:
  - Home
  - About
  - Contact
NavStyle:
  background-color: "#222"
  color: white
Footer:
  Text: "© 2025 WebLite"
```

### Section Styling

Style entire sections with ease:

```yaml
Hero:
  style:
    background-color: "#fefefe"
    padding: 40px
```

### Inline Component Styling

Add styles directly to components:

```yaml
"Title >> color: #333; font-size: 36px": "**WebLite**"
"CTA >> background-color: orange; color: white": "Get Started"
```

### Repeating Components

Create lists of styled elements:

```yaml
Features:
  Items:
    - "p >> color: #444": "Clean YAML structure"
    - "p >> color: #444": "Instant HTML and CSS output"
```

---

## 🌐 Deploy Your Site

Host the `output/` folder on platforms like:

- [GitHub Pages](https://pages.github.com/)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)
- Any web server (e.g., Apache, Nginx)

---

## 📁 Project Structure

```plaintext
/WebLite-DSL
├── weblite/
│   ├── builder.py      # Core site generation logic
│   ├── cli.py         # CLI interface
│   └── __main__.py    # Entry point
├── site.wl            # Your YAML site definition
├── output/            # Generated static website
├── README.md          # This file
├── LICENSE            # GPLv3 license
├── requirements.txt   # Python dependencies
```

---

## 📜 License

WebLite is open-source and licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## 💡 Why Choose WebLite?

- **Effortless**: No HTML, no CSS, just YAML.
- **Fast**: Generate sites in milliseconds.
- **Portable**: Deploy anywhere, no server-side setup.
- **Flexible**: Style and structure your site your way.
- **Developer-Friendly**: Built for simplicity and speed.

---

## 🔗 Resources

- [Website Template Gallery](https://github.com/scgssk/WebLite-DSL/templates) *(Coming Soon!)*
- [Contribute to WebLite](https://github.com/scgssk/WebLite-DSL/blob/main/CONTRIBUTING.md)
- [Report Issues](https://github.com/scgssk/WebLite-DSL/issues)

---

## ❤️ Built for Developers, by Developers

WebLite is a labor of love to simplify web development. Join our community, contribute, or share your creations with `#WebLite` on [X](https://x.com/)!

> Star the repo on [GitHub](https://github.com/scgssk/WebLite-DSL) to support the project! 🌟
