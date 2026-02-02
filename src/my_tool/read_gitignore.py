from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern

def load_gitignore(repo_root):
    gitignore = repo_root / ".gitignore"
    if not gitignore.exists():
        return PathSpec.from_lines(GitWildMatchPattern, [])
    return PathSpec.from_lines(GitWildMatchPattern, gitignore.read_text().splitlines())
