from pathlib import Path
import os
import sys


def print_tree(root_path, ignore_list, prefix=""):
    # Get all items that aren't in the ignore list
    # Sorting ensures folders appear before files or in alphabetical order
    paths = sorted(
        [p for p in root_path.iterdir() if p.name not in ignore_list],
        key=lambda p: (p.is_file(), p.name.lower())
    )

    for i, path in enumerate(paths):
        # Check if this is the last item in the current folder
        is_last = (i == len(paths) - 1)

        # Decide which connector to use
        connector = "└── " if is_last else "├── "

        # Print the current item
        print(f"{prefix}{connector}{path.name}")

        # If it's a directory, go deeper (Recursion)
        if path.is_dir():
            # If this was the last item, the next level needs empty space
            # Otherwise, it needs a vertical pipe to continue the line
            extension = "    " if is_last else "│   "
            print_tree(path, ignore_list, prefix + extension)


# --- CONFIGURATION ---
folder_to_scan = Path('C:/Users/acer/Desktop/PROGRAMMING/java-coin-based-content-access')
ignore = {".git", "__pycache__", ".idea", "target", "node_modules"}

# Start the process
print(folder_to_scan.name + "/")
print_tree(folder_to_scan, ignore)

def run_script():
    # Get args
    args = sys.argv[1:]
