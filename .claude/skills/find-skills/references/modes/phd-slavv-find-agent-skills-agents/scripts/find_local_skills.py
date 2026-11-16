from __future__ import annotations

import argparse
from pathlib import Path

from skill_catalog import LIBRARY_SKILLS, find_repository_root, load_catalog


def score(query: str, name: str, description: str, body: str) -> int:
    terms = [term.lower() for term in query.split() if term.strip()]
    haystack = f"{name} {description} {body}".lower()
    return sum(1 for term in terms if term in haystack)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search project-local agent skills.")
    parser.add_argument("query", nargs="*", help="Search terms.")
    parser.add_argument(
        "--root",
        type=Path,
        default=LIBRARY_SKILLS,
        help="Skills directory to scan.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        help="Repository whose procedures to search; inferred from the working directory by default.",
    )
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    repository = (
        args.repo_root.resolve() if args.repo_root else find_repository_root(Path.cwd())
    )
    rows: list[tuple[int, str, str, Path]] = []
    for skill in load_catalog(
        args.root, repository=repository.name if repository else None
    ):
        skill_file = skill.path
        body = skill.body
        name = skill.name
        description = skill.description
        rank = score(query, name, description, body) if query else 1
        if rank or not query:
            rows.append((rank, name, description, skill_file))

    rows.sort(key=lambda row: (-row[0], row[1]))
    for _, name, description, path in rows:
        print(f"{name}\t{path}\t{description}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
