from pathlib import Path


from my_tool.read_gitignore import get_top_level

def read_files_in_ignore(file_path : Path, ignore_name: str = ".gitignore"):
    patterns = []
    # Use 'with open' to ensure the file is properly closed after reading
    try:
        with open(file_path / ignore_name, 'r') as f:
            for line in f:
                # Strip leading/trailing whitespace (including newline characters)
                line = line.strip()
                # Ignore blank lines and comments (lines starting with '#')
                if line and not line.startswith('#'):
                    patterns.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    
    # natively ignore .git files 
    patterns.append(".git")
    # remove redundancy 
    clean_list = set(patterns)
    pattern_list = [*clean_list]
    return pattern_list



def test_read_gitignore_contains_required_folders():
    # 1. Setup
    to_scan = Path.cwd()
    
    # 2. Action
    ignore_list = get_top_level(to_scan)

   
    
    # 3. Assert (Check if individual items exist in the result)
    assert ".git" in ignore_list
    assert ".venv" in ignore_list
    assert "__pycache__" in ignore_list
    assert ".idea" in ignore_list
    
    # check for things that SHOULD NOT be there
    assert "src" not in ignore_list

def test_read_file_outside_ignore():
    root = Path.cwd()
    ignore_list = read_files_in_ignore(root)
    
    # This now returns a list of strings like ["src/main.py", "README.md"]
    results = read_file_outside_ignore(root, ignore_list)

    print("\n\nreuslt", results)






















def read_file_outside_ignore(project_root: Path, ignore_patterns: list):
    # .rglob("*") finds EVERY file and folder recursively
    all_paths = project_root.rglob("*")
    
    valid_paths = []
    
    for p in all_paths:
        # 1. Calculate the path relative to the root (e.g., "src/main.py")
        # This is vital because gitignore patterns are relative to the root.
        relative_path = p.relative_to(project_root)
        
        # 2. Check this path against every pattern in your ignore list
        # Using .match() allows us to handle globs like *.py or logs/*.txt
        is_ignored = any(relative_path.match(pattern) for pattern in ignore_patterns)
        
        # 3. Handle Parent Directories!
        # If 'src' is ignored, then 'src/file.py' must be ignored too.
        if not is_ignored:
            # Check if any parent of this file is in the ignore list
            if not any(parent.match(pattern) for parent in relative_path.parents for pattern in ignore_patterns):
                valid_paths.append(p)


    print(valid_paths)

    return valid_paths