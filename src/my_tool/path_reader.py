import pathlib

def generate_tree(root_path, ignore_list, repo_root, prefix=""):
    dir_list = []

    paths = sorted(
        root_path.iterdir(),
        key=lambda p: (p.is_file(), p.name.lower())
    )

    entries = []
    for path in paths:
        rel = path.relative_to(repo_root).as_posix()

        if path.name == ".git":
            continue

        if ignore_list.match_file(rel):
            continue    

        entries.append((path, rel))

    for i, (path, rel_path) in enumerate(entries):

        # Check if this is the last item in the current folder
        is_last = (i == len(entries) - 1)

        # Decide which connector to use
        connector = "└── " if is_last else "├── "

        # Print the current item
        dir_list.append(f"{prefix}{connector}{path.name}")

        # print(ignore_list)
        # If it's a directory, go deeper (Recursion)
        if path.is_dir():
            # If this was the last item, the next level needs empty space
            # Otherwise, it needs a vertical pipe to continue the line
            extension = "    " if is_last else "│   "
            dir_list.extend(generate_tree(path, ignore_list, repo_root, prefix + extension))

    return dir_list
    


