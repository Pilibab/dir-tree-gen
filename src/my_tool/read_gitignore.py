from pathlib import Path



def get_top_level(project_root: Path):
    patterns = []
    # Use 'with open' to ensure the file is properly closed after reading
    try:
        with open(project_root / ".gitignore", 'r') as f:
            for line in f:
                # Strip leading/trailing whitespace (including newline characters)
                line = line.strip()
                # Ignore blank lines and comments (lines starting with '#')
                if line and not line.startswith('#'):
                    patterns.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{project_root}' was not found.")
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