from pathlib import Path

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


    # Start the process
    print(folder_to_scan.name + "/")
    # print(ignore)

    dir_tree = generate_tree(folder_to_scan, ignore)

    print("="*10, "vs loop ", "="*10)
    for dir in dir_tree:
        print(dir)

if __name__ == '__main__':
    start()