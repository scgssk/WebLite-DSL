
````markdown
# 🚀 WebLite

[![MIT License](https://img.shields.io/badge/license-GPLv3-blue.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.11-blue?logo=python)](https://www.python.org/)
[![Build Sites Fast](https://img.shields.io/badge/Build%20Sites-FAST-success?style=flat&logo=fastapi)]()
[![YAML Powered](https://img.shields.io/badge/YAML-Powered-yellow?logo=yaml)]()

WebLite is a **blazing-fast, YAML-powered static site builder** that lets you build beautiful websites _without writing any HTML or CSS_. Just write structured content in `.wl` files and generate full HTML pages in a flash.

> Think of it as Markdown meets HTML — with built-in styling superpowers.

---

## ✨ Features

- ✅ Write your entire website in YAML
- 🎨 Apply inline styles without touching CSS
- ⚡ Converts YAML to static HTML + CSS
- 🧠 Supports semantic tags (Title, Subtitle, CTA, etc.)
- 📂 Auto-generates clean output folder
- 🛠️ Easy to extend and customize

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weblite.git
cd weblite
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Install WebLite CLI

```bash
pip install -e .
```

---

## 🛠️ Usage

Create your website definition in `site.wl`:

```yaml
Nav:
  - Home
  - About

Home:
  Hero:
    Title: "**Welcome to WebLite**"
    Subtitle: "Build websites instantly with YAML"
    CTA >> background-color: #ff6600; color: white: "Get Started"
```

Then build your site:

```bash
weblite site.wl
```

Your generated website will be inside the `/output` folder.

---

## 🧾 YAML Reference

### Global Elements

```yaml
Nav: [Home, About, Contact]
NavStyle:
  background-color: "#222"
  color: white
Footer:
  Text: "&copy 2025 WebLite"
```

### Section Styling

```yaml
Hero:
  style:
    background-color: "#fefefe"
    padding: 40px
```

### Inline Component Styling

```yaml
  "Title >> color: #333; font-size: 36px": "**WebLite**"
  "CTA >> background-color: orange; color: white": "Get Started"
```

### Repeating Components

```yaml
Features:
  Items:
    - "p >> color: #444": "Clean YAML structure"
    - "p >> color: #444": "Instant HTML and CSS output"
```

---

## 🌐 Hosting Options

After building, host the `/output` folder on:

* GitHub Pages
* Netlify
* Vercel
* Any web server

---

## 📁 Folder Structure

```
/WebLite
├── weblite/
│   ├── builder.py
│   ├── cli.py
│   └── __main__.py
├── site.wl            # Your YAML site definition
├── output/            # Generated static website
├── README.md
├── LICENSE
```

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## 💡 Why Use WebLite?

* No HTML required
* No CSS files to manage
* 100% portable, runs anywhere Python runs
* Write once, style once, deploy instantly
* Built for speed and simplicity

---

## 🔗 Links

* [Website Template Gallery (coming soon)]()
* [Contribute to WebLite](https://github.com/scgssk/WebLite-DSL)
* [Issues / Bugs](https://github.com/your-username/WebLite-DSL/issues)

---

## ❤️ Built with love by developer, for developers.

```


