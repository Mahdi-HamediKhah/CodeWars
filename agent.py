import os
import subprocess

PROJECT_PATH = r"D:\Boot Camp\git"  # مسیر پروژه
COMMIT_MESSAGE_TEMPLATE = "✅ Added: {file_name}"
BRANCH_NAME = "main"

def get_all_files_to_commit():
    os.chdir(PROJECT_PATH)
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    files_to_commit = []

    for line in lines:
        status = line[:2]
        path = line[3:].strip()
        full_path = os.path.join(PROJECT_PATH, path)

        # هم فایل‌های جدید هم تغییر کرده‌ها
        if status in ("??", " M", "M ", "MM", "AM", "A "):
            if os.path.isfile(full_path):
                files_to_commit.append(path)
            elif os.path.isdir(full_path):
                for root, _, files in os.walk(full_path):
                    for file in files:
                        rel_path = os.path.relpath(os.path.join(root, file), PROJECT_PATH)
                        files_to_commit.append(rel_path)

    return files_to_commit

def git_add_commit(file_path):
    subprocess.run(["git", "add", file_path])
    message = COMMIT_MESSAGE_TEMPLATE.format(file_name=file_path)
    subprocess.run(["git", "commit", "-m", message])

def git_push():
    subprocess.run(["git", "push", "origin", BRANCH_NAME])

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
