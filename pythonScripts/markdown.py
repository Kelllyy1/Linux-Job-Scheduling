"""  This is a Python script that fetches the top programming languages used in a GitHub user's repositories and generates a README.md file with badges for each language.
    It uses the GitHub API to get the user's repositories and their respective languages, and then creates a badge for each language using Shields.io.
    The script requires the `requests` library for making HTTP requests and `python-dotenv` for loading environment variables from a `.env` file.
    It also uses the `collections.Counter` class to count the occurrences of each language in the user's repositories. """

# Import the necessary modules
import os
import requests
from collections import Counter
from dotenv import load_dotenv
from urllib.parse import quote
from typing import Dict, List

load_dotenv()

# Import the credentials from the .env file
TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
HEADERS = {"Authorization": f"token {TOKEN}"}

# A dictionary mapping the programming lanuage to the logo used in the badge
LOGO_MAP = {
    "Python": "python", "JavaScript": "javascript", "Go": "go", "HTML": "html5", "Ruby": "ruby",
    "TypeScript": "typescript", "C++": "cplusplus", "C": "c", "Swift": "swift", "Shell": "gnu-bash",
    "CSS": "css3", "Objective-C": "apple", "Jupyter Notebook": "jupyter", "Java": "java"
}

# A function to fetch all repositories of a user from GitHub API
# It uses pagination to get all repositories, and filters out forks
def get_all_repos(username: str) -> List[dict]:
    page = 1
    repos = []
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"GitHub API error: {response.json()}")
        data = response.json()
        if not data:
            break
        repos.extend([repo for repo in data if not repo.get("fork")])
        page += 1
    return repos

# It returns a list of dictionaries, each representing a repository
# The function fetches the languages used in each repository and counts their occurrences
def fetch_languages(repos: List[dict]) -> Dict[str, int]:
    counter = Counter()
    for repo in repos:
        response = requests.get(repo["languages_url"], headers=HEADERS)
        if response.status_code == 200:
            counter.update(response.json())
    return dict(counter)

# It generates a badge for each programming language using Shields.io
# The badge includes the language name, a logo, and a color scheme
def generate_badge(label: str) -> str:
    logo = LOGO_MAP.get(label, "")
    encoded = quote(label)
    return f"![{label}](https://img.shields.io/badge/{encoded}-informational?style=for-the-badge&logo={logo}&logoColor=white)"

# This function generates a README.md file with badges for the top programming languages used in the user's repositories
def write_readme(lang_data: Dict[str, int], output_file="README.md", top_n=10):
    sorted_langs = sorted(lang_data.items(), key=lambda x: x[1], reverse=True)[:top_n]
    with open(output_file, "w") as f:
        f.write("##  Top Languages from My GitHub\n\n")
        for i, (lang, _) in enumerate(sorted_langs):
            f.write(generate_badge(lang) + " ")
            if (i + 1) % 4 == 0:
                f.write("\n")
        f.write("\n")

# Main function to execute the script
def main():
    print(f" Fetching repos for {USERNAME}...")
    repos = get_all_repos(USERNAME)
    print(f" Found {len(repos)} repos (excluding forks)")
    langs = fetch_languages(repos)
    print(f" Detected {len(langs)} unique languages")
    write_readme(langs)
    print(" README.md generated!")

if __name__ == "__main__":
    main()


# Iteration 1
# import requests
# from collections import Counter
# from urllib.parse import quote

# GITHUB_USERNAME = "Kelllyy1"  # <- Replace this

# def fetch_languages(username):
#     repos_url = f"https://api.github.com/users/{username}/repos"
#     response = requests.get(repos_url)
#     repos = response.json()

#     if not isinstance(repos, list):
#         print("Error fetching repositories:", repos.get("message"))
#         return {}

#     language_counter = Counter()
#     for repo in repos:
#         lang_url = repo["languages_url"]
#         lang_response = requests.get(lang_url)
#         if lang_response.status_code == 200:
#             repo_langs = lang_response.json()
#             language_counter.update(repo_langs)

#     return dict(language_counter)

# def generate_badge(language):
#     logo_map = {
#         "Jupyter Notebook": "jupyter",
#         "C++": "cplusplus",
#         "C#": "csharp",
#         "JavaScript": "javascript",
#         "TypeScript": "typescript",
#         "HTML": "html5",
#         "CSS": "css3",
#         "Shell": "gnu-bash",
#         "Go": "go",
#         "Python": "python",
#         "Java": "java",
#         "Ruby": "ruby",
#         "Rust": "rust",
#         "PHP": "php",
#         "Swift": "swift",
#         "Kotlin": "kotlin",
#         "Scala": "scala",
#         "Haskell": "haskell",
#         "C": "c",
#         "Assembly": "assembly",
#         "Objective-C": "apple",
#         "Makefile": "cmake",
#         "PowerShell": "powershell",
#         "Dart": "dart"
#     }

#     logo = logo_map.get(language, "")
#     label_encoded = quote(language)
#     return f"![{language}](https://img.shields.io/badge/{label_encoded}-informational?style=for-the-badge&logo={logo}&logoColor=white)"

# def write_readme(language_data):
#     with open("README.md", "w") as f:
#         f.write("##  Languages Detected From My GitHub\n\n")
#         sorted_langs = sorted(language_data.items(), key=lambda x: x[1], reverse=True)
#         for lang, _ in sorted_langs:
#             badge = generate_badge(lang)
#             f.write(f"{badge} ")
#         f.write("\n")

# if __name__ == "__main__":
#     langs = fetch_languages(GITHUB_USERNAME)
#     if langs:
#         write_readme(langs)
#         print(" README.md file generated with badges.")
#     else:
#         print("No languages found.")
