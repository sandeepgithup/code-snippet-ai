# 💡 Code Snippet AI – ERPNext + OpenAI + n8n Automation

This project automatically generates SEO-optimized content for code snippets using OpenAI, stores them in ERPNext, and creates public-facing webpages for students.

---

## 🔧 Tech Stack

- ERPNext (v15)
- Frappe Framework
- n8n (workflow automation)
- OpenAI (GPT-3.5 / GPT-4o)

---

## 🚀 Features

- Auto-generation of:
  - SEO Title
  - Meta Description
  - HTML Tutorial Page
- Web Page creation in ERPNext
- “See on Website” button in Code Snippet Doctype
- Scheduled n8n automation (every hour)

---

## 📁 Structure

code_snippet_ai/
├── api/ # Custom whitelisted methods
├── public/js/code_snippet.js # Client script for web links

yaml
Copy
Edit

---

## 🧪 How It Works

1. Create a Code Snippet with just code
2. n8n workflow picks it up
3. Sends to OpenAI and stores:
   - `seo_title`
   - `seo_description`
   - `html_content`
4. Creates a Web Page like `/snippets/python-loop`
5. User can preview with the “See on Website” button

---

## 🛠 Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app code_snippet_ai
🤝 Contributing
This app uses pre-commit for code formatting and linting. Please install pre-commit and enable it for this repository:

bash
Copy
Edit
cd apps/code_snippet_ai
pre-commit install
Pre-commit is configured to use the following tools:

ruff

eslint

prettier

pyupgrade

✅ CI (GitHub Actions)
CI Workflow: Installs this app and runs unit tests on every push to the develop branch.

Linters Workflow: Runs Frappe Semgrep Rules and pip-audit on every pull request.

📄 License
MIT

