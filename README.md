# 💡 Code Snippet AI – ERPNext + OpenAI + n8n Automation

This project automatically generates SEO-optimized content for code snippets using OpenAI, stores them in ERPNext, and creates public-facing webpages for students.

## 🔧 Tech Stack
- ERPNext (v15)
- Frappe Framework
- n8n (workflow automation)
- OpenAI (GPT-3.5/4o)

## 🚀 Features
- Auto-generation of:
  - SEO Title
  - Meta Description
  - HTML Tutorial Page
- Web Page creation in ERPNext
- “See on Website” button in Code Snippet Doctype
- Scheduled n8n automation (every hour)

## 📁 Structure
- `code_snippet_ai/` - Frappe app
- `api/` - Custom whitelisted methods
- `public/js/code_snippet.js` - Client script for custom buttons
- `integrations/n8n/` - Exported automation workflow
- `screenshots/` - (Optional) demo UI shots

## 🧪 How It Works
1. Create a Code Snippet with just code
2. n8n workflow picks it up
3. Sends to OpenAI and stores:
   - `seo_title`
   - `seo_description`
   - `html_content`
4. Creates a Web Page like `/snippets/python-loop`
5. User can preview with “See on Website” button

---

📌 Developed by [Sandeep Ambala](https://github.com/sandeepgithup)

### Code Snippet Ai

AI-powered code snippet enhancer

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app code_snippet_ai
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/code_snippet_ai
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
