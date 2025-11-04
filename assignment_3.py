import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)


def list_dir(path: Path, prefix: str = "", is_last: bool = True, is_root: bool = True):
    icons = {'root_folder': "📦",
         'other_folder': "📂",
         'file': "📜"}
    
    if is_root:
            print(f"{icons['root_folder']} {path.name}")

    entries = list(path.iterdir())
    folders = sorted([p for p in entries if p.is_dir()])
    files = sorted([p for p in entries if p.is_file()])
    entries = folders + files

    for i, entry in enumerate(entries):
        is_last_entry = i == len(entries) - 1
        connector = "┗" if is_last_entry else "┣"
        next_prefix = prefix + ("  " if is_last_entry else "┃ ")

        if entry.is_dir():
            print(f"{prefix}{connector} {Fore.BLUE}{icons['other_folder']}{Style.RESET_ALL} {entry.name}")
            # recursive call
            list_dir(entry, next_prefix, is_last_entry, is_root=False)
        else:
            print(f"{prefix}{connector} {Fore.GREEN}{icons['file']}{Style.RESET_ALL} {entry.name}")


def get_executed():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}⚠️  Please pass absolute path for the current directory")
        sys.exit(1)

    dir_path = Path(sys.argv[1]).resolve()

    if not dir_path.exists() or not dir_path.is_dir():
        print("Please provide a valid directory.")
        sys.exit(1)

    list_dir(dir_path)

get_executed()
