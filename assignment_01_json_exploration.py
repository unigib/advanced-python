"""Assignment 1: load a JSON file and explore its Python data structures."""

import json
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).parent / "data" / "library.json"


def print_category(category: dict[str, Any], indent: str = "") -> None:
    """Print books in a category and its immediate subcategories."""
    print(f"{indent}Category: {category['name']}")

    for book in category["books"]:
        print(f"{indent}  - {book['title']} by {book['author']}")

    for subcategory in category["subcategories"]:
        print(f"{indent}  Subcategory: {subcategory['name']}")
        for book in subcategory["books"]:
            print(f"{indent}    - {book['title']} by {book['author']}")


def main() -> None:
    # json.load converts JSON objects to dictionaries and arrays to lists.
    with DATA_FILE.open(encoding="utf-8") as file:
        library = json.load(file)

    print(f"Loaded {DATA_FILE.name}")
    print(f"Top-level Python type: {type(library).__name__}")
    print(f"Top-level keys: {list(library.keys())}")
    print(f"Library name: {library['name']}")
    print(f"Categories value type: {type(library['categories']).__name__}")
    print()

    # Traverse the list of categories, then each category's lists and dictionaries.
    for category in library["categories"]:
        print_category(category)

    # A JSON book object is now a Python dict, so its fields can be accessed by key.
    first_book = library["categories"][0]["books"][0]
    print()
    print(f"First book's year: {first_book['year']}")
    print(f"First book's fields: {list(first_book.keys())}")


if __name__ == "__main__":
    main()
