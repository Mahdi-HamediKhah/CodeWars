import os
import subprocess
from datetime import datetime

# ----------------------------
# ✨ CONFIG SECTION
# ----------------------------
PROJECT_PATH = r"D:\Boot Camp\git"  # <- مسیر جدید شامل کل پروژه
COMMIT_MESSAGE_TEMPLATE = "Add solution file {file_name}"
BRANCH_NAME = "main"  # یا master اگر شاخهٔ پیش‌فرض تو اینه

# ----------------------------
# ✅ FUNCTIONS
# ----------------------------
def get_all_untracked_files():
    os.chdir(PROJECT_PATH)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    untracked_files = []

    for line in lines:
        if line.startswith("??"):
            path = line[3:].strip()
            full_path = os.path.join(PROJECT_PATH, path)
            if os.path.isfile(full_path):
                untracked_files.append(path)
            elif os.path.isdir(full_path):
                # اگر پوشه بود، همه فایل‌های داخلش رو بگیر
                for root, _, files in os.walk(full_path):
                    for f in files:
                        rel_path = os.path.relpath(os.path.join(root, f), PROJECT_PATH)
                        untracked_files.append(rel_path)
    return untracked_files

def git_add_commit(file_path):
    subprocess.run(["git", "add", file_path])
    message = COMMIT_MESSAGE_TEMPLATE.format(file_name=file_path)
    subprocess.run(["git", "commit", "-m", message])

def git_push():
    subprocess.run(["git", "push", "origin", BRANCH_NAME])

# ----------------------------
# ⏰ RUN
# ----------------------------
if __name__ == "__main__":
    os.chdir(PROJECT_PATH)

    files = get_all_untracked_files()
    if not files:
        print("\u274c No new files to commit.")
    else:
        print(f"\u2705 Found new files: {files}")
        for file in files:
            git_add_commit(file)

        print("\ud83d\ude80 Pushing to GitHub...")
        git_push()
        print("✅ Done!")