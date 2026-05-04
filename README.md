# BRECOMPERU Solutions Repository

This repository contains agile HTML/CSS demos for various industries and segments. It is designed to be highly scalable, SEO-friendly, and easy to maintain.

## 🏗️ Architecture: Domain-Driven Structure

Every demo follows a standardized path that defines its context and URL:

`solutions/[industry]/[segment]/[type]/[tier].html`

### 1. Hierarchy Levels
- **`[industry]`**: The broad industry category (e.g., `legal`, `healthcare`, `agriculture`).
- **`[segment]`**: The specific sector or niche (e.g., `labor`, `real-estate`, `general`).
- **`[type]`**: 
    - `standard/`: Packaged templates for quick delivery (80% of cases).
    - `custom/[client-name]/`: Bespoke demos for high-ticket clients.
- **`[tier].html`**: The value proposal level:
    - `essential.html`: **Digital Agility** (The essentials to compete).
    - `growth.html`: **Growth Ecosystem** (Scalable operations).
    - `exponential.html`: **Exponential Transformation** (Market leadership with IA/3D).

### 2. Assets Management
If a demo requires images or other resources, they must be stored in a local `assets/` folder within the demo directory.
**Rule**: Never reference images from another industry or segment folder.

Example:
`legal/labor/custom/smith-law/assets/hero.jpg`

---

## 🚀 Quick Start for Developers

To create a new demo for a new industry (e.g., "Mining"):

1. Create the directory:
   `mkdir -p mining/general/standard`
2. Drop your three HTML files:
   - `essential.html`
   - `growth.html`
   - `exponential.html`
3. (Optional) Create an `assets/` folder for local images.

---

## 🛠️ Technical Rules
- **CSS**: Must be embedded within the HTML file (no external CSS files).
- **SEO**: The path automatically defines the URL on the main web application.
- **English**: All directories and files must be named in English.
- **Agility**: Demos are intended to be self-contained and ready in minutes.

solutions/
├── legal/
│   ├── labor/
│   │   ├── standard/
│   │   │   ├── essential.html
│   │   │   ├── growth.html
│   │   │   └── exponential.html
│   │   └── custom/
│   │       └── estudio-perez/
│   │           ├── essential.html
│   │           ├── growth.html
│   │           ├── exponential.html
│   │           └── assets/
│   │               ├── hero.jpg
│   │               └── logo.png
│   │
│   ├── real-estate/
│   │   └── standard/
│   │       ├── essential.html
│   │       ├── growth.html
│   │       └── exponential.html
│   │
│   └── corporate/
│       └── standard/
│           ├── essential.html
│           ├── growth.html
│           └── exponential.html
│
├── healthcare/
│   └── clinics/
│       └── standard/
│           ├── essential.html
│           ├── growth.html
│           └── exponential.html
│
└── mining/
    └── standard/
        ├── essential.html
        ├── growth.html
        └── exponential.html