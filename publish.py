#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import re
import subprocess


REPO = Path(__file__).resolve().parent

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


# ============================================================
# Utility functions
# ============================================================

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


def should_ignore(path):
    if ".git" in path.parts:
        return True

    if path.name.startswith("."):
        return True

    if path.suffix.lower() in IGNORED_EXTENSIONS:
        return True

    return False


def clean_name(name):
    return (
        name.replace("_", " ")
        .replace("-", " ")
        .strip()
        .title()
    )


def read_source(path):
    try:
        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception:
        return ""


# ============================================================
# Concept detection
# ============================================================

CONCEPT_RULES = {

    "Bitwise Operations": [
        r"\&",
        r"\|",
        r"\^",
        r"<<",
        r">>",
    ],

    "Conditional Statements": [
        r"\bif\s*\(",
        r"\belse\b",
        r"\bswitch\s*\(",
    ],

    "For Loops": [
        r"\bfor\s*\(",
    ],

    "While Loops": [
        r"\bwhile\s*\(",
    ],

    "Do-While Loops": [
        r"\bdo\b",
    ],

    "Functions": [
        r"\b[a-zA-Z_][a-zA-Z0-9_]*\s+\w+\s*\([^;]*\)\s*\{",
    ],

    "Arrays": [
        r"\[[0-9]*\]",
    ],

    "Pointers": [
        r"\*\s*[a-zA-Z_][a-zA-Z0-9_]*",
        r"&\s*[a-zA-Z_][a-zA-Z0-9_]*",
    ],

    "Structures": [
        r"\bstruct\s+\w+",
    ],

    "Character Handling": [
        r"\bchar\b",
    ],

    "Input / Output": [
        r"\bprintf\s*\(",
        r"\bscanf\s*\(",
        r"\bfgets\s*\(",
        r"\bputs\s*\(",
    ],

    "String Handling": [
        r"\bstrlen\s*\(",
        r"\bstrcpy\s*\(",
        r"\bstrcmp\s*\(",
        r"\bstrcat\s*\(",
    ],

    "Recursion": [
        r"\breturn\s+\w+\s*\(",
    ],

    "Dynamic Memory": [
        r"\bmalloc\s*\(",
        r"\bcalloc\s*\(",
        r"\brealloc\s*\(",
        r"\bfree\s*\(",
    ],

    "Type Casting": [
        r"\([a-zA-Z_][a-zA-Z0-9_]*\)\s*[a-zA-Z0-9_(]",
    ],

}


def detect_concepts(source, filename):

    concepts = set()

    lower_name = filename.lower()
    lower_source = source.lower()

    # Filename-based recognition
    filename_rules = {
        "bitwise": "Bitwise Operations",
        "fibonacci": "Iteration",
        "factorial": "Iteration",
        "prime": "Number Theory",
        "armstrong": "Number Theory",
        "palindrome": "Number Manipulation",
        "reverse": "Number Manipulation",
        "digit": "Number Manipulation",
        "array": "Arrays",
        "pointer": "Pointers",
        "string": "String Handling",
        "char": "Character Handling",
        "switch": "Switch Statements",
        "goto": "Goto Statements",
        "loop": "Loops",
        "function": "Functions",
        "struct": "Structures",
    }

    for keyword, concept in filename_rules.items():
        if keyword in lower_name:
            concepts.add(concept)

    # Source-code recognition
    for concept, patterns in CONCEPT_RULES.items():

        for pattern in patterns:

            try:
                if re.search(
                    pattern,
                    source,
                    re.MULTILINE
                ):
                    concepts.add(concept)
                    break

            except re.error:
                continue

    return sorted(concepts)


# ============================================================
# Program knowledge
# ============================================================

KNOWN_PROGRAMS = {

    "fibonacci": {
        "title": "Fibonacci Sequence",
        "description": (
            "Generates or works with the Fibonacci sequence "
            "using iterative computation."
        ),
        "objective": (
            "Practice iteration, variable updates, and "
            "sequence-based problem solving."
        ),
    },

    "factorial": {
        "title": "Factorial Calculation",
        "description": (
            "Calculates the factorial of a number using "
            "iterative or recursive logic."
        ),
        "objective": (
            "Understand repeated multiplication and "
            "algorithmic iteration."
        ),
    },

    "prime": {
        "title": "Prime Number",
        "description": (
            "Determines whether a number is prime by "
            "checking its possible divisors."
        ),
        "objective": (
            "Practice conditional logic, loops, and "
            "basic number-theory problem solving."
        ),
    },

    "armstrong": {
        "title": "Armstrong Number",
        "description": (
            "Checks whether a number satisfies the "
            "mathematical conditions of an Armstrong number."
        ),
        "objective": (
            "Practice digit extraction, arithmetic operations, "
            "loops, and conditional logic."
        ),
    },

    "bitwise": {
        "title": "Bitwise Operations",
        "description": (
            "Demonstrates operations that manipulate "
            "individual bits within integer values."
        ),
        "objective": (
            "Build an understanding of low-level bit "
            "manipulation used in systems and embedded programming."
        ),
    },

    "fibonacci": {
        "title": "Fibonacci Sequence",
        "description": (
            "Generates values from the Fibonacci sequence "
            "using C programming constructs."
        ),
        "objective": (
            "Practice loops, arithmetic, and maintaining "
            "state across iterations."
        ),
    },

    "cast": {
        "title": "Type Casting",
        "description": (
            "Demonstrates conversion between different "
            "C data types."
        ),
        "objective": (
            "Understand implicit and explicit type conversion "
            "in C."
        ),
    },

    "sizeof": {
        "title": "Sizeof Operator",
        "description": (
            "Explores the sizeof operator and the memory "
            "requirements of C data types."
        ),
        "objective": (
            "Understand how C represents the size of "
            "different data types in memory."
        ),
    },

    "ternary": {
        "title": "Ternary Operator",
        "description": (
            "Demonstrates conditional expressions using "
            "the C ternary operator."
        ),
        "objective": (
            "Practice concise conditional expressions in C."
        ),
    },

    "simple_interest": {
        "title": "Simple Interest",
        "description": (
            "Calculates simple interest using principal, "
            "rate, and time."
        ),
        "objective": (
            "Practice arithmetic operations, variables, "
            "and formatted input/output."
        ),
    },

}


def get_program_information(filename):

    stem = Path(filename).stem.lower()

    for keyword, information in KNOWN_PROGRAMS.items():

        if keyword in stem:
            return information

    return {
        "title": clean_name(Path(filename).stem),
        "description": (
            f"A C programming exercise demonstrating "
            f"the concepts implemented in `{filename}`."
        ),
        "objective": (
            "Strengthen C programming fundamentals through "
            "hands-on implementation and problem solving."
        ),
    }


# ============================================================
# Program README generation
# ============================================================

def create_program_readme(source_file):

    readme = source_file.parent / (
        source_file.stem + "_README.md"
    )

    # Never overwrite a README
    if readme.exists():
        return

    source = read_source(source_file)

    info = get_program_information(
        source_file.name
    )

    concepts = detect_concepts(
        source,
        source_file.name
    )

    lines = [
        f"# {info['title']}",
        "",
        "## Overview",
        "",
        info["description"],
        "",
        "## Concepts Demonstrated",
        "",
    ]

    if concepts:

        for concept in concepts:
            lines.append(f"- {concept}")

    else:

        lines.append(
            "- C programming fundamentals"
        )

    lines.extend([
        "",
        "## Source File",
        "",
        f"- `{source_file.name}`",
        "",
        "## Compilation",
        "",
        "```bash",
        f"gcc {source_file.name} -o {source_file.stem}",
        "```",
        "",
        "## Execution",
        "",
        "```bash",
        f"./{source_file.stem}",
        "```",
        "",
        "## Learning Objective",
        "",
        info["objective"],
        "",
    ])

    readme.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Created: {readme.relative_to(REPO)}"
    )


# ============================================================
# Folder README generation
# ============================================================

def create_folder_readme(directory):

    readme = directory / "README.md"

    # Never overwrite existing README
    if readme.exists():
        return

    source_files = sorted(
        path for path in directory.iterdir()
        if path.is_file()
        and path.suffix.lower() == ".c"
        and not should_ignore(path)
    )

    if not source_files:
        return

    title = clean_name(directory.name)

    all_concepts = set()

    program_information = []

    for source_file in source_files:

        source = read_source(source_file)

        concepts = detect_concepts(
            source,
            source_file.name
        )

        all_concepts.update(concepts)

        info = get_program_information(
            source_file.name
        )

        program_information.append(
            (source_file, info)
        )

    lines = [
        f"# {title}",
        "",
        "## Overview",
        "",
        (
            f"This section contains C programming exercises "
            f"focused on **{title}** and related programming concepts."
        ),
        "",
        "## Programs",
        "",
        "| Program | Description |",
        "|---|---|",
    ]

    for source_file, info in program_information:

        lines.append(
            f"| `{source_file.name}` | "
            f"{info['description']} |"
        )

    lines.extend([
        "",
        "## Concepts Covered",
        "",
    ])

    for concept in sorted(all_concepts):

        lines.append(
            f"- {concept}"
        )

    lines.extend([
        "",
        "## Language",
        "",
        "- C",
        "",
        "## Learning Focus",
        "",
        (
            "These exercises are intended to strengthen "
            "problem-solving skills and practical understanding "
            "of C programming fundamentals."
        ),
        "",
    ])

    readme.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(
        f"Created: {readme.relative_to(REPO)}"
    )


# ============================================================
# README generation
# ============================================================

def generate_program_readmes():

    print("\nGenerating program documentation...")

    source_files = sorted(
        path for path in REPO.rglob("*.c")
        if not should_ignore(path)
    )

    for source_file in source_files:
        create_program_readme(source_file)


def generate_folder_readmes():

    print("\nGenerating folder documentation...")

    directories = sorted(
        path for path in REPO.rglob("*")
        if path.is_dir()
        and ".git" not in path.parts
    )

    for directory in directories:
        create_folder_readme(directory)


# ============================================================
# Main portfolio README
# ============================================================

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
        (
            "A structured collection of C programming exercises, "
            "problem-solving implementations, and programming "
            "fundamentals developed through hands-on practice."
        ),
        "",
        "## Repository Overview",
        "",
        (
            "This repository documents my progression in C "
            "programming through practical exercises covering "
            "fundamentals, control flow, problem solving, "
            "memory concepts, and systems-oriented programming."
        ),
        "",
        "## Topics",
        "",
    ]

    for directory in directories:

        lines.append(
            f"- [{directory.name}](./{directory.name}/)"
        )

    lines.extend([
        "",
        "## Repository Statistics",
        "",
        f"- **C source files:** {len(source_files)}",
        f"- **Main categories:** {len(directories)}",
        "",
        "## Core Areas",
        "",
        "- C programming fundamentals",
        "- Control flow",
        "- Problem solving",
        "- Functions",
        "- Arrays",
        "- Pointers",
        "- Memory concepts",
        "- Number manipulation",
        "- Embedded C foundations",
        "",
        "## Development Environment",
        "",
        "- Linux",
        "- GCC",
        "- Git",
        "- GitHub",
        "",
        "## Documentation",
        "",
        (
            "Each major section contains its own README describing "
            "the programs and concepts covered."
        ),
        "",
    ])

    readme.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print("Updated: README.md")


# ============================================================
# Git publishing
# ============================================================

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


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 60)
    print("        C PROGRAMMING PORTFOLIO PUBLISHER")
    print("=" * 60)

    generate_program_readmes()

    generate_folder_readmes()

    update_main_readme()

    print("\nPublishing changes...")

    git_publish()

    print("\n" + "=" * 60)
    print("             PUBLISH COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
