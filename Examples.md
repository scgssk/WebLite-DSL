
### 🔹 **Basic Landing Page**

```yaml
Home:
  Hero:
    - "Title >> big centered red": "**Welcome to WebLite!**"
    - "Subtitle >> gray medium centered": "Build static sites effortlessly"
    - "CTA": "Get Started"

```

---

### 🔹 **With Navigation and Footer**

```yaml
Nav:
  - "Home"
  - "About"
  - "Contact"

Footer:
  - "© 2025 WebLite Inc."

Home:
  Hero:
    - "Title >> big centered": "**Simple. Powerful. Lightweight.**"
    - "Description": "Your go-to static site builder."
    - "CTA": "Try Now"
```

---

**Multi-Page Site with Reusable Components**

```yaml
Nav:
  - "Home"
  - "Docs"
  - "Contact"

Footer:
  - "Thanks for visiting WebLite!"

Components:
  InfoCard:
    - style:
        box: true
        padded: true
        centered: true
    - "Title >> red": "**{title}**"
    - "Description": "{text}"

Home:
  Hero:
    - "Title >> big": "**Welcome to WebLite!**"
    - "CTA": "Explore"

  Features:
    - InfoCard:
        title: "Easy YAML Syntax"
        text: "Write less, build more."

    - InfoCard:
        title: "Custom Styles"
        text: "Use aliases or raw CSS."

Docs:
  Content:
    - "Title": "Documentation"
    - "Paragraph": "Coming soon..."

Contact:
  Form:
    - "Subtitle": "Get in Touch"
    - "Paragraph": "Email us at support@weblite.dev"
```

