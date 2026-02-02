from pathlib import Path
import os 
import subprocess
import tempfile
import argparse

from .path_reader import generate_tree
from .read_gitignore import load_gitignore


def start(output_mode="file"):
    """
        runs the entire process of executing the script
    return:
        <name>.txt of dir tree
    """
    folder_to_scan = Path.cwd()
    ignore = load_gitignore(folder_to_scan)
    dir_tree = generate_tree(folder_to_scan, ignore, folder_to_scan)

    # Use a clear boolean check or specific string comparison
    if output_mode == "terminal":
        print(f"\n{folder_to_scan.name}/")
        for line in dir_tree:
            print(line)
        print("\n") # Added padding for visibility
    else:
        temp_path = os.path.join(tempfile.gettempdir(), "tree_output.txt")
        with open(temp_path, "w", encoding='utf-8') as f:
            f.write(folder_to_scan.name + "/\n")
            for line in dir_tree:
                f.write(line + "\n")
        
        # Wrapped in try-except to catch cases where 'code' isn't in PATH
        try:
            subprocess.run(["code", "-r", temp_path], shell=True)
        except Exception as e:
            print(f"Failed to open VS Code: {e}")


def main():
    parser = argparse.ArgumentParser(description="Generate directory tree")
    parser.add_argument(
        "-t", "--terminal", action="store_true", help="Print tree to terminal"
    )
    parser.add_argument(
        "-o", "--output", action="store_true", help="Write tree to text file (default)"
    )

    args = parser.parse_args()

    # Decide output mode
    if args.terminal:
        start(output_mode="terminal")
    else:
        start(output_mode="file")