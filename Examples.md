
### 🔹 **Basic Landing Page**

```yaml
Home:
  Hero:
    - "Title >> big centered red": "**Welcome to WebLite!**"
    - "Subtitle >> gray medium centered": "Build static sites effortlessly"
    - "CTA": "Get Started"

```

### You can use css styles also like text-align etc...

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

### 🔹 **Multi-Page Site with Reusable Components**

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

### 🔷️ ** Complex site example **
```yaml
Nav:
  - style:
      background: "#2c3e50"
      color: white
      text-align: center
  - Home
  - About
  - Services
  - Contact

Footer:
  - style:
      background: "#34495e"
      color: white
      padding: 20px
  - "Paragraph >> small centered gray": "© 2025 WebLite Inc. All rights reserved."

Components:
  HeroCard:
    - style:
        box: true
        background: "#ecf0f1"
        centered: true
    - "Title >> big red": "**{title}**"
    - "Description >> gray": "{description}"

  ServiceItem:
    - style:
        box: true
        background: "#f8f8f8"
        padding: 20px
        border-radius: 8px
    - "Title >> medium blue": "**{name}**"
    - "Paragraph": "{details}"

Home:
  Hero:
    - style:
        background: "#1abc9c"
        color: white
        padding: 60px
        centered: true
    - "Title >> big": "**Welcome to WebLite**"
    - "Description >> small": "Build websites using YAML. Fast, minimal, and fun!"
    - "CTA >> padded box": "Get Started"

  Features:
    - HeroCard:
        title: "Minimal Syntax"
        description: "Define pages and styles using readable YAML without boilerplate code."
    - HeroCard:
        title: "Reusable Components"
        description: "Create components once and use them across multiple sections."

About:
  Intro:
    - style:
        padding: 30px
        centered: true
    - "Title >> big blue": "**About WebLite**"
    - "Paragraph": "WebLite is a custom Domain-Specific Language (DSL) that transforms YAML files into clean HTML sites."

  Team:
    - style:
        centered: true
    - "Title >> medium": "Meet Our Team"
    - Image:
        src: "https://i.pravatar.cc/100?img=12"
    - Image:
        src: "https://i.pravatar.cc/100?img=45"

Services:
  Offerings:
    - ServiceItem:
        name: "WebLite Builder"
        details: "A Python-powered engine that converts YAML to responsive static HTML."
    - ServiceItem:
        name: "Online Editor"
        details: "Try out your code instantly with our Monaco-based WebLite Try-It editor."

Contact:
  ReachOut:
    - style:
        centered: true
        background: "#ecf0f1"
        padding: 30px
    - "Title >> big": "**Let's Talk**"
    - "Paragraph": "Have questions or suggestions? Reach out through our social channels."
```

