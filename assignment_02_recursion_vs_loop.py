"""Assignment 2: count books recursively and with a loop."""

import json
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).parent / "data" / "library.json"


def count_books_recursive(categories: list[dict[str, Any]]) -> int:
    """Count books in categories and all of their nested subcategories."""
    total = 0

    for category in categories:
        total += len(category["books"])
        total += count_books_recursive(category["subcategories"])

    return total


def count_books_iterative(categories: list[dict[str, Any]]) -> int:
    """Count books using a loop and an explicit stack of categories."""
    total = 0
    pending = list(categories)

    while pending:
        category = pending.pop()
        total += len(category["books"])
        pending.extend(category["subcategories"])

    return total


def main() -> None:
    with DATA_FILE.open(encoding="utf-8") as file:
        library = json.load(file)

    recursive_total = count_books_recursive(library["categories"])
    iterative_total = count_books_iterative(library["categories"])

    print(f"Books counted recursively: {recursive_total}")
    print(f"Books counted with a loop: {iterative_total}")
    print(f"Both approaches agree: {recursive_total == iterative_total}")


if __name__ == "__main__":
    main()
