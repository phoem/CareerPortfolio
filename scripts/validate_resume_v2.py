#!/usr/bin/env python3
"""Generate evidence-aware ATS readiness reports for resume artifact sets."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

VERSION = "0.2.0"
BAD_GLYPHS = ("�", "□", "■", "\x00")
STOPWORDS = {
    "the", "and", "or", "to", "of", "a", "in", "for", "with", "on", "as",
    "is", "are", "be", "will", "you", "we", "our", "this", "that", "from",
    "at", "by", "an", "have", "has", "using", "work", "role", "team", "your",
    "experience", "years", "including", "across", "their", "they",
}
CONTACT_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone": re.compile(r"(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}"),
}
DATE_PATTERN = re.compile(
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\s+\d{4}\b|\b\d{4}\s*[-–]\s*(?:\d{4}|Present)\b", re.I,
)
ALIASES = {
    "c/c++": {"c", "c++", "c/c++"},
    "tcp": {"tcp", "tcp/ip"},
    "open source": {"open source", "open-source", "github", "public repositories"},
    "nri": {"nri", "node resource interface"},
    "kubelet": {"kubelet", "kubelets"},
    "ai/ml": {"ai/ml", "ai", "ml", "machine learning"},
}
LIMITING_PHRASES = (
    "experimental", "experiments", "exploratory", "familiarity", "familiar with",
    "fundamentals", "conceptual", "has not", "have not", "no claim", "not production",
)


@dataclass
class CategoryScore:
    score: int
    findings: list[str]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"[`*_>#|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokens(text: str) -> list[str]:
    values = re.findall(r"[A-Za-z][A-Za-z0-9+#./-]*", text.lower())
    return [value for value in values if value not in STOPWORDS and len(value) > 1]


def extract_docx(path: Path) -> str:
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    paragraphs = []
    for paragraph in root.findall(".//w:p", namespace):
        parts = [node.text or "" for node in paragraph.findall(".//w:t", namespace)]
        if parts:
            paragraphs.append("".join(parts))
    return "\n".join(paragraphs)


def extract_pdf(path: Path) -> str:
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "pdf.txt"
        process = subprocess.run(
            ["pdftotext", "-layout", str(path), str(output)],
            text=True, capture_output=True, check=False,
        )
        if process.returncode:
            raise RuntimeError(process.stderr.strip() or "pdftotext failed")
        return output.read_text(encoding="utf-8", errors="replace")


def coverage(source: str, artifact: str) -> float:
    source_tokens = set(tokens(normalize(source)))
    artifact_tokens = set(tokens(normalize(artifact)))
    return 1.0 if not source_tokens else len(source_tokens & artifact_tokens) / len(source_tokens)


def score_parseability(markdown: str, docx: str, pdf: str) -> CategoryScore:
    score = 100
    findings = []
    for name, text in (("DOCX", docx), ("PDF", pdf)):
        value = coverage(markdown, text)
        if value < 0.80:
            score -= 35
        elif value < 0.90:
            score -= 20
        elif value < 0.96:
            score -= 8
        findings.append(f"{name} token coverage versus Markdown: {value:.1%}.")
        if any(glyph in text for glyph in BAD_GLYPHS):
            score -= 15
            findings.append(f"{name} contains suspicious or corrupted glyphs.")
    if len(normalize(pdf)) < 500:
        score -= 40
        findings.append("PDF extraction returned unusually little text.")
    return CategoryScore(max(0, score), findings)


def score_completeness(markdown: str) -> CategoryScore:
    score = 100
    findings = []
    lower = markdown.lower()
    for label, pattern in CONTACT_PATTERNS.items():
        if not pattern.search(markdown):
            score -= 15
            findings.append(f"Missing recognizable {label}.")
    for heading in ("## summary", "## professional experience", "## education"):
        if heading not in lower:
            score -= 15
            findings.append(f"Missing conventional {heading[3:].title()} heading.")
    if len(DATE_PATTERN.findall(markdown)) < 3:
        score -= 15
        findings.append("Work-history dates may be incomplete or inconsistently parseable.")
    if re.search(r"\b(TODO|TBD|PLACEHOLDER|FIXME)\b", markdown, re.I):
        score -= 30
        findings.append("Placeholder text remains.")
    if not findings:
        findings.append("Contact details, conventional sections, and work-history dates are present.")
    return CategoryScore(max(0, score), findings)


def extract_requirements(job: str) -> tuple[list[str], list[str]]:
    required, preferred = [], []
    mode: str | None = None
    for raw in job.splitlines():
        stripped = raw.strip()
        heading = re.sub(r"^#+\s*", "", stripped).strip().lower()
        if stripped.startswith("#"):
            if heading in {"what we are looking for", "required qualifications", "requirements", "qualifications"}:
                mode = "required"
            elif heading in {"additionally helpful experience", "preferred qualifications", "nice to have", "bonus qualifications"}:
                mode = "preferred"
            else:
                mode = None
            continue
        if mode and stripped.startswith(("-", "*", "•")):
            line = stripped.lstrip("-*• ").strip()
            if len(line.split()) >= 3:
                (required if mode == "required" else preferred).append(line)
    return required, preferred


def phrase_present(phrase: str, resume_lower: str) -> bool:
    options = ALIASES.get(phrase, {phrase})
    return any(re.search(rf"(?<![a-z0-9]){re.escape(option)}(?![a-z0-9])", resume_lower) for option in options)


def evidence_context(term: str, resume: str) -> str:
    lower = resume.lower()
    options = ALIASES.get(term, {term})
    positions = [lower.find(option) for option in options if lower.find(option) >= 0]
    if not positions:
        return ""
    position = min(positions)
    return lower[max(0, position - 180): position + 240]


def requirement_match(requirement: str, resume: str) -> tuple[str, float, list[str]]:
    req_lower = requirement.lower()
    resume_lower = resume.lower()
    req_tokens = list(dict.fromkeys(tokens(requirement)))
    matched = [term for term in req_tokens if phrase_present(term, resume_lower)]
    ratio = len(matched) / max(1, len(req_tokens))

    # Explicit capability patterns that ordinary tokenization often misses.
    if "proficiency in go, java, or c/c++" in req_lower:
        direct = bool(re.search(r"\bgo\b", resume_lower)) or "c++" in resume_lower or bool(re.search(r"\bc\b", resume_lower))
        return ("direct" if direct else "missing", 1.0 if direct else 0.0, ["Go/C/C++"] if direct else [])

    limiting = False
    for term in matched:
        context = evidence_context(term, resume)
        if any(phrase in context for phrase in LIMITING_PHRASES):
            limiting = True
            break

    # Prevent keyword-only false positives for contribution/development requirements.
    if "contribute to the upstream" in req_lower:
        if re.search(r"(contributed|contributions?)\s+to\s+(upstream|kubernetes|containerd)", resume_lower):
            return "direct", 1.0, ["upstream contributions"]
        return "missing", ratio, matched
    if "linux kernel development" in req_lower:
        if re.search(r"linux kernel (module|development|patch|contribution)", resume_lower) and "has not written" not in resume_lower:
            return "direct", ratio, matched
        if "linux kernel" in resume_lower and ("freebsd kernel" in resume_lower or "kernel modules" in resume_lower):
            return "adjacent", ratio, matched
        return "missing", ratio, matched
    if "ai/ml workloads" in req_lower:
        if re.search(r"(managed|operated|supported|owned).{0,80}(ai/ml|machine learning|ml workloads)", resume_lower):
            return "direct", ratio, matched
        return "missing", ratio, matched
    if "customizations and plugins" in req_lower and limiting:
        return "adjacent", ratio, matched
    if "runtimes as a service" in req_lower and limiting:
        return "adjacent", ratio, matched

    strength = "direct" if ratio >= 0.55 else "adjacent" if ratio >= 0.25 else "missing"
    if limiting and strength == "direct":
        strength = "adjacent"
    return strength, ratio, matched


def score_requirements(requirements: list[str], resume: str, label: str) -> CategoryScore:
    if not requirements:
        return CategoryScore(0, [f"No explicit {label.lower()} requirements were parsed."])
    points, findings = [], []
    for requirement in requirements:
        strength, _, matched = requirement_match(requirement, resume)
        points.append(100 if strength == "direct" else 55 if strength == "adjacent" else 0)
        findings.append(f"{strength.title()}: {requirement} (matched: {', '.join(matched[:8]) or 'none'}).")
    return CategoryScore(round(sum(points) / len(points)), findings)


def score_language(markdown: str, requirements: list[str]) -> CategoryScore:
    score = 100
    findings = []
    resume_tokens = tokens(markdown)
    if len(set(resume_tokens)) / max(1, len(resume_tokens)) < 0.32:
        score -= 12
        findings.append("Vocabulary is highly repetitive.")
    if len(resume_tokens) > 1300:
        score -= 10
        findings.append("Resume is unusually dense for ATS and recruiter review.")
    action_hits = len(re.findall(r"(?m)^[-*]\s+(?:Architected|Built|Designed|Developed|Implemented|Led|Created|Automated|Modernized|Rebuilt|Served|Diagnosed|Debugged|Used)\b", markdown, re.I))
    if action_hits < 8:
        score -= 10
        findings.append("Relatively few bullets begin with strong action verbs.")
    requirement_tokens = set(tokens(" ".join(requirements)))
    overlap = len(requirement_tokens & set(resume_tokens)) / max(1, len(requirement_tokens))
    findings.append(f"Qualification-language token coverage: {overlap:.1%}.")
    if overlap < 0.35:
        score -= 20
    elif overlap < 0.50:
        score -= 10
    return CategoryScore(max(0, score), findings)


def score_human(markdown: str) -> CategoryScore:
    score = 100
    findings = []
    lines = markdown.splitlines()
    first_third = "\n".join(lines[:35]).lower()
    if not any(term in first_third for term in ("distributed systems", "systems software", "infrastructure", "backend")):
        score -= 15
        findings.append("Target positioning is not explicit in the first third.")
    bullets = [line for line in lines if line.startswith("- ")]
    if sum(bool(re.search(r"\d", bullet)) for bullet in bullets) < 4:
        score -= 12
        findings.append("Few bullets include scale or measurable context.")
    long_bullets = sum(len(bullet) > 240 for bullet in bullets)
    if long_bullets:
        score -= min(15, long_bullets * 3)
        findings.append(f"{long_bullets} bullets are long enough to hinder scanning.")
    if not findings:
        findings.append("The first third is role-specific and evidence is easy to scan.")
    return CategoryScore(max(0, score), findings)


def disposition(score: int, critical: list[str], targeted_complete: bool) -> str:
    if critical or not targeted_complete:
        return "Not Ready"
    if score >= 90:
        return "Submission Ready"
    if score >= 80:
        return "Strong"
    if score >= 70:
        return "Needs Revision"
    return "Not Ready"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", type=Path, required=True)
    parser.add_argument("--docx", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--job", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--pass-number", type=int, default=0, choices=range(0, 4))
    args = parser.parse_args()
    for path in (args.resume, args.docx, args.pdf):
        if not path.exists():
            parser.error(f"missing input: {path}")

    markdown = args.resume.read_text(encoding="utf-8")
    docx, pdf = extract_docx(args.docx), extract_pdf(args.pdf)
    job = args.job.read_text(encoding="utf-8") if args.job else None
    parseability = score_parseability(markdown, docx, pdf)
    completeness = score_completeness(markdown)
    human = score_human(markdown)
    rows = []

    if job:
        required, preferred = extract_requirements(job)
        required_score = score_requirements(required, markdown, "Required")
        preferred_score = score_requirements(preferred, markdown, "Preferred") if preferred else CategoryScore(100, ["No explicit preferred requirements were listed."])
        language = score_language(markdown, required + preferred)
        for kind, requirements in (("Required", required), ("Preferred", preferred)):
            for requirement in requirements:
                strength, _, matched = requirement_match(requirement, markdown)
                rows.append((kind, strength, requirement, matched))
        scores = {
            "Artifact parseability and structure": (parseability, 25),
            "Required-information completeness": (completeness, 10),
            "Required job-requirement evidence": (required_score, 30),
            "Preferred job-requirement evidence": (preferred_score, 15),
            "Language and keyword quality": (language, 10),
            "Human readability and positioning": (human, 10),
        }
        targeted_complete = bool(required)
    else:
        language = score_language(markdown, [])
        scores = {
            "Artifact parseability and structure": (parseability, 50),
            "Required-information completeness": (completeness, 20),
            "Language and keyword quality": (language, 15),
            "Human readability and positioning": (human, 15),
        }
        targeted_complete = True

    overall = round(sum(category.score * weight for category, weight in scores.values()) / sum(weight for _, weight in scores.values()))
    critical = []
    if parseability.score < 60:
        critical.append("Generated artifacts do not parse reliably enough.")
    if completeness.score < 60:
        critical.append("Required contact or work-history structure is incomplete.")
    final_disposition = disposition(overall, critical, targeted_complete)
    hashes = {"resume": sha256(args.resume), "docx": sha256(args.docx), "pdf": sha256(args.pdf)}
    if args.job:
        hashes["job"] = sha256(args.job)

    validated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    output = [
        "# ATS Readiness Report", "",
        f"- **Validated:** {validated}",
        f"- **Validator:** CareerPortfolio ATS Validator v{VERSION}",
        f"- **Score type:** {'Targeted readiness' if job else 'Generic baseline'}",
        f"- **Overall score:** {overall}/100",
        f"- **Disposition:** {final_disposition}",
        f"- **Autonomous revision pass:** {args.pass_number} of 3", "",
        "## Category Scores", "", "| Category | Score | Weight |", "|---|---:|---:|",
    ]
    output.extend(f"| {name} | {category.score} | {weight}% |" for name, (category, weight) in scores.items())
    output.extend(["", "## Critical Failures", ""])
    output.extend([f"- {item}" for item in critical] or ["- None detected."])
    for name, (category, _) in scores.items():
        output.extend(["", f"## {name}", ""])
        output.extend(f"- {finding}" for finding in category.findings)
    if rows:
        output.extend(["", "## Requirement-to-Evidence Matrix", "", "| Type | Strength | Requirement | Matched terms |", "|---|---|---|---|"])
        for kind, strength, requirement, matched in rows:
            output.append(f"| {kind} | {strength.title()} | {requirement.replace('|', '/')} | {', '.join(matched[:10]) or 'None'} |")
    output.extend(["", "## Artifact Versions", ""])
    output.extend(f"- `{name}`: `{value}`" for name, value in hashes.items())
    output.extend(["", "## Recommended Next Action", ""])
    output.append("- Submit after final human visual review." if final_disposition == "Submission Ready" else "- Review evidence gaps and make only truthful, material improvements before submission.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(output) + "\n", encoding="utf-8")

    result = {
        "validator_version": VERSION,
        "overall_score": overall,
        "disposition": final_disposition,
        "targeted_complete": targeted_complete,
        "pass_number": args.pass_number,
        "categories": {name: {**asdict(category), "weight": weight} for name, (category, weight) in scores.items()},
        "critical_failures": critical,
        "hashes": hashes,
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{overall} {final_disposition}")
    return 2 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
