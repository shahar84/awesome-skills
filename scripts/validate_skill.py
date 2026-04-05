#!/usr/bin/env python3
"""
Validate a skill directory has proper structure and frontmatter.

Usage:
    python validate_skill.py <skill-directory>
    python validate_skill.py skills/imagen-copy-guidelines
"""

import sys
import os
import re
from pathlib import Path

def parse_frontmatter(content: str) -> dict | None:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None

    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value

    return frontmatter

def validate_skill(skill_path: str) -> list[str]:
    """
    Validate a skill directory.
    Returns a list of error messages (empty if valid).
    """
    errors = []
    skill_dir = Path(skill_path)

    # Check directory exists
    if not skill_dir.exists():
        return [f"Skill directory does not exist: {skill_path}"]

    if not skill_dir.is_dir():
        return [f"Path is not a directory: {skill_path}"]

    # Check SKILL.md exists
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"Missing required file: SKILL.md")
        return errors

    # Read and parse SKILL.md
    content = skill_md.read_text(encoding='utf-8')

    # Check frontmatter exists and is valid
    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        errors.append("SKILL.md must start with YAML frontmatter (--- delimited)")
        return errors

    # Check required fields
    if 'name' not in frontmatter:
        errors.append("Frontmatter missing required field: name")

    if 'description' not in frontmatter:
        errors.append("Frontmatter missing required field: description")

    # Validate name matches directory name
    skill_name = skill_dir.name
    if 'name' in frontmatter and frontmatter['name'] != skill_name:
        errors.append(f"Frontmatter 'name' ({frontmatter['name']}) does not match directory name ({skill_name})")

    # Check description is not empty
    if 'description' in frontmatter and len(frontmatter['description'].strip()) < 10:
        errors.append("Description is too short (minimum 10 characters)")

    # Check for broken internal references (skip those inside code blocks/backticks)
    # First remove fenced code blocks (``` ... ```)
    content_without_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Then remove inline code spans (`...`) - non-greedy, single line only
    content_without_code = re.sub(r'`[^`\n]+`', '', content_without_code)

    references_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for match in references_pattern.finditer(content_without_code):
        link_text, link_path = match.groups()
        if not link_path.startswith(('http://', 'https://', '#', 'mailto:')):
            # It's a relative path
            full_path = skill_dir / link_path
            if not full_path.exists():
                errors.append(f"Broken internal reference: {link_path}")

    # Check references directory if mentioned
    if 'references/' in content:
        refs_dir = skill_dir / 'references'
        if not refs_dir.exists():
            errors.append("SKILL.md references 'references/' but directory does not exist")

    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-directory>")
        sys.exit(1)

    skill_path = sys.argv[1].rstrip('/')
    skill_name = os.path.basename(skill_path)

    print(f"Validating skill: {skill_name}")
    errors = validate_skill(skill_path)

    if errors:
        print(f"  FAILED - {len(errors)} error(s):")
        for error in errors:
            print(f"    - {error}")
        sys.exit(1)
    else:
        print(f"  OK")
        sys.exit(0)

if __name__ == "__main__":
    main()
