import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise Exception("GitHub token not found. Set GITHUB_TOKEN environment variable.")

print("✅ GitHub token loaded successfully")
