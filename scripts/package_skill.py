#!/usr/bin/env python3
"""
Package a skill directory into a distributable .skill file.

A .skill file is a zip archive containing the skill directory contents.
Users can double-click to install in Cowork or drag into Claude Code.

Usage:
    python package_skill.py <skill-directory> [output-directory]
    python package_skill.py skills/imagen-copy-guidelines
    python package_skill.py skills/imagen-copy-guidelines dist/
"""

import sys
import os
import zipfile
from pathlib import Path

def package_skill(skill_path: str, output_dir: str = ".") -> str:
    """
    Package a skill directory into a .skill file.
    Returns the path to the created .skill file.
    """
    skill_dir = Path(skill_path)
    output_path = Path(output_dir)

    if not skill_dir.exists():
        raise FileNotFoundError(f"Skill directory does not exist: {skill_path}")

    if not skill_dir.is_dir():
        raise ValueError(f"Path is not a directory: {skill_path}")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"Missing SKILL.md in {skill_path}")

    # Create output directory if needed
    output_path.mkdir(parents=True, exist_ok=True)

    # Create .skill file (zip archive)
    skill_name = skill_dir.name
    skill_file = output_path / f"{skill_name}.skill"

    with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_dir.rglob('*'):
            if file_path.is_file():
                # Skip hidden files and common junk
                if any(part.startswith('.') for part in file_path.parts):
                    continue
                if file_path.name in ['.DS_Store', 'Thumbs.db', '__pycache__']:
                    continue

                # Archive with skill name as root directory
                arcname = str(skill_name / file_path.relative_to(skill_dir))
                zf.write(file_path, arcname)

    return str(skill_file)

def main():
    if len(sys.argv) < 2:
        print("Usage: package_skill.py <skill-directory> [output-directory]")
        sys.exit(1)

    skill_path = sys.argv[1].rstrip('/')
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    skill_name = os.path.basename(skill_path)
    print(f"Packaging skill: {skill_name}")

    try:
        skill_file = package_skill(skill_path, output_dir)
        file_size = os.path.getsize(skill_file)
        print(f"  Created: {skill_file} ({file_size:,} bytes)")
        sys.exit(0)
    except Exception as e:
        print(f"  FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
