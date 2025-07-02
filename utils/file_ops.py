import os
from pathlib import Path

def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def read_text_file(filepath: str) -> str:
    """Read the entire contents of a text file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_text_file(filepath: str, content: str) -> None:
    """Write string content to a text file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def list_files(dir_path: str, extensions=None) -> list[str]:
    """List files in directory, optionally filtering by extensions."""
    files = []
    for f in os.listdir(dir_path):
        if extensions is None or f.lower().endswith(tuple(extensions)):
            files.append(os.path.join(dir_path, f))
    return files

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to be safe on all OSes."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()
