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


def read_file_outside_ignore(file_path : Path):
    

def test_read_gitignore_contains_required_folders():
    # 1. Setup
    to_scan = Path.cwd()
    
    # 2. Action
    ignore_list = get_top_level(to_scan)

    print(ignore_list)
    
    # 3. Assert (Check if individual items exist in the result)
    assert ".git" in ignore_list
    assert ".venv" in ignore_list
    assert "__pycache__" in ignore_list
    assert ".idea" in ignore_list
    
    # check for things that SHOULD NOT be there
    assert "src" not in ignore_list
