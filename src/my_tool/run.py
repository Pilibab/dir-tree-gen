from pathlib import Path


from .path_reader import print_tree
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
    print_tree(folder_to_scan, ignore)

if __name__ == '__main__':
    start()