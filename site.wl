# 🔗 Navigation
Nav:
  - style:
      background-color: "#000"
      color: "#fff"
  - Home
  - Services
  - Portfolio
  - Blog
  - About

# 🧱 Global Components
Components:
  ServiceCard:
    - style:
        box: true
        padded: true
    - "Title >> medium blue": "**{title}**"
    - "Paragraph >> gray": "{desc}"
    - "Link >> text-decoration: none; color: #342": "{link}"

  BlogPost:
    - "Title >> small blue": "**{title}**"
    - "Paragraph >> small gray": "{snippet}"
    - "Link >> small": "{url}"

  ContactBox:
    - style:
        box: true
        background-color: "#fefefe"
        padding: 20px
    - "Title >> red small": "**{heading}**"
    - "Paragraph >> gray": "{info}"
    - "Link >> blue": "{email}"

  ImageCard:
    - "Image >> border-radius: 8px": "https://placehold.co/400x400"
    - "Paragraph >> small centered gray": "{caption}"
    - style:
        display: flex
        flex-direction: column
        align-items: center

  SocialIcons:
    - "Paragraph >> centered": "Follow us: GitHub | Twitter | LinkedIn"



# 🔻 Footer
Footer:
  - style:
      background-color: "#222"
      color: "#fff"
      text-align: center
  - "Paragraph >> small gray": "Made with Love by Devs"
  - SocialIcons


# 🏠 Home Page
Home:
  Hero:
    - "Title >> big centered red": "**Next-gen Sites with Simplicity**"
    - "Subtitle >> medium gray centered": "Turn YAML into beautiful web pages."
    - style:
        background-color: "#f3f3f3"
        padded: true
        text-align: center

  Highlights:
    - ServiceCard:
        title: "Speed First"
        desc: "Your site builds in milliseconds."
        link: "/services.html#speed"
        style:
          background-color: "#e0f7fa"
    - ServiceCard:
        title: "Developer Friendly"
        desc: "Code less, style smartly, build faster."
        link: "/services.html#dev"
    - ServiceCard:
        title: "Custom Components"
        desc: "Reusable blocks with flexible overrides."
        link: "/services.html#components"
        style:
          background-color: "#f9fbe7"

  CallToAction:
    - "Title >> centered medium": "**Try it out now!**"
    - "CTA >> background-color: #27ae60; color: white": "Launch WebLite"
    - style:
        text-align: center
        background-color: "#ffffff"
        padded: true

# 🛠 Services Page
Services:
  Overview:
    - "Title >> medium blue": "**Our Services**"
    - "Paragraph >> gray": "Here's what WebLite can offer you:"
    - style:
        background-color: "#e8f5e9"
        padded: true

  Cards:
    - ServiceCard:
        title: "YAML to HTML"
        desc: "Write once, generate everywhere."
        link: "#yaml-html"
    - ServiceCard:
        title: "Components"
        desc: "Create once, reuse infinitely."
        link: "#components"
    - ServiceCard:
        title: "Smart Styling"
        desc: "Mix aliases and CSS on the fly."
        link: "#styling"

# 🎨 Portfolio Page
Portfolio:
  Showcase:
    - "Title >> big blue": "**Projects We Loved**"
    - "Paragraph >> gray": "Each built with care, YAML, and WebLite."
    - ImageCard:
        caption: "Landing Page Design"
    - ImageCard:
        caption: "Startup Portfolio Site"
    - ImageCard:
        caption: "Interactive Blog Platform"
    - style:
        background-color: "#f4f4f4"
        padded: true
        display: flex
        flex-direction: column
        align-items: center

# ✍️ Blog Page
Blog:
  Articles:
    - BlogPost:
        title: "10 Reasons to Ditch HTML for YAML"
        snippet: "Why WebLite makes site building a breeze..."
        url: "/blog/reasons.html"
    - BlogPost:
        title: "Component-based Web Architecture"
        snippet: "Building modularly like never before."
        url: "/blog/components.html"
    - BlogPost:
        title: "WebLite vs Traditional CMS"
        snippet: "Compare performance, control, and simplicity."
        url: "/blog/comparison.html"
    - style:
        background-color: "#fafafa"
        padded: true

# 👥 About Page
About:
  Team:
    - "Title >> medium centered blue": "**Meet the Makers**"
    - "Paragraph >> gray centered": "We're a team of developers passionate about simplifying the web."
    - ImageCard:
        src: "https://placehold.co/100x100"
        caption: "Soorya Kumar - Founder"
    - ImageCard:
        src: "https://placehold.co/100x100"
        caption: "Jane Doe - Designer"
    - ImageCard:
        src: "https://placehold.co/100x100"
        caption: "Mark Tech - Engineer"
    - style:
        background-color: "#e3f2fd"
        text-align: center
        padded: true

  ReachOut:
    - ContactBox:
        heading: "General Enquiries"
        info: "For questions, partnership, or feedback"
        email: "mailto:contact@weblite.dev"
    - ContactBox:
        heading: "Support"
        info: "Facing issues? Let’s help!"
        email: "mailto:support@weblite.dev"
    - style:
        background-color: "#fff3e0"
        padded: true
