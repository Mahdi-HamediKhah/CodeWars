import os
import subprocess

# ----------------------------
# ✨ CONFIG SECTION
# ----------------------------
PROJECT_PATH = r"D:\Boot Camp\git"  # مسیر ثابت
COMMIT_MESSAGE_TEMPLATE = "✅ Added: {file_name}"
BRANCH_NAME = "main"

# ----------------------------
# ✅ FUNCTIONS
# ----------------------------
def get_all_new_files():
    os.chdir(PROJECT_PATH)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    new_files = []

    for line in lines:
        if line.startswith("??"):
            path = line[3:].strip()
            full_path = os.path.join(PROJECT_PATH, path)

            # اگه فایل مستقیم باشه
            if os.path.isfile(full_path):
                new_files.append(path)

            # اگه پوشه باشه، همه فایل‌های داخلش رو بیار
            elif os.path.isdir(full_path):
                for root, _, files in os.walk(full_path):
                    for file in files:
                        relative_path = os.path.relpath(os.path.join(root, file), PROJECT_PATH)
                        new_files.append(relative_path)

    return new_files

def git_add_commit(file_path):
    subprocess.run(["git", "add", file_path])
    message = COMMIT_MESSAGE_TEMPLATE.format(file_name=file_path)
    subprocess.run(["git", "commit", "-m", message])

def git_push():
    subprocess.run(["git", "push", "origin", BRANCH_NAME])

# ----------------------------
# 🚀 RUN
# ----------------------------
if __name__ == "__main__":
    os.chdir(PROJECT_PATH)

    files = get_all_new_files()
    if not files:
        print("❌ No new files to commit.")
    else:
        print(f"✅ Found new files: {files}")
        for file in files:
            git_add_commit(file)

        print("🚀 Pushing to GitHub...")
        git_push()
        print("✅ Done!")
