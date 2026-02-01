from pathlib import Path
import os 
import subprocess
import tempfile

from .path_reader import generate_tree
from .read_gitignore import get_top_level


def start():
    """
        runs the entire process of executing the script
    return:
        <name>.txt of dir tree
    """

    # Get the current location
    # value for folder_to_scan 

    folder_to_scan = Path.cwd()

    ignore = get_top_level(folder_to_scan)


    dir_tree = generate_tree(folder_to_scan, ignore)

    temp_path = os.path.join(tempfile.gettempdir(), "tree_output.txt")
    with open(temp_path, "w", encoding='utf-8') as f:
        f.write(folder_to_scan.name + "/\n")
        for dir in dir_tree:
            f.write(dir + "\n")
    
    # 3. Tell VS Code to open it in a new column
    # '-r' opens it in the current window, '2' opens it in the second column
    subprocess.run(["code", "-r", "--column", "2", temp_path], shell=True)

if __name__ == '__main__':
    start()