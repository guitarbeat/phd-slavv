"""Canonical skill identity and task-relevant local resources for discovery tools."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

LIBRARY_SKILLS = Path(__file__).resolve().parents[2]
ALIAS_PATH = LIBRARY_SKILLS.parent / "skill-aliases.json"


def find_repository_root(start: Path) -> Path | None:
    """Find the nearest Git checkout, including worktrees with a .git file."""
    start = start.resolve()
    for directory in (start, *start.parents):
        if (directory / ".git").exists():
            return directory
    return None


@dataclass(frozen=True)
class Skill:
    name: str
    description: str
    body: str
    path: Path


def canonical_name(name: str, aliases: dict[str, str] | None = None) -> str:
    if aliases is None:
        aliases = json.loads(ALIAS_PATH.read_text(encoding="utf-8"))
    seen = set()
    while name in aliases:
        if name in seen:
            raise ValueError(f"Alias cycle at {name}")
        seen.add(name)
        name = aliases[name]
    return name


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter: {path}")
    metadata = yaml.safe_load(match[1])
    if not isinstance(metadata, dict):
        raise ValueError(f"Frontmatter is not a mapping: {path}")
    return metadata


def effective_body(manifest: Path, repository: str | None = None) -> str:
    """Read linked procedures inside this skill, filtering repository-specific modes.

    Two link levels cover entrypoint -> selected procedure -> procedure reference.
    Never follow links into other skills, repositories, URLs, or user home folders.
    """
    skill_root = manifest.resolve().parent
    visited = set()
    texts = []

    def visit(path: Path, depth: int) -> None:
        path = path.resolve()
        if path in visited or not path.is_relative_to(skill_root) or not path.is_file():
            return
        visited.add(path)
        text = path.read_text(encoding="utf-8")
        texts.append(text)
        if depth == 2:
            return
        prose = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", "", text)
        for link in re.findall(r"\]\(([^)]+)\)", prose):
            link = link.strip("<>").split("#", 1)[0]
            if not link or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                continue
            resource = (path.parent / link).resolve()
            if resource.suffix != ".md" or not resource.is_relative_to(skill_root):
                continue
            parts = resource.relative_to(skill_root).parts
            if "modes" in parts and repository:
                mode = parts[parts.index("modes") + 1]
                if mode.startswith("phd-") and not mode.startswith(repository + "-"):
                    continue
            visit(resource, depth + 1)

    visit(manifest, 0)
    return "\n\n".join(texts)


def load_catalog(
    skills_root: Path = LIBRARY_SKILLS, repository: str | None = None
) -> list[Skill]:
    skills = {}
    for manifest in sorted(skills_root.glob("*/SKILL.md")):
        metadata = read_frontmatter(manifest)
        name = canonical_name(metadata.get("name") or manifest.parent.name)
        skills[name] = Skill(
            name,
            metadata.get("description", ""),
            effective_body(manifest, repository),
            manifest.resolve(),
        )
    return list(skills.values())
