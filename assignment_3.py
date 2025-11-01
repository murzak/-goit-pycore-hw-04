import sys
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)


def list_dir(path: Path):
    icons = {'root_folder': "📦",
         'other_folder': "📂",
         'file': "📜"}
    
    print(f"{icons['root_folder']} {path.name}")

    stack = [(path, "", True)]  # (current_path, prefix, is_last)
    while stack:
        current_path, prefix, _ = stack.pop()

        entries = list(current_path.iterdir())


        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "┗" if is_last else "┣"
            next_prefix = prefix + ("  " if is_last else "┃ ")

            if entry.is_dir():
                print(f"{prefix}{connector} {Fore.BLUE}{icons['other_folder']}{Style.RESET_ALL} {entry.name}")
                # Push this directory to the stack for further processing
                stack.append((entry, next_prefix, is_last))
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
