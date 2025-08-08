import os
import subprocess

# ----------------------------
# ✨ CONFIG SECTION
# ----------------------------
PROJECT_PATH = r"D:\Boot Camp\git"  # مسیر پروژه
COMMIT_MESSAGE_TEMPLATE = "✅ Added: {file_name}"
BRANCH_NAME = "main"

# ----------------------------
# ✅ FUNCTIONS
# ----------------------------

def get_all_files_to_commit():
    os.chdir(PROJECT_PATH)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    files_to_commit = []

    for line in lines:
        status = line[:2]
        path = line[3:].strip()
        full_path = os.path.join(PROJECT_PATH, path)

        if status in ("??", " M", "M ", "MM", "AM", "A "):  # فایل جدید یا تغییر کرده
            if os.path.isfile(full_path):
                files_to_commit.append(path)
            elif os.path.isdir(full_path):  # اگر فولدر باشه، همه فایل‌های داخلش
                for root, _, files in os.walk(full_path):
                    for file in files:
                        relative_path = os.path.relpath(os.path.join(root, file), PROJECT_PATH)
                        files_to_commit.append(relative_path)

    return files_to_commit

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

    files = get_all_files_to_commit()
    if not files:
        print("❌ No new files to commit.")
    else:
        print(f"✅ Found files: {files}")
        for file in files:
            git_add_commit(file)

        print("🚀 Pushing to GitHub...")
        git_push()
        print("✅ Done!")
