from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from skill_catalog import (
    LIBRARY_SKILLS,
    Skill,
    canonical_name,
    find_repository_root,
    load_catalog,
)


@dataclass(frozen=True)
class ScanContext:
    repo_root: Path
    skills_root: Path = LIBRARY_SKILLS

    def skill_target(self, name: str) -> str:
        return str(self.skills_root / canonical_name(name) / "SKILL.md")


@dataclass(frozen=True)
class Candidate:
    name: str
    kind: str
    evidence: str
    reason: str
    target: str


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_skills(context: ScanContext) -> list[Skill]:
    return load_catalog(context.skills_root, repository=context.repo_root.name)


def has_skill(skills: list[Skill], *terms: str) -> bool:
    haystack = "\n".join(
        f"{skill.name} {skill.description} {skill.body}" for skill in skills
    ).lower()
    return all(term.lower() in haystack for term in terms)


def skill_body_contains(skills: list[Skill], skill_name: str, phrase: str) -> bool:
    for skill in skills:
        if skill.name == canonical_name(skill_name):
            return phrase.lower() in skill.body.lower()
    return False


def active_checkboxes(text: str) -> list[str]:
    return [
        line.strip() for line in text.splitlines() if line.strip().startswith("- [ ]")
    ]


def active_blockers(text: str) -> list[str]:
    in_blockers = False
    blockers: list[str] = []
    for line in text.splitlines():
        if line.startswith("## ") and "Active blockers" in line:
            in_blockers = True
            continue
        if in_blockers and line.startswith("## "):
            break
        if in_blockers and re.match(r"\d+\.\s+\*\*", line):
            blockers.append(line.strip())
    return blockers


def solution_count(directory: Path) -> int:
    if not directory.exists():
        return 0
    return sum(
        1 for path in directory.rglob("*.md") if path.name.lower() != "readme.md"
    )


def parity_candidates(
    skills: list[Skill], context: ScanContext, parity_evidence: str
) -> list[Candidate]:
    candidates: list[Candidate] = []
    if parity_evidence and not has_skill(skills, "parity", "proof"):
        candidates.append(
            Candidate(
                name="parity-proof-compounder",
                kind="new skill",
                evidence=parity_evidence,
                reason=(
                    "Active parity work repeatedly asks agents to check run status, "
                    "prove the first failing stage, record findings, and promote verified fixes."
                ),
                target=context.skill_target("parity-proof-compounder"),
            )
        )
    elif parity_evidence and not skill_body_contains(
        skills,
        "self-improving-agent",
        "For parity proof sessions",
    ):
        candidates.append(
            Candidate(
                name="strengthen existing parity skills",
                kind="skill edit",
                evidence=parity_evidence,
                reason=(
                    "Parity is already covered by docs and prompts, but the generative promotion step "
                    "should explicitly create solution notes or skill edits after verified failures."
                ),
                target=context.skill_target("self-improving-agent"),
            )
        )

    return candidates


def solution_candidates(
    skills: list[Skill], context: ScanContext, count: int
) -> list[Candidate]:
    candidates: list[Candidate] = []
    if count <= 1 and not has_skill(skills, "solution", "note"):
        candidates.append(
            Candidate(
                name="solution-note-generator",
                kind="new skill",
                evidence=f"Only {count} documented solution note(s) found under docs/solutions.",
                reason=(
                    "The docs describe a compound-solutions workflow, but there is little searchable "
                    "solution history relative to the amount of parity and integration debugging."
                ),
                target=context.skill_target("solution-note-generator"),
            )
        )
    elif count <= 1:
        candidates.append(
            Candidate(
                name="exercise solution-note-generator",
                kind="scratch reflection",
                evidence=f"Only {count} documented solution note(s) found, but a solution-note skill exists.",
                reason=(
                    "The next generative step is to use the skill after the next verified parity or "
                    "integration fix, then check whether its template captured enough evidence."
                ),
                target="workspace/scratch/agent-reflections.md",
            )
        )

    return candidates


def run_ops_candidates(
    skills: list[Skill], context: ScanContext, tasks: list[str]
) -> list[Candidate]:
    candidates: list[Candidate] = []
    if any(
        "monitor" in task.lower() or "rerun" in task.lower() for task in tasks
    ) and not skill_body_contains(skills, "control-cli", "SLAVV Run Ops"):
        candidates.append(
            Candidate(
                name="run-ops-watch",
                kind="skill edit",
                evidence="Active tasks mention reruns, PIDs, duplicate writers, and monitor/status commands.",
                reason=(
                    "Run operations are a recurring workflow; strengthen control-cli or add a narrow "
                    "run-monitoring workflow only if agents keep missing the PID/duplicate-writer guard."
                ),
                target=context.skill_target("control-cli"),
            )
        )

    return candidates


def preflight_candidates(skills: list[Skill], context: ScanContext) -> list[Candidate]:
    candidates: list[Candidate] = []
    if (
        has_skill(skills, "workflow", "chats")
        and has_skill(skills, "self", "improving")
        and not skill_body_contains(skills, "find-skills", "Generative Skill Loop")
    ):
        candidates.append(
            Candidate(
                name="preflight skill selection",
                kind="skill edit",
                evidence="Both workflow-from-chats and self-improving-agent exist.",
                reason=(
                    "Before creating any new skill, agents should run local skill discovery and decide "
                    "whether the evidence belongs in an existing skill, a solution note, or scratch."
                ),
                target=context.skill_target("find-agent-skills"),
            )
        )

    return candidates


def build_candidates(skills: list[Skill], context: ScanContext) -> list[Candidate]:
    tasks = active_checkboxes(read_text(context.repo_root / "docs/TODO.md"))
    blockers = active_blockers(
        read_text(context.repo_root / "docs/reference/core/EXACT_PROOF_FINDINGS.md")
    )
    parity_evidence = "; ".join((tasks + blockers)[:3])
    count = solution_count(context.repo_root / "docs/solutions")
    return (
        parity_candidates(skills, context, parity_evidence)
        + solution_candidates(skills, context, count)
        + run_ops_candidates(skills, context, tasks)
        + preflight_candidates(skills, context)
    )


def render_markdown(candidates: list[Candidate]) -> str:
    if not candidates:
        return "No generative skill candidates found.\n"
    lines = ["# Generative Skill Candidates", ""]
    for candidate in candidates:
        lines.extend(
            [
                f"## {candidate.name}",
                "",
                f"- Kind: {candidate.kind}",
                f"- Evidence: {candidate.evidence}",
                f"- Reason: {candidate.reason}",
                f"- Target: `{candidate.target}`",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Suggest generative skill candidates from repo signals."
    )
    parser.add_argument("--format", choices=["markdown"], default="markdown")
    parser.add_argument(
        "--repo-root",
        type=Path,
        help="Repository whose work signals to inspect; inferred from the working directory by default.",
    )
    parser.add_argument("--skills-root", type=Path, default=LIBRARY_SKILLS)
    args = parser.parse_args()
    repo_root = (
        args.repo_root.resolve()
        if args.repo_root
        else find_repository_root(Path.cwd()) or Path.cwd()
    )
    context = ScanContext(repo_root, args.skills_root.resolve())
    candidates = build_candidates(load_skills(context), context)
    if args.format == "markdown":
        print(render_markdown(candidates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
