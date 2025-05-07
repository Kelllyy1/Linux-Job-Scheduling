import os
from pathlib import Path

def get_folder_size(path):
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                continue
    return total

def scan_dirs(dirs_to_check):
    usage = []
    for directory in dirs_to_check:
        if os.path.exists(directory):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    size = get_folder_size(item_path)
                    usage.append((item, size))
    return usage

def print_results(usage, top_n=10):
    print(f"\nTop {top_n} space-consuming applications:\n")
    print(f"{'Application':40} {'Size (GB)':>10}")
    print("-" * 55)
    for name, size in sorted(usage, key=lambda x: x[1], reverse=True)[:top_n]:
        print(f"{name:40} {size / (1024 ** 3):10.2f}")

if __name__ == "__main__":
    user_profile = os.environ.get('USERPROFILE', str(Path.home()))
    dirs_to_scan = [
        os.environ.get('ProgramFiles', r"C:\Program Files"),
        os.environ.get('ProgramFiles(x86)', r"C:\Program Files (x86)"),
        os.path.join(user_profile, r"AppData\Local\Programs"),
    ]

    all_apps_usage = scan_dirs(dirs_to_scan)
    print_results(all_apps_usage)
