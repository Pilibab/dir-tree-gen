
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

        # print(ignore_list)
        # If it's a directory, go deeper (Recursion)
        if path.is_dir():
            
            # If this was the last item, the next level needs empty space
            # Otherwise, it needs a vertical pipe to continue the line
            extension = "    " if is_last else "│   "
            print_tree(path, ignore_list, prefix + extension)




