# GitHub Language Badge Generator

This script fetches the most-used programming languages across your public, non-forked GitHub repositories, then generates a neat `README.md` file with visual Shields.io badges.

---

## How It Works

1. Authenticates with GitHub using a Personal Access Token (PAT) from a `.env` file.
2. Retrieves all repositories (with pagination).
3. Filters out forked repos.
4. Fetches language stats per repo using the GitHub API.
5. Counts total usage of each language (based on bytes).
6. Sorts and renders badges using Shields.io in Markdown format.

---

## Requirements

- Python 3.7+
- `requests`
- `python-dotenv`

Install dependencies:

```bash
pip install requests python-dotenv
```

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/github-language-badges
cd github-language-badges
```

### 2. Create a `.env` File

Create a `.env` file in the project root with the following contents:

```
GITHUB_USERNAME=your-github-username
GITHUB_TOKEN=ghp_yourtoken123456789
```

### 3. Generate a GitHub Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Set a name and optional expiration
4. Leave scopes unchecked (for public repo access only)
5. Copy the token and paste it in your `.env` file

---

## Run the Script

```bash
python generate_github_skills_readme.py
```

This will create a new `README.md` file with badges showing your most-used programming languages.

---

## Output Example

```
## Top Languages from My GitHub

![Python](...) ![JavaScript](...) ![Go](...) ...
```

Open this file on GitHub to view your language profile as rendered badges.

---

## Optional Customization

- Modify `logo_map` to control how Shields.io displays logos
- Change the `top_n` in the script to control how many languages are shown
- Style your output further with Markdown sections or categories

---

<!-- ## License

MIT License. Free to use, share, and build on! -->