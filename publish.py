#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import subprocess


# --------------------------------------------------
# Configuration
# --------------------------------------------------

REPO = Path(__file__).resolve().parent

IGNORED_FILES = {
    ".git",
    ".gitignore",
    "publish.py",
}

IGNORED_EXTENSIONS = {
    ".out",
    ".o",
    ".swp",
    ".swo",
}

SOURCE_EXTENSIONS = {
    ".c",
    ".h",
}


# --------------------------------------------------
# Run shell commands
# --------------------------------------------------

def run(command):
    print(f"\n$ {command}")
    result = subprocess.run(
        command,
        shell=True,
        cwd=REPO,
        text=True
    )

    if result.returncode != 0:
        raise SystemExit(
            f"\nCommand failed: {command}"
        )


# --------------------------------------------------
# Check whether a file should be ignored
# --------------------------------------------------

def should_ignore(path):
    if path.name in IGNORED_FILES:
        return True

    if path.suffix.lower() in IGNORED_EXTENSIONS:
        return True

    if path.name.startswith("."):
        return True

    return False


# --------------------------------------------------
# Create README for a directory
# --------------------------------------------------

def create_readme(directory):
    readme = directory / "README.md"

    if readme.exists():
        return

    source_files = sorted(
        file for file in directory.iterdir()
        if file.is_file()
        and file.suffix.lower() in SOURCE_EXTENSIONS
        and not should_ignore(file)
    )

    subdirectories = sorted(
        directory.iterdir()
    )

    title = directory.name.replace("_", " ").replace("-", " ").title()

    lines = [
        f"# {title}",
        "",
        "## Overview",
        "",
        f"This directory contains C programming exercises "
        f"and examples related to **{title}**.",
        "",
    ]

    if source_files:
        lines.extend([
            "## Programs",
            "",
            "| File | Description |",
            "|---|---|",
        ])

        for file in source_files:
            description = (
                file.stem
                .replace("_", " ")
                .replace("-", " ")
                .title()
            )

            lines.append(
                f"| `{file.name}` | {description} |"
            )

        lines.append("")

    child_dirs = [
        item for item in subdirectories
        if item.is_dir()
        and item.name != ".git"
    ]

    if child_dirs:
        lines.extend([
            "## Subdirectories",
            "",
        ])

        for child in child_dirs:
            lines.append(
                f"- [{child.name}](./{child.name}/)"
            )

        lines.append("")

    lines.extend([
        "## Language",
        "",
        "- C",
        "",
        "## Purpose",
        "",
        "Practice and strengthen C programming fundamentals "
        "through hands-on implementations.",
        "",
    ])

    readme.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"Created: {readme.relative_to(REPO)}")


# --------------------------------------------------
# Create README files
# --------------------------------------------------

def generate_readmes():
    print("\nGenerating README files...")

    directories = sorted(
        path for path in REPO.rglob("*")
        if path.is_dir()
        and ".git" not in path.parts
    )

    for directory in directories:
        create_readme(directory)


# --------------------------------------------------
# Create/update main README
# --------------------------------------------------

def update_main_readme():
    readme = REPO / "README.md"

    directories = sorted(
        path for path in REPO.iterdir()
        if path.is_dir()
        and path.name != ".git"
        and not path.name.startswith(".")
    )

    source_files = sorted(
        path for path in REPO.rglob("*.c")
        if ".git" not in path.parts
    )

    lines = [
        "# C Programming Portfolio",
        "",
        "A structured collection of C programming exercises "
        "and implementations developed through hands-on practice.",
        "",
        "## Topics",
        "",
    ]

    for directory in directories:
        lines.append(
            f"- [{directory.name}]"
            f"(./{directory.name}/)"
        )

    lines.extend([
        "",
        "## Repository Statistics",
        "",
        f"- C source files: **{len(source_files)}**",
        f"- Main categories: **{len(directories)}**",
        "",
        "## Focus Areas",
        "",
        "- C programming fundamentals",
        "- Problem solving",
        "- Control structures",
        "- Functions",
        "- Pointers",
        "- Data structures",
        "- Embedded C foundations",
        "",
    ])

    readme.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print("Updated: README.md")


# --------------------------------------------------
# Git operations
# --------------------------------------------------

def git_publish():

    run("git add .")

    status = subprocess.run(
        "git status --short",
        shell=True,
        cwd=REPO,
        text=True,
        capture_output=True
    )

    if not status.stdout.strip():
        print("\nNo changes to publish.")
        return

    print("\nChanges that will be committed:")
    print(status.stdout)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )

    commit_message = (
        f"docs: update C programming portfolio "
        f"{timestamp}"
    )

    run(
        f'git commit -m "{commit_message}"'
    )

    run("git push")


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    print("=" * 60)
    print("        C PROGRAMMING PORTFOLIO PUBLISHER")
    print("=" * 60)

    generate_readmes()

    update_main_readme()

    print("\nPublishing changes...")

    git_publish()

    print("\n" + "=" * 60)
    print("             PUBLISH COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
