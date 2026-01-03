import pathspec
from pathlib import Path


def get_top_level(project_root: Path):
    project_root = project_root.resolve()
    gitignore_path = project_root / ".gitignore"

    if not gitignore_path.exists():
        return []

    with gitignore_path.open("r") as f:
        spec = pathspec.PathSpec.from_lines("gitwildmatch", f)

    ignore = set()

    for match in spec.match_tree(project_root):
        p = Path(match)

        # Normalize to absolute path
        if not p.is_absolute():
            p = project_root / p

        try:
            rel = p.relative_to(project_root)
            ignore.add(rel.parts[0])
        except ValueError:
            # Defensive: ignore anything outside the project root
            continue

    return sorted(ignore)
