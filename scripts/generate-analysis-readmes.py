#!/usr/bin/env python3
"""Generate README.md files for all analysis domain and subdomain directories."""

import os
import re
from pathlib import Path

ANALYSIS_DIR = Path("analysis")

# File descriptions for numbered files
FILE_DESCRIPTIONS = {
    "01-overview.md": "Executive summary and scope",
    "02-current-state.md": "Present-day conditions and data",
    "03-history.md": "Historical context and evolution",
    "04-root-causes.md": "Systemic analysis of why problems exist",
    "05-stakeholders.md": "Who is affected and who has power",
    "06-opposition.md": "Who opposes reform and why",
    "07-solutions.md": "Proposed reforms and interventions",
    "08-roadmap.md": "Implementation timeline and sequencing",
    "09-resources.md": "Further reading and citations",
    "10-actions.md": "What citizens can do",
    "11-legislation.md": "Draft legal text and model legislation",
    "12-perspectives.md": "Political perspectives analysis",
}

def get_title_from_overview(dir_path: Path) -> str:
    """Extract H1 title from 01-overview.md."""
    overview = dir_path / "01-overview.md"
    if overview.exists():
        with open(overview, "r") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    # Fallback: convert directory name to title
    return dir_path.name.replace("-", " ").title()


def get_description_from_overview(overview_path: Path) -> str:
    """Extract description from overview file (various section patterns)."""
    if not overview_path.exists():
        return ""

    with open(overview_path, "r") as f:
        content = f.read()

    def is_valid_description(text: str) -> bool:
        """Check if text is valid (not placeholder, right length)."""
        if not text:
            return False
        # Skip placeholders like [Brief summary...] or template text
        if text.startswith("[") or "TBD" in text or "[placeholder" in text.lower():
            return False
        # Skip if it looks like a list or table
        if text.startswith("-") or text.startswith("|") or text.startswith("*"):
            return False
        return 50 < len(text) < 1200

    # Try different section headers in order of preference
    section_patterns = [
        r"## Executive Summary\s*\n\n(.+?)(?=\n\n)",
        r"## Overview\s*\n\n(.+?)(?=\n\n)",
        r"## Introduction\s*\n\n(.+?)(?=\n\n)",
        r"## Definition\s*\n\n(.+?)(?=\n\n)",
        r"## What Is .+?\s*\n\n(.+?)(?=\n\n)",
        r"## Why It Matters\s*\n\n(.+?)(?=\n\n)",
    ]

    for pattern in section_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            first_para = match.group(1).strip()
            if is_valid_description(first_para):
                return first_para

    # Fallback: try to get first paragraph after title (before any ## heading)
    match = re.search(r"^# .+\n\n([^#\n].+?)(?=\n\n)", content, re.MULTILINE | re.DOTALL)
    if match:
        para = match.group(1).strip()
        if is_valid_description(para):
            return para

    return ""


def get_subdirectories(dir_path: Path) -> list[tuple[str, str]]:
    """Get list of subdirectories with their titles."""
    subdirs = []
    for item in sorted(dir_path.iterdir()):
        if item.is_dir():
            title = get_title_from_overview(item)
            subdirs.append((item.name, title))
    return subdirs


def get_numbered_files(dir_path: Path) -> list[str]:
    """Get list of numbered .md files (01-12)."""
    files = []
    for f in sorted(dir_path.glob("*.md")):
        if re.match(r"^\d{2}-", f.name) and f.name != "README.md":
            files.append(f.name)
    return files


def format_dir_name(name: str) -> str:
    """Convert directory name to readable format."""
    return name.replace("-", " ").title()


def generate_domain_readme(domain_path: Path) -> str:
    """Generate README content for a top-level domain."""
    title = get_title_from_overview(domain_path)
    domain_name = domain_path.name
    subdirs = get_subdirectories(domain_path)
    files = get_numbered_files(domain_path)

    lines = [
        f"# {title}",
        "",
    ]

    # Add description from overview if available
    overview = domain_path / "01-overview.md"
    desc = get_description_from_overview(overview)
    if desc:
        lines.extend([desc, ""])

    # List subtopics if any
    if subdirs:
        lines.extend([
            "## Subtopics",
            "",
        ])
        for subdir_name, subdir_title in subdirs:
            lines.append(f"- [{subdir_title}]({subdir_name}/)")
        lines.append("")

    # List files
    if files:
        lines.extend([
            "## Files",
            "",
            "| File | Description |",
            "|------|-------------|",
        ])
        for f in files:
            desc = FILE_DESCRIPTIONS.get(f, "")
            lines.append(f"| [{f}]({f}) | {desc} |")
        lines.append("")

    # Navigation
    lines.extend([
        "---",
        "",
        "*[Back to Analysis Overview](../01-overview.md)*",
        "",
    ])

    return "\n".join(lines)


def generate_subdomain_readme(subdomain_path: Path) -> str:
    """Generate README content for a subdomain directory."""
    title = get_title_from_overview(subdomain_path)
    parent_name = subdomain_path.parent.name
    parent_title = get_title_from_overview(subdomain_path.parent)
    files = get_numbered_files(subdomain_path)

    lines = [
        f"# {title}",
        "",
    ]

    # Add description from overview if available
    overview = subdomain_path / "01-overview.md"
    desc = get_description_from_overview(overview)
    if desc:
        lines.extend([desc, ""])

    # List files
    if files:
        lines.extend([
            "## Files",
            "",
            "| File | Description |",
            "|------|-------------|",
        ])
        for f in files:
            desc = FILE_DESCRIPTIONS.get(f, "")
            lines.append(f"| [{f}]({f}) | {desc} |")
        lines.append("")

    # Navigation
    lines.extend([
        "---",
        "",
        f"*Part of [{parent_title}](../README.md)*",
        "",
    ])

    return "\n".join(lines)


def main():
    """Generate all README files."""
    created = 0

    # Process each domain
    for domain in sorted(ANALYSIS_DIR.iterdir()):
        if not domain.is_dir():
            continue

        # Generate domain README
        readme_path = domain / "README.md"
        content = generate_domain_readme(domain)
        with open(readme_path, "w") as f:
            f.write(content)
        print(f"Created: {readme_path}")
        created += 1

        # Process subdirectories
        for subdir in sorted(domain.iterdir()):
            if not subdir.is_dir():
                continue

            readme_path = subdir / "README.md"
            content = generate_subdomain_readme(subdir)
            with open(readme_path, "w") as f:
                f.write(content)
            print(f"Created: {readme_path}")
            created += 1

    print(f"\nTotal README files created: {created}")


if __name__ == "__main__":
    main()
